"""
https://leetcode.com/problems/design-twitter/
Design Twitter
"""

from collections import defaultdict


class Tweet:
    def __init__(self, user_id: int, tweet_id: int):
        self.user_id = user_id
        self.tweet_id = tweet_id


class Twitter:
    def __init__(self):
        self.tweets: [Tweet] = []
        self.following = defaultdict(set)

    def postTweet(self, user_id: int, tweet_id: int) -> None:
        self.tweets.append(Tweet(user_id, tweet_id))

    def getNewsFeed(self, user_id: int) -> [int]:
        # If I want to get my tweets and my followings'
        # I should check "what is `user_id`'s following list?"
        following = self.following[user_id]

        def _is_following(tweet: Tweet) -> bool:
            if tweet.user_id in following or tweet.user_id == user_id:
                return True
            else:
                return False

        # And then I should pick in some specific standards.
        feed = list(filter(_is_following, self.tweets))
        feed = list(map(lambda x: x.tweet_id, feed))
        feed.reverse()
        return feed

    def follow(self, follower_id: int, followee_id: int) -> None:
        self.following[follower_id].add(followee_id)

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        if followee_id in self.following[follower_id]:
            self.following[follower_id].remove(followee_id)


# Your Twitter object will be instantiated and called as such:
t = Twitter()
t.postTweet(1, 5)
t.postTweet(1, 3)
t.postTweet(1, 101)
t.postTweet(1, 13)
t.postTweet(1, 10)
t.postTweet(1, 2)
t.postTweet(1, 94)
t.postTweet(1, 505)
t.postTweet(1, 333)
t.postTweet(1, 22)
t.postTweet(1, 11)
assert t.getNewsFeed(1) == [11, 22, 333, 505, 94, 2, 10, 13, 101, 3, 5]
