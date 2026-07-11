class Solution:
    def findIntegers(self, n: int) -> int:
        # f[i] = count of valid binary strings of length i
        f = [1, 2]
        for _ in range(30):
            f.append(f[-1] + f[-2])
        
        ans = 0
        prev_bit = 0
        for i in range(30, -1, -1):
            if (n >> i) & 1:
                ans += f[i]            # place 0 here, free lower i bits
                if prev_bit == 1:      # "11" → n itself invalid, stop
                    return ans
                prev_bit = 1
            else:
                prev_bit = 0
        
        return ans + 1                 # +1 for n itself