
test_query = {"kind":"Document","definitions":[{"kind":"OperationDefinition","operation":"query","name":{"kind":"Name","value":"LeaderboardDailyPage"},"variableDefinitions":[{"kind":"VariableDefinition","variable":{"kind":"Variable","name":{"kind":"Name","value":"year"}},"type":{"kind":"NonNullType","type":{"kind":"NamedType","name":{"kind":"Name","value":"Int"}}}},{"kind":"VariableDefinition","variable":{"kind":"Variable","name":{"kind":"Name","value":"month"}},"type":{"kind":"NonNullType","type":{"kind":"NamedType","name":{"kind":"Name","value":"Int"}}}},{"kind":"VariableDefinition","variable":{"kind":"Variable","name":{"kind":"Name","value":"day"}},"type":{"kind":"NonNullType","type":{"kind":"NamedType","name":{"kind":"Name","value":"Int"}}}},{"kind":"VariableDefinition","variable":{"kind":"Variable","name":{"kind":"Name","value":"cursor"}},"type":{"kind":"NamedType","name":{"kind":"Name","value":"String"}}},{"kind":"VariableDefinition","variable":{"kind":"Variable","name":{"kind":"Name","value":"order"}},"type":{"kind":"NamedType","name":{"kind":"Name","value":"PostsOrder"}}},{"kind":"VariableDefinition","variable":{"kind":"Variable","name":{"kind":"Name","value":"featured"}},"type":{"kind":"NonNullType","type":{"kind":"NamedType","name":{"kind":"Name","value":"Boolean"}}}}],"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"FragmentSpread","name":{"kind":"Name","value":"LeaderboardCommonFragment"}},{"kind":"Field","name":{"kind":"Name","value":"homefeedItems"},"arguments":[{"kind":"Argument","name":{"kind":"Name","value":"featured"},"value":{"kind":"Variable","name":{"kind":"Name","value":"featured"}}},{"kind":"Argument","name":{"kind":"Name","value":"first"},"value":{"kind":"IntValue","value":"20"}},{"kind":"Argument","name":{"kind":"Name","value":"year"},"value":{"kind":"Variable","name":{"kind":"Name","value":"year"}}},{"kind":"Argument","name":{"kind":"Name","value":"month"},"value":{"kind":"Variable","name":{"kind":"Name","value":"month"}}},{"kind":"Argument","name":{"kind":"Name","value":"day"},"value":{"kind":"Variable","name":{"kind":"Name","value":"day"}}},{"kind":"Argument","name":{"kind":"Name","value":"order"},"value":{"kind":"Variable","name":{"kind":"Name","value":"order"}}},{"kind":"Argument","name":{"kind":"Name","value":"after"},"value":{"kind":"Variable","name":{"kind":"Name","value":"cursor"}}}],"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"FragmentSpread","name":{"kind":"Name","value":"LeaderboardPostListFragment"}}]}}]}},{"kind":"FragmentDefinition","name":{"kind":"Name","value":"GoldenKittyYearsFragment"},"typeCondition":{"kind":"NamedType","name":{"kind":"Name","value":"Query"}},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"goldenKittyHof"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"years"}}]}}]}},{"kind":"FragmentDefinition","name":{"kind":"Name","value":"PostStatusIconFragment"},"typeCondition":{"kind":"NamedType","name":{"kind":"Name","value":"Post"}},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"productState"}}]}},{"kind":"FragmentDefinition","name":{"kind":"Name","value":"PostThumbnailFragment"},"typeCondition":{"kind":"NamedType","name":{"kind":"Name","value":"Post"}},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"name"}},{"kind":"Field","name":{"kind":"Name","value":"thumbnailImageUuid"}},{"kind":"FragmentSpread","name":{"kind":"Name","value":"PostStatusIconFragment"}}]}},{"kind":"FragmentDefinition","name":{"kind":"Name","value":"UsePostVoteFragment"},"typeCondition":{"kind":"NamedType","name":{"kind":"Name","value":"Post"}},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"hasVoted"}},{"kind":"Field","name":{"kind":"Name","value":"latestScore"}},{"kind":"Field","name":{"kind":"Name","value":"launchDayScore"}},{"kind":"Field","name":{"kind":"Name","value":"disabledWhenScheduled"}},{"kind":"Field","name":{"kind":"Name","value":"featuredAt"}},{"kind":"Field","name":{"kind":"Name","value":"updatedAt"}},{"kind":"Field","name":{"kind":"Name","value":"createdAt"}},{"kind":"Field","name":{"kind":"Name","value":"embargoPreviewAt"}},{"kind":"Field","name":{"kind":"Name","value":"product"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"isSubscribed"}}]}}]}},{"kind":"FragmentDefinition","name":{"kind":"Name","value":"PostVoteButtonFragment"},"typeCondition":{"kind":"NamedType","name":{"kind":"Name","value":"Post"}},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"FragmentSpread","name":{"kind":"Name","value":"UsePostVoteFragment"}}]}},{"kind":"FragmentDefinition","name":{"kind":"Name","value":"EmbargoedPostCountdownFragment"},"typeCondition":{"kind":"NamedType","name":{"kind":"Name","value":"Post"}},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"featuredAt"}},{"kind":"Field","name":{"kind":"Name","value":"scheduledAt"}},{"kind":"Field","name":{"kind":"Name","value":"createdAt"}}]}},{"kind":"FragmentDefinition","name":{"kind":"Name","value":"EmbargoedPostItemNotifyButtonFragment"},"typeCondition":{"kind":"NamedType","name":{"kind":"Name","value":"Post"}},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"isSubscribed"}}]}},{"kind":"FragmentDefinition","name":{"kind":"Name","value":"EmbargoedPostItemFragment"},"typeCondition":{"kind":"NamedType","name":{"kind":"Name","value":"Post"}},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"name"}},{"kind":"Field","name":{"kind":"Name","value":"slug"}},{"kind":"Field","name":{"kind":"Name","value":"tagline"},"arguments":[{"kind":"Argument","name":{"kind":"Name","value":"respectEmbargo"},"value":{"kind":"BooleanValue","value":True}}]},{"kind":"Field","name":{"kind":"Name","value":"hideVotesCount"}},{"kind":"Field","name":{"kind":"Name","value":"redirectToProduct"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"slug"}}]}},{"kind":"Field","name":{"kind":"Name","value":"product"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"slug"}}]}},{"kind":"FragmentSpread","name":{"kind":"Name","value":"PostThumbnailFragment"}},{"kind":"FragmentSpread","name":{"kind":"Name","value":"PostVoteButtonFragment"}},{"kind":"FragmentSpread","name":{"kind":"Name","value":"EmbargoedPostCountdownFragment"}},{"kind":"FragmentSpread","name":{"kind":"Name","value":"EmbargoedPostItemNotifyButtonFragment"}}]}},{"kind":"FragmentDefinition","name":{"kind":"Name","value":"UserImage"},"typeCondition":{"kind":"NamedType","name":{"kind":"Name","value":"User"}},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"name"}},{"kind":"Field","name":{"kind":"Name","value":"username"}},{"kind":"Field","name":{"kind":"Name","value":"avatarUrl"}}]}},{"kind":"FragmentDefinition","name":{"kind":"Name","value":"FeaturedComment"},"typeCondition":{"kind":"NamedType","name":{"kind":"Name","value":"Comment"}},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"path"}},{"kind":"Field","name":{"kind":"Name","value":"bodyText"}},{"kind":"Field","name":{"kind":"Name","value":"isPinned"}},{"kind":"Field","name":{"kind":"Name","value":"subject"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}}]}},{"kind":"Field","name":{"kind":"Name","value":"user"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"username"}},{"kind":"FragmentSpread","name":{"kind":"Name","value":"UserImage"}}]}}]}},{"kind":"FragmentDefinition","name":{"kind":"Name","value":"PostItemVoteButtonFragment"},"typeCondition":{"kind":"NamedType","name":{"kind":"Name","value":"Post"}},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"hideVotesCount"}},{"kind":"Field","name":{"kind":"Name","value":"featuredAt"}},{"kind":"Field","name":{"kind":"Name","value":"createdAt"}},{"kind":"Field","name":{"kind":"Name","value":"disabledWhenScheduled"}},{"kind":"Field","name":{"kind":"Name","value":"embargoPreviewAt"}},{"kind":"Field","name":{"kind":"Name","value":"latestScore"}},{"kind":"Field","name":{"kind":"Name","value":"launchDayScore"}},{"kind":"FragmentSpread","name":{"kind":"Name","value":"UsePostVoteFragment"}}]}},{"kind":"FragmentDefinition","name":{"kind":"Name","value":"PostItemCommentsButtonFragment"},"typeCondition":{"kind":"NamedType","name":{"kind":"Name","value":"Post"}},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"slug"}},{"kind":"Field","name":{"kind":"Name","value":"commentsCount"}},{"kind":"Field","name":{"kind":"Name","value":"product"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"slug"}}]}}]}},{"kind":"FragmentDefinition","name":{"kind":"Name","value":"PostItemExternalLinkButtonFragment"},"typeCondition":{"kind":"NamedType","name":{"kind":"Name","value":"Post"}},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"shortenedUrl"}}]}},{"kind":"FragmentDefinition","name":{"kind":"Name","value":"PostItemFragment"},"typeCondition":{"kind":"NamedType","name":{"kind":"Name","value":"Post"}},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"slug"}},{"kind":"Field","name":{"kind":"Name","value":"name"}},{"kind":"Field","name":{"kind":"Name","value":"tagline"},"arguments":[{"kind":"Argument","name":{"kind":"Name","value":"respectEmbargo"},"value":{"kind":"BooleanValue","value":True}}]},{"kind":"Field","name":{"kind":"Name","value":"shortenedUrl"}},{"kind":"Field","name":{"kind":"Name","value":"dailyRank"}},{"kind":"Field","name":{"kind":"Name","value":"weeklyRank"}},{"kind":"Field","name":{"kind":"Name","value":"monthlyRank"}},{"kind":"Field","name":{"kind":"Name","value":"product"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"slug"}}]}},{"kind":"Field","name":{"kind":"Name","value":"redirectToProduct"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"slug"}}]}},{"kind":"FragmentSpread","name":{"kind":"Name","value":"PostThumbnailFragment"}},{"kind":"FragmentSpread","name":{"kind":"Name","value":"PostItemVoteButtonFragment"}},{"kind":"FragmentSpread","name":{"kind":"Name","value":"PostItemCommentsButtonFragment"}},{"kind":"FragmentSpread","name":{"kind":"Name","value":"PostItemExternalLinkButtonFragment"}}]}},{"kind":"FragmentDefinition","name":{"kind":"Name","value":"HomefeedItemPostItemFriendVotersFragment"},"typeCondition":{"kind":"NamedType","name":{"kind":"Name","value":"Post"}},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"friendVoters"},"arguments":[{"kind":"Argument","name":{"kind":"Name","value":"first"},"value":{"kind":"IntValue","value":"1"}}],"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"edges"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"node"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"name"}},{"kind":"Field","name":{"kind":"Name","value":"username"}},{"kind":"FragmentSpread","name":{"kind":"Name","value":"UserImage"}}]}}]}},{"kind":"Field","name":{"kind":"Name","value":"totalCount"}}]}}]}},{"kind":"FragmentDefinition","name":{"kind":"Name","value":"HomefeedItemPostItemTopicTagsFragment"},"typeCondition":{"kind":"NamedType","name":{"kind":"Name","value":"Post"}},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"topics"},"arguments":[{"kind":"Argument","name":{"kind":"Name","value":"first"},"value":{"kind":"IntValue","value":"3"}}],"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"edges"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"node"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"slug"}},{"kind":"Field","name":{"kind":"Name","value":"name"}}]}}]}}]}}]}},{"kind":"FragmentDefinition","name":{"kind":"Name","value":"HomefeedItemPostItemFragment"},"typeCondition":{"kind":"NamedType","name":{"kind":"Name","value":"Post"}},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"featuredComment"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"FragmentSpread","name":{"kind":"Name","value":"FeaturedComment"}}]}},{"kind":"FragmentSpread","name":{"kind":"Name","value":"PostItemFragment"}},{"kind":"FragmentSpread","name":{"kind":"Name","value":"HomefeedItemPostItemFriendVotersFragment"}},{"kind":"FragmentSpread","name":{"kind":"Name","value":"HomefeedItemPostItemTopicTagsFragment"}}]}},{"kind":"FragmentDefinition","name":{"kind":"Name","value":"HomefeedItemPostFragment"},"typeCondition":{"kind":"NamedType","name":{"kind":"Name","value":"Post"}},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"FragmentSpread","name":{"kind":"Name","value":"EmbargoedPostItemFragment"}},{"kind":"FragmentSpread","name":{"kind":"Name","value":"HomefeedItemPostItemFragment"}}]}},{"kind":"FragmentDefinition","name":{"kind":"Name","value":"AdFragment"},"typeCondition":{"kind":"NamedType","name":{"kind":"Name","value":"Ad"}},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"subject"}},{"kind":"Field","name":{"kind":"Name","value":"post"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"slug"}},{"kind":"Field","name":{"kind":"Name","value":"name"}},{"kind":"Field","name":{"kind":"Name","value":"updatedAt"}},{"kind":"Field","name":{"kind":"Name","value":"commentsCount"}},{"kind":"Field","name":{"kind":"Name","value":"topics"},"arguments":[{"kind":"Argument","name":{"kind":"Name","value":"first"},"value":{"kind":"IntValue","value":"3"}}],"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"edges"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"node"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"slug"}},{"kind":"Field","name":{"kind":"Name","value":"name"}}]}}]}}]}},{"kind":"Field","name":{"kind":"Name","value":"featuredComment"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"FragmentSpread","name":{"kind":"Name","value":"FeaturedComment"}}]}},{"kind":"FragmentSpread","name":{"kind":"Name","value":"PostVoteButtonFragment"}},{"kind":"FragmentSpread","name":{"kind":"Name","value":"PostItemCommentsButtonFragment"}},{"kind":"FragmentSpread","name":{"kind":"Name","value":"PostItemVoteButtonFragment"}},{"kind":"FragmentSpread","name":{"kind":"Name","value":"HomefeedItemPostItemTopicTagsFragment"}}]}},{"kind":"Field","name":{"kind":"Name","value":"name"}},{"kind":"Field","name":{"kind":"Name","value":"tagline"}},{"kind":"Field","name":{"kind":"Name","value":"thumbnailUuid"}},{"kind":"Field","name":{"kind":"Name","value":"largeAssetUuid"}},{"kind":"Field","name":{"kind":"Name","value":"smallAssetUuid"}},{"kind":"Field","name":{"kind":"Name","value":"url"}},{"kind":"Field","name":{"kind":"Name","value":"variationId"}}]}},{"kind":"FragmentDefinition","name":{"kind":"Name","value":"GhostAdFragment"},"typeCondition":{"kind":"NamedType","name":{"kind":"Name","value":"GhostAd"}},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"subject"}}]}},{"kind":"FragmentDefinition","name":{"kind":"Name","value":"HomefeedItemFragment"},"typeCondition":{"kind":"NamedType","name":{"kind":"Name","value":"HomefeedItem"}},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"InlineFragment","typeCondition":{"kind":"NamedType","name":{"kind":"Name","value":"Post"}},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"FragmentSpread","name":{"kind":"Name","value":"HomefeedItemPostFragment"}}]}},{"kind":"InlineFragment","typeCondition":{"kind":"NamedType","name":{"kind":"Name","value":"Ad"}},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"Field","name":{"kind":"Name","value":"channelKind"}},{"kind":"Field","name":{"kind":"Name","value":"smallAssetUuid"}},{"kind":"Field","name":{"kind":"Name","value":"largeAssetUuid"}},{"kind":"FragmentSpread","name":{"kind":"Name","value":"AdFragment"}}]}},{"kind":"InlineFragment","typeCondition":{"kind":"NamedType","name":{"kind":"Name","value":"GhostAd"}},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"id"}},{"kind":"FragmentSpread","name":{"kind":"Name","value":"GhostAdFragment"}}]}}]}},{"kind":"FragmentDefinition","name":{"kind":"Name","value":"LeaderboardCommonFragment"},"typeCondition":{"kind":"NamedType","name":{"kind":"Name","value":"Query"}},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"FragmentSpread","name":{"kind":"Name","value":"GoldenKittyYearsFragment"}}]}},{"kind":"FragmentDefinition","name":{"kind":"Name","value":"LeaderboardPostListFragment"},"typeCondition":{"kind":"NamedType","name":{"kind":"Name","value":"HomefeedItemConnection"}},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"edges"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"node"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"FragmentSpread","name":{"kind":"Name","value":"HomefeedItemFragment"}}]}}]}},{"kind":"Field","name":{"kind":"Name","value":"pageInfo"},"selectionSet":{"kind":"SelectionSet","selections":[{"kind":"Field","name":{"kind":"Name","value":"endCursor"}},{"kind":"Field","name":{"kind":"Name","value":"hasNextPage"}}]}}]}}]}

test_with_typenames = """query LeaderboardDailyPage($year: Int!, $month: Int!, $day: Int!, $cursor: String, $order: PostsOrder, $featured: Boolean!) {
  ...LeaderboardCommonFragment
  homefeedItems(
    featured: $featured
    first: 20
    year: $year
    month: $month
    day: $day
    order: $order
    after: $cursor
  ) {
    ...LeaderboardPostListFragment
    __typename
  }
}

fragment GoldenKittyYearsFragment on Query {
  goldenKittyHof {
    years
    __typename
  }
  __typename
}

fragment PostStatusIconFragment on Post {
  id
  productState
  __typename
}

fragment PostThumbnailFragment on Post {
  id
  name
  thumbnailImageUuid
  ...PostStatusIconFragment
  __typename
}

fragment UsePostVoteFragment on Post {
  id
  hasVoted
  latestScore
  launchDayScore
  disabledWhenScheduled
  featuredAt
  updatedAt
  createdAt
  embargoPreviewAt
  product {
    id
    isSubscribed
    __typename
  }
  __typename
}

fragment PostVoteButtonFragment on Post {
  id
  ...UsePostVoteFragment
  __typename
}

fragment EmbargoedPostCountdownFragment on Post {
  id
  featuredAt
  scheduledAt
  createdAt
  __typename
}

fragment EmbargoedPostItemNotifyButtonFragment on Post {
  id
  isSubscribed
  __typename
}

fragment EmbargoedPostItemFragment on Post {
  id
  name
  slug
  tagline(respectEmbargo: true)
  hideVotesCount
  redirectToProduct {
    id
    slug
    __typename
  }
  product {
    id
    slug
    __typename
  }
  ...PostThumbnailFragment
  ...PostVoteButtonFragment
  ...EmbargoedPostCountdownFragment
  ...EmbargoedPostItemNotifyButtonFragment
  __typename
}

fragment UserImage on User {
  id
  name
  username
  avatarUrl
  __typename
}

fragment FeaturedComment on Comment {
  id
  path
  bodyText
  isPinned
  subject {
    id
    __typename
  }
  user {
    id
    username
    ...UserImage
    __typename
  }
  __typename
}

fragment PostItemVoteButtonFragment on Post {
  id
  hideVotesCount
  featuredAt
  createdAt
  disabledWhenScheduled
  embargoPreviewAt
  latestScore
  launchDayScore
  ...UsePostVoteFragment
  __typename
}

fragment PostItemCommentsButtonFragment on Post {
  id
  slug
  commentsCount
  product {
    id
    slug
    __typename
  }
  __typename
}

fragment PostItemExternalLinkButtonFragment on Post {
  id
  shortenedUrl
  __typename
}

fragment PostItemFragment on Post {
  id
  slug
  name
  tagline(respectEmbargo: true)
  shortenedUrl
  dailyRank
  weeklyRank
  monthlyRank
  product {
    id
    slug
    __typename
  }
  redirectToProduct {
    id
    slug
    __typename
  }
  ...PostThumbnailFragment
  ...PostItemVoteButtonFragment
  ...PostItemCommentsButtonFragment
  ...PostItemExternalLinkButtonFragment
  __typename
}

fragment HomefeedItemPostItemFriendVotersFragment on Post {
  id
  friendVoters(first: 1) {
    edges {
      node {
        id
        name
        username
        ...UserImage
        __typename
      }
      __typename
    }
    totalCount
    __typename
  }
  __typename
}

fragment HomefeedItemPostItemTopicTagsFragment on Post {
  id
  topics(first: 3) {
    edges {
      node {
        id
        slug
        name
        __typename
      }
      __typename
    }
    __typename
  }
  __typename
}

fragment HomefeedItemPostItemFragment on Post {
  id
  featuredComment {
    id
    ...FeaturedComment
    __typename
  }
  ...PostItemFragment
  ...HomefeedItemPostItemFriendVotersFragment
  ...HomefeedItemPostItemTopicTagsFragment
  __typename
}

fragment HomefeedItemPostFragment on Post {
  id
  ...EmbargoedPostItemFragment
  ...HomefeedItemPostItemFragment
  __typename
}

fragment AdFragment on Ad {
  id
  subject
  post {
    id
    slug
    name
    updatedAt
    commentsCount
    topics(first: 3) {
      edges {
        node {
          id
          slug
          name
          __typename
        }
        __typename
      }
      __typename
    }
    featuredComment {
      id
      ...FeaturedComment
      __typename
    }
    ...PostVoteButtonFragment
    ...PostItemCommentsButtonFragment
    ...PostItemVoteButtonFragment
    ...HomefeedItemPostItemTopicTagsFragment
    __typename
  }
  name
  tagline
  thumbnailUuid
  largeAssetUuid
  smallAssetUuid
  url
  variationId
  __typename
}

fragment GhostAdFragment on GhostAd {
  id
  subject
  __typename
}

fragment HomefeedItemFragment on HomefeedItem {
  ... on Post {
    id
    ...HomefeedItemPostFragment
    __typename
  }
  ... on Ad {
    id
    channelKind
    smallAssetUuid
    largeAssetUuid
    ...AdFragment
    __typename
  }
  ... on GhostAd {
    id
    ...GhostAdFragment
    __typename
  }
  __typename
}

fragment LeaderboardCommonFragment on Query {
  ...GoldenKittyYearsFragment
  __typename
}

fragment LeaderboardPostListFragment on HomefeedItemConnection {
  edges {
    node {
      ...HomefeedItemFragment
      __typename
    }
    __typename
  }
  pageInfo {
    endCursor
    hasNextPage
    __typename
  }
  __typename
}"""

test_with_typenames_stripped = """query LeaderboardDailyPage($year:Int!$month:Int!$day:Int!$cursor:String$order:PostsOrder$featured:Boolean!){...LeaderboardCommonFragment homefeedItems(featured:$featured first:20 year:$year month:$month day:$day order:$order after:$cursor){...LeaderboardPostListFragment __typename}}fragment GoldenKittyYearsFragment on Query{goldenKittyHof{years __typename}__typename}fragment PostStatusIconFragment on Post{id productState __typename}fragment PostThumbnailFragment on Post{id name thumbnailImageUuid ...PostStatusIconFragment __typename}fragment UsePostVoteFragment on Post{id hasVoted latestScore launchDayScore disabledWhenScheduled featuredAt updatedAt createdAt embargoPreviewAt product{id isSubscribed __typename}__typename}fragment PostVoteButtonFragment on Post{id ...UsePostVoteFragment __typename}fragment EmbargoedPostCountdownFragment on Post{id featuredAt scheduledAt createdAt __typename}fragment EmbargoedPostItemNotifyButtonFragment on Post{id isSubscribed __typename}fragment EmbargoedPostItemFragment on Post{id name slug tagline(respectEmbargo:true)hideVotesCount redirectToProduct{id slug __typename}product{id slug __typename}...PostThumbnailFragment ...PostVoteButtonFragment ...EmbargoedPostCountdownFragment ...EmbargoedPostItemNotifyButtonFragment __typename}fragment UserImage on User{id name username avatarUrl __typename}fragment FeaturedComment on Comment{id path bodyText isPinned subject{id __typename}user{id username ...UserImage __typename}__typename}fragment PostItemVoteButtonFragment on Post{id hideVotesCount featuredAt createdAt disabledWhenScheduled embargoPreviewAt latestScore launchDayScore ...UsePostVoteFragment __typename}fragment PostItemCommentsButtonFragment on Post{id slug commentsCount product{id slug __typename}__typename}fragment PostItemExternalLinkButtonFragment on Post{id shortenedUrl __typename}fragment PostItemFragment on Post{id slug name tagline(respectEmbargo:true)shortenedUrl dailyRank weeklyRank monthlyRank product{id slug __typename}redirectToProduct{id slug __typename}...PostThumbnailFragment ...PostItemVoteButtonFragment ...PostItemCommentsButtonFragment ...PostItemExternalLinkButtonFragment __typename}fragment HomefeedItemPostItemFriendVotersFragment on Post{id friendVoters(first:1){edges{node{id name username ...UserImage __typename}__typename}totalCount __typename}__typename}fragment HomefeedItemPostItemTopicTagsFragment on Post{id topics(first:3){edges{node{id slug name __typename}__typename}__typename}__typename}fragment HomefeedItemPostItemFragment on Post{id featuredComment{id ...FeaturedComment __typename}...PostItemFragment ...HomefeedItemPostItemFriendVotersFragment ...HomefeedItemPostItemTopicTagsFragment __typename}fragment HomefeedItemPostFragment on Post{id ...EmbargoedPostItemFragment ...HomefeedItemPostItemFragment __typename}fragment AdFragment on Ad{id subject post{id slug name updatedAt commentsCount topics(first:3){edges{node{id slug name __typename}__typename}__typename}featuredComment{id ...FeaturedComment __typename}...PostVoteButtonFragment ...PostItemCommentsButtonFragment ...PostItemVoteButtonFragment ...HomefeedItemPostItemTopicTagsFragment __typename}name tagline thumbnailUuid largeAssetUuid smallAssetUuid url variationId __typename}fragment GhostAdFragment on GhostAd{id subject __typename}fragment HomefeedItemFragment on HomefeedItem{...on Post{id ...HomefeedItemPostFragment __typename}...on Ad{id channelKind smallAssetUuid largeAssetUuid ...AdFragment __typename}...on GhostAd{id ...GhostAdFragment __typename}__typename}fragment LeaderboardCommonFragment on Query{...GoldenKittyYearsFragment __typename}fragment LeaderboardPostListFragment on HomefeedItemConnection{edges{node{...HomefeedItemFragment __typename}__typename}pageInfo{endCursor hasNextPage __typename}__typename}"""

test_hash = "547bb5ae92ec9a7a5ba5a4007def856e7c9ab781a03f9f80060c8656816a6b5a"