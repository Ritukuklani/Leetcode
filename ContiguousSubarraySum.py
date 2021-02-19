class Solution:
    import collections
    def checkSubarraySum(self, nums, k: int) -> bool:
        # count = 0
        # for i in range(len(nums)-1):
        #     curr_sum = nums[i]
        #     for j in range(i+1, len(nums)):
        #         curr_sum+=nums[j]
        #         if k==0 and curr_sum==0:
        #             count+=1
        #         elif k!=0 and curr_sum%k == 0:
        #             count+=1
        # return count
        
        # Using hashmap
        
        # my_dict = collections.defaultdict(int)
        my_dict = {}
        my_dict[0] = -1
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            if k!=0:
                curr_sum = curr_sum%k
            if curr_sum in my_dict: 
                if i - my_dict[curr_sum]>1: 
                    return True
            else:
                my_dict[curr_sum] = i
        return False
                
            
        
                