class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        curr_sum = 0
        flip_sum = 0
        max_sum = 0
        for i in range(len(nums)):
            if nums[i]==1:
                curr_sum+=1
                flip_sum+=1
                max_sum = max(max_sum, max(curr_sum, flip_sum))
            else:
                flip_sum = curr_sum + 1
                curr_sum = 0
                max_sum = max(max_sum, max(curr_sum, flip_sum))
        return max_sum
                