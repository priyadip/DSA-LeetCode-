class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums = sorted(set(nums))
        j = 0
        ans = 0
        for num in nums:
            if num%k == 0:
                j += 1
                print(j)
                print(num/k)
                if num/k != j:
                    ans = j*k
                    print(ans)
                    break
        return ans or k*(j+1)
 

        