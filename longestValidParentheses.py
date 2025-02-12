from typing import List
def longestValidParentheses(s: str) -> int:
    # write your code here ^_^

    stack = [-1]
    ml = 0
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                ml = max(ml, i - stack[-1])
    return ml


print(longestValidParentheses('(()'))