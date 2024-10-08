class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[-1]
        le=0
        for i in range(len(s)):
            if s[i]=="(":
                stack.append(i)
            else:
                stack.pop()
                if len(stack)==0:
                    stack.append(i)
                else:
                    le=max(le,i-stack[-1])
        return le

        