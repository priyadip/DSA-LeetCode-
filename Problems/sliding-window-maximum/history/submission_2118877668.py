class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)
        q = [0] * n
        head = 0
        tail = 0
        result = []

        for i in range(n):

            # Remove expired indices
            while head < tail and q[head] <= i - k:
                head += 1

            # Remove smaller values
            while head < tail and nums[q[tail - 1]] <= nums[i]:
                tail -= 1

            q[tail] = i
            tail += 1

            if i >= k - 1:
                result.append(nums[q[head]])

        return result

            