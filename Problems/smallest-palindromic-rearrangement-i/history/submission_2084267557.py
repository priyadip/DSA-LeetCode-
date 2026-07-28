class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = [0]*26
        
        for ch in s:
            freq[ord(ch)-97] += 1

        left = []
        mid = ''

        for i in range(26):
            if freq[i]:
                left.append(chr(i+97)*(freq[i]//2))

                if freq[i] & 1:
                    mid = chr(i+97)
        left = ''.join(left)

        return left+mid+left[::-1]


        