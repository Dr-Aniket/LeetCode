class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        count = 0
        for brack in s:
            if brack == '(':
                stack.append('(')
            else:
                if stack:
                    stack.pop()
                else:
                    count += 1
        return count + len(stack)