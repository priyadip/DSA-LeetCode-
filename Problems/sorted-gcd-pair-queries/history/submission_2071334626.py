class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        M = max(nums)
        
        # Step 1: frequency of each number
        freq = [0] * (M + 1)
        for x in nums:
            freq[x] += 1
            
        # Step 2: count multiples for each possible gcd g
        cnt = [0] * (M + 1)
        for g in range(1, M + 1):
            s = 0
            for multiple in range(g, M + 1, g):
                s += freq[multiple]
            cnt[g] = s
            
        # Step 3: total pairs where both numbers are multiples of g
        pairs_mult = [0] * (M + 1)
        for g in range(1, M + 1):
            c = cnt[g]
            pairs_mult[g] = c * (c - 1) // 2
            
        # Step 4: inclusion-exclusion to get exact number of pairs with gcd == g
        exact = [0] * (M + 1)
        for g in range(M, 0, -1):
            val = pairs_mult[g]
            multiple = g * 2
            while multiple <= M:
                val -= exact[multiple]
                multiple += g
            exact[g] = val
            
        # Step 5: prefix sums of exact counts
        cumulative = [0] * (M + 1)
        cum = 0
        for g in range(1, M + 1):
            cum += exact[g]
            cumulative[g] = cum
            
        # Step 6: answer each query by binary searching the smallest gcd with cumulative > q
        ans = []
        for q in queries:
            left, right = 1, M
            while left < right:
                mid = (left + right) // 2
                if cumulative[mid] > q:
                    right = mid
                else:
                    left = mid + 1
            ans.append(left)
            
        return ans
        