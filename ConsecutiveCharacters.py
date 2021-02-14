class Solution:
    def maxPower(self, s: str) -> int:
        left = right = 0
        ans = 0
        while right<len(s):
            if s[right]==s[left]:
                right+=1
            else:
                left = right
            ans = max(ans, right-left)
        return ans