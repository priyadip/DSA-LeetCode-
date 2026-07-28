class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = [0] * 26
        n = len(s)

        for ch in s:
            freq[ord(ch) - 97] += 1

        ans = [''] * n
        l, r = 0, n - 1
        mid = n // 2

        for i in range(26):
            c = chr(i + 97)

            # Place pairs
            while freq[i] >= 2:
                ans[l] = c
                ans[r] = c
                l += 1
                r -= 1
                freq[i] -= 2

            # Place the single remaining character (if any)
            if freq[i] == 1:
                ans[mid] = c

        return "".join(ans)





        # freq = [0]*26
        
        # for ch in s:
        #     freq[ord(ch)-97] += 1

        # left = []
        # mid = ''

        # for i in range(26):
        #     if freq[i]:
        #         left.append(chr(i+97)*(freq[i]//2))

        #         if freq[i] & 1:
        #             mid = chr(i+97)
        # left = ''.join(left)

        # return left+mid+left[::-1]


        