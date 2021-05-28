import collections
from typing import List


class TweetCounts:

    def __init__(self):
        self.usertweets = collections.defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.usertweets[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if freq == 'minute':
            ms = 60
        elif freq == 'hour':
            ms = 3600
        else:
            ms = 3600 * 60
        answer = [0] * ((endTime - startTime) // ms + 1)
        for time in self.usertweets[tweetName]:
            if startTime <= time <= endTime:
                answer[(time - startTime) // ms] += 1
        return answer

# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
