class Solution:
    MAX = 10 ** 6 + 1
    def smallestPalindrome(self, s: str, k: int) -> str:
        cnt = Counter(s)
        half = [0] * 26
        mid = ""

        for ch, f in cnt.items():
            if f & 1:
                mid = ch
            half[ord(ch) - 97] = f // 2

        if self.count_perm(half) < k:
            return ""

        left = []

        while sum(half):
            for c in range(26):
                if half[c] == 0:
                    continue
                half[c] -= 1
                ways = self.count_perm(half)
                if ways >= k:
                    left.append(chr(c + 97))
                    break
                k -= ways
                half[c] += 1

        left = "".join(left)
        return left + mid + left[::-1]

    def count_perm(self, cnt):
        total = sum(cnt)
        res = 1

        for f in cnt:
            if f == 0:
                continue
            res *= self.nCk(total, f)
            if res >= self.MAX:
                return self.MAX
            total -= f
        return res

    def nCk(self, n, k):
        k = min(k, n - k)
        ans = 1
        for i in range(1, k + 1):
            ans = ans * (n - i + 1) // i
            if ans >= self.MAX:
                return self.MAX

        return ans