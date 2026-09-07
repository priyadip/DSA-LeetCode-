class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        i = 0
        j = len(s) - 1
        vowels = 'aeiouAEIOU'
        l = r = -1
        while i < j:
            if s[i] in vowels:
                l = i
            else:
                i += 1

            if s[j] in vowels:
                r = j
            else:
                j -= 1
            if l != -1 and r != -1:
                s[l], s[r] = s[r], s[l]
                i += 1
                j -= 1
                l = r = -1
        return ''.join(s)



            


        