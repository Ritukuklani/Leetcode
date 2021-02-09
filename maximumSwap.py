class Solution:
    """If the there are two numbers greater than ith number, choose the one towards the units place."""
    def maximumSwap(self, num: int) -> int:
        num_s = str(num)
        max_num = 0
        index = 0
        for i in range(len(num_s)-1):
            for j in range(i+1, len(num_s)):
                if int(num_s[j])>int(num_s[i]):
                    if int(num_s[j])>=max_num:
                        max_num = int(num_s[j])
                        index = j
                        # print(max_num, index)
            if index:
                
                ans = num_s[:i] + num_s[index] + num_s[i+1:index]+num_s[i] + num_s[index+1:]
                return ans
        return num_s