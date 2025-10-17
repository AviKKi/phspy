import os
import sys

# Ensure the project root is on sys.path so `import crawler` works when tests
# are collected/executed from within the `crawler/` directory.
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


