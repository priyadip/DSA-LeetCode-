class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:


        n = len(arr)

        INF = n + 1

        # arr[i] <= 1000
        # best value <= n
        # So BASE must be larger than both.
        BASE = max(1001, n + 2)

        left = 0
        curr_sum = 0
        ans = INF

        for right in range(n):

            # ----------------------------------
            # Recover original arr[right]
            # ----------------------------------
            if arr[right] >= BASE:
                x = arr[right] // BASE
            else:
                x = arr[right]

            curr_sum += x

            # ----------------------------------
            # Sliding window
            # ----------------------------------
            while curr_sum > target:

                if arr[left] >= BASE:
                    value = arr[left] // BASE
                else:
                    value = arr[left]

                curr_sum -= value
                left += 1

            # ----------------------------------
            # best = shortest valid subarray
            # found completely before 'right'
            # ----------------------------------
            if right == 0:
                best = INF
            else:
                best = arr[right - 1] % BASE

            # ----------------------------------
            # Current window [left ... right]
            # ----------------------------------
            if curr_sum == target:

                length = right - left + 1

                # Need a previous valid subarray
                # completely before 'left'
                if left > 0:

                    previous = arr[left - 1] % BASE

                    if previous != INF:
                        ans = min(
                            ans,
                            previous + length
                        )

                # Current subarray can be the best
                # one for future subarrays.
                best = min(best, length)

            # ----------------------------------
            # Store two things in arr[right]:
            #
            # original value
            # +
            # best prefix information
            #
            # encoded = original * BASE + best
            # ----------------------------------
            arr[right] = x * BASE + best

        return -1 if ans == INF else ans