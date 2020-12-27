class Solution:
    def partition(self, s: str):      # return type : List[List[str]]   
        def isPalindrome(string):
            length = len(string)
            for i in range(length//2):
                if string[i]!=string[length-1-i]:
                    return False
            return True
        def backtrack(s, start, curr, result):
            if start>=len(s):    
                result.append(list(curr))
            for i in range(start, len(s)):
                if isPalindrome(s[start:i+1]):
                    curr.append(s[start:i+1])
                    backtrack(s, i+1, curr, result)
                    curr.pop()
        result = []
        backtrack(s, 0, [], result)
        return result
        