class Solution:
    def reverseWords(self, s: str) -> str:
        wordlist = s.split()

        return ' '.join(wordlist[::-1])




        