from sortedcontainers import SortedDict
class Leaderboard:

    def __init__(self):
        self.scores = {}
        self.sortedScores = SortedDict()

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.scores:
            self.scores[playerId] = score
            self.sortedScores[-score] = self.sortedScores.get(-score, 0) + 1
        else:
            preScore = self.scores[playerId]
            if self.sortedScores[-preScore]==1:
                del self.sortedScores[-preScore]
            else:
                self.sortedScores[-preScore] = self.sortedScores[-preScore]-1
            newScore = preScore+ score
            self.scores[playerId] = newScore
            self.sortedScores[-newScore] = self.sortedScores.get(-newScore,0) + 1

    def top(self, K: int) -> int:
        ans = 0
        curr = 0
        for key, val in self.sortedScores.items():
            count = self.sortedScores.get(key)
            for i in range(count):
                ans+=key
                curr+=1
                if curr==K:
                    break
            if curr==K:
                break
        return abs(ans)

    def reset(self, playerId: int) -> None:
        score = self.scores[playerId]
        if self.sortedScores[-score]==1:
            del self.sortedScores[-score]
        else:
            self.sortedScores[-score] = self.sortedScores.get(-score)-1
        del self.scores[playerId]
            


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
