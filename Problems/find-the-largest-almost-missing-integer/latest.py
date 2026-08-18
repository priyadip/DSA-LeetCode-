class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        if k == 1:
            return max((x for x in nums if c[x] == 1), default=-1)

        elif k == len(nums):
            return max(nums)
        else:
          
            return max( (x for x in (nums[0], nums[-1]) if c[x] == 1), default=-1)



        



        