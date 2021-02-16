class Solution:
    def findPoisonedDuration(self, timeSeries, duration: int) -> int:
        end = 0
        res = 0
        for i in range(len(timeSeries)):
            if timeSeries[i]<end:
                res += (timeSeries[i] + duration - end)
                end = timeSeries[i] + duration
            else:
                res += (timeSeries[i] + duration - timeSeries[i])
                end = timeSeries[i]+duration
        return res  