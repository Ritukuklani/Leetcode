class Solution:
    from collections import OrderedDict
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if len(s)==0 or k==0:
            return 0
        curr_dict = OrderedDict()
        i = j = 0
        max_count = 0
        while j<len(s):
            if s[j] in curr_dict:
                del curr_dict[s[j]]
                curr_dict[s[j]] = j
                j+=1
            else:
                if len(curr_dict)<k:
                    curr_dict[s[j]] = j
                    j+=1
                else:
                    _, idx = curr_dict.popitem(last = False)
                    i = idx+1
            max_count = max(max_count, j-i)
        return max_count
            