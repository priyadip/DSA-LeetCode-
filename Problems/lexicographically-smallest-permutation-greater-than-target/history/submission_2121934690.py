class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - 97] += 1

        n = len(s)
        i = 0

        # Match target as far as possible.
        while i < n:
            x = ord(target[i]) - 97
            if cnt[x] == 0:
                break
            cnt[x] -= 1
            i += 1

        # Try to make the first unmatched position larger.
        if i < n:
            x = ord(target[i]) - 97

            for y in range(x + 1, 26):
                if cnt[y]:
                    cnt[y] -= 1
                    suffix = ''.join(
                        chr(k + 97) * cnt[k] for k in range(26)
                    )
                    return target[:i] + chr(y + 97) + suffix

        # No larger character at i.
        # Backtrack and increase an earlier position.
        for j in range(i - 1, -1, -1):
            x = ord(target[j]) - 97
            cnt[x] += 1

            for y in range(x + 1, 26):
                if cnt[y]:
                    cnt[y] -= 1
                    suffix = ''.join(
                        chr(k + 97) * cnt[k] for k in range(26)
                    )
                    return target[:j] + chr(y + 97) + suffix

        return ""