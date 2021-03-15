class Solution:
    def shortestDistance(self, wordsDict, word1: str, word2: str) -> int:   # wordsDict is a list of str
        p1, p2 = None, None
        min_dist = float("inf")
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                p1 = i
            if wordsDict[i] == word2:
                p2 = i
            if p1!=None and p2!=None:
                min_dist = min(min_dist, abs(p1-p2))
        return min_dist