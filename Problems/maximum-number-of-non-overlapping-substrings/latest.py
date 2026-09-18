class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = [len(s)] * 26
        last = [-1] * 26

        for i, c in enumerate(s):
            x = ord(c) - 97
            first[x] = min(first[x], i)
            last[x] = i

        a = []
        for c in range(26):
            l, r = first[c], last[c]
            if r < 0:
                continue

            i = l
            while i <= r:
                x = ord(s[i]) - 97
                if first[x] < l:
                    break
                r = max(r, last[x])
                i += 1
            else:
                a.append((r, l))

        a.sort()
        ans, end = [], -1

        for r, l in a:
            if l > end:
                ans.append(s[l:r + 1])
                end = r

        return ans