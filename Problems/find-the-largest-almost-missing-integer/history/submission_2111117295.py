class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        if k == 1:
            s = [x for x in nums if c[x] == 1]
            if s:
                return max(s)
            else:
                return -1
        elif k == len(nums):
            return max(nums)
        else:
            if c[nums[0]] == 1 and c[nums[-1]] == 1:
                return max(nums[0], nums[-1])
            elif c[nums[0]] == 1:
                return nums[0]
            elif c[nums[-1]] == 1:
                return nums[-1]
            else:
                return -1



        



        