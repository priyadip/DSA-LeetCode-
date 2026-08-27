class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - 97] += 1

        n = len(s)
        i = 0

        while i < n:
            x = ord(target[i]) - 97
            if not cnt[x]:
                break
            cnt[x] -= 1
            i += 1

        # Try making the first unmatched position larger
        if i < n:
            x = ord(target[i]) - 97
            for y in range(x + 1, 26):
                if cnt[y]:
                    cnt[y] -= 1
                    return target[:i] + chr(y + 97) + \
                           ''.join(chr(k + 97) * cnt[k] for k in range(26))

        # Otherwise backtrack to find the rightmost position
        # that can be increased.
        for j in range(i - 1, -1, -1):
            x = ord(target[j]) - 97
            cnt[x] += 1

            for y in range(x + 1, 26):
                if cnt[y]:
                    cnt[y] -= 1
                    return target[:j] + chr(y + 97) + \
                           ''.join(chr(k + 97) * cnt[k] for k in range(26))

        return ""
        