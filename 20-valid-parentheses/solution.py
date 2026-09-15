// 3 ms | 12.4 MB
class Solution(object):
    def isValid(self, s):
        d = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for ch in s:
            if ch in d:
                stack.append(ch)
            else:
                if not stack:
                    return False

                if d[stack[-1]] != ch:
                    return False

                stack.pop()

        return len(stack) == 0