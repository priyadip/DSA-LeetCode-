class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:

        present = {num // k for num in nums if num % k == 0}

        i = 1
        while i in present:
            i += 1

        return i * k
 

        