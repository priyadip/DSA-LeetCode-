class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = -1
        r = len(nums)
        c = 0
      
        while c < r:
            if nums[c] == 0:
                # Move 0 to the left section
                l += 1
                nums[l], nums[c] = nums[c], nums[l]
                # Move c forward since we know the swapped element is processed
                c += 1
            elif nums[c] == 2:
                # Move 2 to the right section
                r -= 1
                nums[r], nums[c] = nums[c], nums[r]
                # Don't increment c as the swapped element needs to be examined
            else:
                # Element is 1, leave it in the middle section
                c += 1


        