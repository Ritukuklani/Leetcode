class NumArray:

    def __init__(self, nums): #nums is a List of int
        n = len(nums)
        self.nums = nums
        self.tree = [0 for i in range(2*n)]
        i = n
        for j in range(n):
            self.tree[i+j] = nums[j]
        for j in range(n-1, 0, -1):
            self.tree[j] = self.tree[2*j] + self.tree[2*j+1]
        print(self.tree)

    def update(self, index: int, val: int) -> None:
        i = index+len(self.nums)
        change = val - self.tree[i]
        while i>0:
            self.tree[i] += change
            i=i//2

    def sumRange(self, left: int, right: int) -> int:
        left+=len(self.nums)
        right+=len(self.nums)
        sum_val = 0
        while (left<=right):
            if(left%2==1):
                sum_val+=self.tree[left]
                left+=1
            if(right%2==0):
                sum_val+=self.tree[right]
                right-=1
            left = left//2
            right = right//2
        return sum_val
            
        

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)