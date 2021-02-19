class Solution:
    def maxSubArrayLen(self, nums, k: int) -> int:
        if k==0 and len(nums)==0:
            return 0
        visited_dict = {}
        visited_dict[0] = -1
        curr_sum = 0
        max_val = float("-inf")
        for i in range(len(nums)):
            curr_sum+=nums[i]
            if (curr_sum-k) in visited_dict:
                max_val = max(max_val, i-visited_dict[curr_sum-k])
            if curr_sum not in visited_dict:
                visited_dict[curr_sum] = i
        return max_val if max_val!=float("-inf") else 0