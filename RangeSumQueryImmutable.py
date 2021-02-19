class NumArray:
    # Using caching 
    # We can use O(n*2) space, O(1) time per query and O(n*2) time for pre-computation or 
    # we can use O(n) space, O(1) time per query and O(n) time for pre-computation
    def __init__(self, nums):
        self.nums = nums
        self.sum_dict = {}
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            self.sum_dict[i] = curr_sum 
        # for i in range(len(self.nums)):
        #     curr_sum = 0
        #     for j in range(i, len(self.nums)):
        #         curr_sum+=self.nums[j]
        #         self.sum_dict[(i, j)] = curr_sum
        
    def sumRange(self, i: int, j: int) -> int:
        return self.sum_dict[j] - self.sum_dict[i-1] if i>=1 else self.sum_dict[j]