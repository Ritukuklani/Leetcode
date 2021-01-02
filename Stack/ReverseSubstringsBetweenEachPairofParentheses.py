class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        temp = []
        for i in range(len(s)):
            if s[i]!=")":
                stack.append(s[i])
            if s[i] == ")":
                temp = []
                ans = stack.pop()
                if ans != "(":
                    temp.append(ans[::-1])
                while ans!="(":
                    ans = stack.pop()
                    if ans == "(":
                        break
                    temp.append(ans[::-1])
                stack.append("".join(temp))
            if i==len(s)-1 and s[i]!=")":
                return "".join(stack)
        return "".join(stack)
            
                
                
                