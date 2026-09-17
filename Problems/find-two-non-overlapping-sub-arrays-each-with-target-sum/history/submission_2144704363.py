class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        INF = n + 1

        BASE = max(1001, n + 2)

        left = 0
        curr_sum = 0
        ans = INF

        for right in range(n):
            if arr[right] >= BASE:
                x = arr[right] // BASE
            else:
                x = arr[right]
            curr_sum += x

            while curr_sum > target:
                if arr[left] >= BASE:
                    value = arr[left] // BASE
                else:
                    value = arr[left]
                curr_sum -= value
                left += 1
            if right == 0:
                best = INF
            else:
                best = arr[right - 1] % BASE

            if curr_sum == target:
                length = right - left + 1
                if left > 0:
                    previous = arr[left - 1] % BASE
                    if previous != INF:
                        ans = min( ans, previous + length )
                best = min(best, length)

            arr[right] = x * BASE + best
        return -1 if ans == INF else ans