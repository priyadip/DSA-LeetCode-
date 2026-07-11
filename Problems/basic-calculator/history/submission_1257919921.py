class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        operand = 0
        result = 0  # Final result
        sign = 1  # Sign of the current operand

        for char in s:
            if char.isdigit():
                operand = operand * 10 + int(char)
            elif char == '+':
                result += sign * operand
                operand = 0
                sign = 1
            elif char == '-':
                result += sign * operand
                operand = 0
                sign = -1
            elif char == '(':
                stack.append((result, sign))
                result = 0
                sign = 1
            elif char == ')':
                result += sign * operand
                operand = 0
                prev_result, prev_sign = stack.pop()
                result = prev_result + prev_sign * result

        return result + sign * operand