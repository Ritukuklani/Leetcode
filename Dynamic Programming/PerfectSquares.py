class Solution:
    def numSquares(self, n: int) -> int:
        # def helper(arr, start, curr):
        #     # print(curr, sum(curr))
        #     if sum(curr) > n:
        #         return
        #     if sum(curr) == n:
        #         self.result = min(self.result, len(curr))
        #     for i in range(start, len(arr)):
        #         helper(arr, start, curr+[arr[i]])
        # self.result = float("inf")
        # arr = [i*i for i in range(1, n//4+1)]
        # helper(arr, 0, [])
        # return self.result
        squares = [i*i for i in range(1, n+1)]
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        for i in range(1, n+1):
            for square in squares:
                if i<square:
                    break
                dp[i] = min(dp[i], dp[i-square]+1)
        return dp[-1]