class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0

        for i, h in enumerate(heights + [0]):
            start = i

            while stack and stack[-1][1] > h:
                j, height = stack.pop()
                ans = max(ans, height * (i - j))
                start = j

            stack.append((start, h))

        return ans