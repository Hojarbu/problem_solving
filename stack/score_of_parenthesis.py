# https://leetcode.com/problems/min-stack/
# https://www.youtube.com/watch?v=Pv35fyoKtUA


def scoreOfParentheses(self, s: str) -> int:
    stack = []
    for i in s:
        _sum = 0
        if i == '(':
            stack.append(0)
        else:
            while stack and stack[-1] != 0:
                _sum += stack.pop()
            _sum = max(2 * _sum, 1)
            stack.pop()
            stack.append(_sum)
    return sum(stack)