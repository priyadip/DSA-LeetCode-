class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1

            stack.append(digit)

        if k:
            stack = stack[:-k]

        ans = ''.join(stack).lstrip('0')

        return ans or '0'



        