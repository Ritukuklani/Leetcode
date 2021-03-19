class Solution:
    # Find the intervals of each character and then merge the intervals
    def partitionLabels(self, S: str):  #Return type -> List[int]:
        first_occurence = {}
        last_occurence = {}
        for i in range(len(S)):
            if S[i] not in first_occurence:
                first_occurence[S[i]] = i
            last_occurence[S[i]] = i
        intervals = [[val, last_occurence[key]] for key, val in first_occurence.items()]
        ans = [intervals[0], ]
        i = 1
        while i<len(intervals):
            if intervals[i][0]<=ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
            else:
                ans.append(intervals[i])
            i+=1
        res = []
        for i in range(len(ans)):
            res.append(ans[i][1]- ans[i][0]+1)
        return res
        