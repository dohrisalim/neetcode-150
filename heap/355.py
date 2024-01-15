class Twitter:

		def __init__(self):

			self.followers = {}
			self.tweets = []

		def postTweet(self, userId: int, tweetId: int) -> None:

			if not userId in self.followers:
				self.followers[userId] = [userId]

			self.tweets.append([userId, tweetId])

		def getNewsFeed(self, userId: int) -> List[int]:

			result = []
			count = 1      
			index = len(self.tweets) - 1

			while count < 11 and index > -1:

				if self.tweets[index][0] in self.followers[userId]:
					result.append(self.tweets[index][1])
					count = count + 1
				index = index - 1

			return result

		def follow(self, followerId: int, followeeId: int) -> None:

			if not followerId in self.followers:
				self.followers[followerId] = [followerId]

			self.followers[followerId].append(followeeId)

		def unfollow(self, followerId: int, followeeId: int) -> None:

			if followeeId in self.followers[followerId]:
				self.followers[followerId].remove(followeeId)