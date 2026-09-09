class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        gr = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for x in s:
            if x in gr:
                if stack and stack[-1] == gr[x]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(x)

        return len(stack) == 0