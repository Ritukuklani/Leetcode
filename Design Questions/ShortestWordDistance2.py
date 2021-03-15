class WordDistance:
    # import collections
    def __init__(self, wordsDict):  #: wordsDict is  a List[str]
        self.wordsDict = wordsDict
        # self.dist = collections.defaultdict(int)
        self.dist = {}
        for i in range(len(self.wordsDict)):
            for j in range(i+1, len(self.wordsDict)):
                if (self.wordsDict[i], self.wordsDict[j]) in self.dist and self.dist[(self.wordsDict[i], self.wordsDict[j])]>j-i:
                    self.dist[(self.wordsDict[i], self.wordsDict[j])] = j-i
                elif (self.wordsDict[j], self.wordsDict[i]) in self.dist and self.dist[(self.wordsDict[j], self.wordsDict[i])]>j-i:
                    self.dist[(self.wordsDict[j], self.wordsDict[i])] = j-i
                elif (self.wordsDict[j], self.wordsDict[i]) not in self.dist and (self.wordsDict[i], self.wordsDict[j]) not in self.dist:
                    self.dist[(self.wordsDict[i], self.wordsDict[j])] = j-i
        print(self.dist)
                    

    def shortest(self, word1: str, word2: str) -> int:
        if word1==word2:
            return 0
        return self.dist[(word1, word2)] or self.dist[(word2, word1)]


###################################################################################################################
    # O(n) time complexity

#class WordDistance:

    # def __init__(self, wordsDict):
    #     #self.word_pos = collections.defaultdict(list)
    #     self.word_pos = {}
    #     for i in range(len(wordsDict)):
    #         self.word_pos[wordsDict[i]].append(i)
    #     # print(word_pos)

    # def shortest(self, word1: str, word2: str) -> int:
    #     loc1 = self.word_pos[word1]
    #     loc2 = self.word_pos[word2]
    #     p1, p2 = 0, 0
    #     min_diff = float("inf")
    #     while p1<len(loc1) and p2<len(loc2):
    #         curr_min = abs(loc1[p1] - loc2[p2])
    #         if loc1[p1]<loc2[p2]:
    #             p1+=1
    #         else:
    #             p2+=1
    #         min_diff = min(min_diff, curr_min)
    #     return min_diff


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)