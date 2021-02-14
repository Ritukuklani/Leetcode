class Solution:
    def longestOnes(self, A, K: int) -> int:
        left = right = 0
        zeros = 0
        max_val = 0
        while right<len(A):
            if A[right]==0:
                zeros+=1
                if zeros>K:
                    while A[left]!=0:
                        left+=1
                    left+=1
                    zeros-=1
                right+=1
            else:
                right+=1
            max_val = max(max_val, right-left)
        return max_val