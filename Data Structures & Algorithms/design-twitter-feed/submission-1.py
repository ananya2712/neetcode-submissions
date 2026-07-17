class Twitter:

    def __init__(self):
        self.time = 0 
        self.twtMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.twtMap[userId].append([self.time, tweetId])
        self.time -=1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minheap = []
        self.followMap[userId].add(userId)

        for followeeId in self.followMap[userId]:
            if followeeId in self.twtMap:
                index = len(self.twtMap[followeeId]) - 1
                count, tweetId = self.twtMap[followeeId][index]
                heapq.heappush(minheap, [count, tweetId, followeeId, index - 1])

        while minheap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minheap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.twtMap[followeeId][index]
                heapq.heappush(minheap, [count, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
