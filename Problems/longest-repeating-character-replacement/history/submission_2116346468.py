class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        c = {}
        mf = 0
        answer = 0

        for r in range(len(s)):
            c[s[r]] = c.get(s[r], 0) + 1
            mf = max(mf, c[s[r]])

            while (r - l + 1) - mf > k:
                c[s[l]] -= 1
                l += 1
                
            answer = max(answer, r - l + 1)

        return answer
        