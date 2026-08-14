class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, ma = 0, len(height) - 1, 0
        while i < j:
            d = j-i
            if height[i] < height[j]:
                ar = height[i]*d
                i += 1
            else:
                ar = height[j]*d
                j -= 1
            if ar > ma:
                ma = ar
        return ma









        # while i<j:
        #     h = min(height[i], height[j])
        #     ar =  h* (j-i)
        #     ma = max(ma,ar)
        #     if height[i]<height[j]:
        #         i += 1
        #     else:
        #         j -= 1
        # return ma



        