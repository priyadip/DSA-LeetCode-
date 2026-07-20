class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        M = max(nums)
        freq = [0] * (M + 1)
        for x in nums:
            freq[x] += 1

        # cnt[g] will finally become: pairs with gcd == g (exact)
        cnt = [0] * (M + 1)
        # Step 1: For each g, count numbers that are multiples of g,
        #          then compute pairs with gcd multiple of g
        for g in range(1, M + 1):
            s = 0
            for m in range(g, M + 1, g):
                s += freq[m]
            cnt[g] = s * (s - 1) // 2

        # Step 2: Inclusion–exclusion to get exact gcd counts (in‑place)
        for g in range(M, 0, -1):
            val = cnt[g]
            for m in range(g * 2, M + 1, g):
                val -= cnt[m]
            cnt[g] = val

        # Step 3: Prefix sums to obtain cumulative counts (in‑place)
        for g in range(2, M + 1):
            cnt[g] += cnt[g - 1]
        # cnt[0] remains 0; cnt[g] now = number of pairs with gcd <= g

        # Step 4: Answer each query with a fast C-level binary search
        return [bisect.bisect_right(cnt, q) for q in queries]