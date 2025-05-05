import pytest
import requests
import requests_mock
from crawler.utils import generate_date_range, ProductHuntClient, get_products_on_date


# ====== Tests for generate_date_range Function ======

def test_valid_range():
    """Test that generate_date_range returns a correct list of dates for a valid range."""
    assert generate_date_range('2024-03-01', '2024-03-03') == ['2024-03-01', '2024-03-02', '2024-03-03']

def test_single_day():
    """Test that generate_date_range returns a single date when start and end dates are the same."""
    assert generate_date_range('2024-03-10', '2024-03-10') == ['2024-03-10']

def test_invalid_range():
    """Test that generate_date_range returns an empty list when start date is after end date."""
    assert generate_date_range('2024-03-05', '2024-03-01') == []

def test_invalid_format():
    """Test that generate_date_range returns an empty list for improperly formatted date strings."""
    assert generate_date_range('05-03-2024', '10-03-2024') == []


# ====== Tests for ProductHuntClient ======

@pytest.fixture
def client():
    """Fixture to create a ProductHuntClient instance with custom configuration."""
    return ProductHuntClient(max_tries=2, timeout=5)

def test_post_success(client, requests_mock):
    """Test that ProductHuntClient.post returns the correct response on a successful API call."""
    url = client.BASE_URL
    mock_response = {'data': {'homefeedItems': {'edges': []}}}
    requests_mock.post(url, json=mock_response, status_code = 200)

    payload = {'operationName': 'TestQuery'}
    response = client.post(payload)

    assert response == mock_response

def test_post_client_error(client, requests_mock):
    """Test that ProductHuntClient.post handles a 4xx client error and returns None."""
    url = client.BASE_URL
    requests_mock.post(url, status_code=404, json={"error": "Not Found"})

    payload = {"operationName": "TestQuery"}
    response = client.post(payload)

    assert response is None

def test_post_server_error(client, requests_mock):
    """Test that ProductHuntClient.post handles a 5xx server error and retries before returning None."""
    url = client.BASE_URL
    requests_mock.post(url, status_code=500)

    payload = {"operationName": "TestQuery"}
    response = client.post(payload)

    assert response is None

def test_post_timeout(client, requests_mock):
    """Test that ProductHuntClient.post handles request timeouts and returns None."""
    url = client.BASE_URL
    requests_mock.post(url, exc=requests.exceptions.Timeout)

    payload = {"operationName": "TestQuery"}
    response = client.post(payload)

    assert response is None

# ====== Tests for get_products_on_date Function ======

def test_get_products_on_date(client, requests_mock):
    """Test get_products_on_date with mock data"""
    url = client.BASE_URL
    mock_response = {
        "data": {
            "homefeedItems": {
                "edges": [
                    {"node": {"__typename": "Product", "name": "TestProduct", "tagline": "A great product",
                              "votesCount": 100, "createdAt": "2024-03-29",
                              "topics": {"edges": [{"node": {"name": "Tech"}}]},
                              "shortenedUrl": "p/testproduct"}}
                ],
                "pageInfo": {"hasNextPage": False, "endCursor": None}
            }
        }
    }
    requests_mock.post(url, json=mock_response, status_code=200)

    products = get_products_on_date(client, 2024, 3, 29)

    assert len(products) == 1
    assert products[0]["name"] == "TestProduct"
    assert products[0]["votes"] == 100
    assert products[0]["topics"] == ["Tech"]
    assert products[0]["product_url"] == "https://www.producthunt.com/p/testproduct"

def test_get_products_on_date_failure(client, requests_mock):
    """Test get_products_on_date failure scenario"""
    url = client.BASE_URL
    requests_mock.post(url, status_code=500)

    products = get_products_on_date(client, 2024, 3, 29)

    assert products == []