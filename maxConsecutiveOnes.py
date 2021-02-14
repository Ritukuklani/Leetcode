class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        max_count = 0
        curr_count = 0
        for i in range(len(nums)):
            if nums[i]==1:
                curr_count+=1
                max_count = max(max_count, curr_count)
            else:
                curr_count = 0
        return max_count