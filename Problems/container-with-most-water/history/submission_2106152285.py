class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        j = n-1
        i = 0
        ma = 0
        while i<j:
            h = min(height[i], height[j])
            ar =  h* (j-i)
            ma = max(ma,ar)
            if height[i]<height[j]:
                i += 1
            else:
                j -= 1
        return ma



        