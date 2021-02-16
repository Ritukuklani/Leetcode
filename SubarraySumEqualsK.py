class Solution:
    def subarraySum(self, nums, k: int) -> int:
        # Brute Force
        count = 0
        for i in range(len(nums)):
            curr_sum = 0
            for j in range(i, len(nums)):
                curr_sum+=nums[j]
                if curr_sum==k:
                    count+=1
        return count
    
        # Using HashMap
        
        # freq = collections.defaultdict(int)
        # curr_sum = 0
        # count = 0
        # freq[0] = 1
        # for i in range(len(nums)):
        #     curr_sum += nums[i]
        #     if (curr_sum-k) in freq:
        #         count+=freq[curr_sum-k]
        #     freq[curr_sum] += 1
        # return count