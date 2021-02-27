class Solution:
    def minSumOfLengths(self, arr, target: int) -> int: # Arr is a list of integers
        sums = {0: -1}
        curr_sum = 0
        dp = [float("inf") for _ in range(len(arr)+1)]
        ans = float("inf")
        for idx, val in enumerate(arr):
            curr_sum+=val
            dp[idx+1] = min(dp[idx+1], dp[idx])
            if curr_sum-target in sums:
                ans = min(ans, idx - sums[curr_sum - target] + dp[sums[curr_sum - target] + 1])
                dp[idx+1] = min(dp[idx+1], idx - sums[curr_sum - target])
            sums[curr_sum] = idx
        return ans if ans!=float("inf") else -1
        
                
                