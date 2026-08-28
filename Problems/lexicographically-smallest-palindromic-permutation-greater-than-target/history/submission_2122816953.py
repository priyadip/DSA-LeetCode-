
class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        cnt = Counter(s)

        # A palindrome can have at most one odd count.
        if sum(v % 2 for v in cnt.values()) > 1:
            return ""

        half_cnt = Counter({c: v // 2 for c, v in cnt.items()})
        m = n // 2
        t = target[:m]
        mid = next((c for c in cnt if cnt[c] % 2), "")

        def make(left):
            return left + mid + left[::-1]

        # Check whether target's first half can be formed exactly.
        rem = half_cnt.copy()
        possible = True

        for c in t:
            if rem[c] == 0:
                possible = False
                break
            rem[c] -= 1

        # If the left half equals target's left half,
        # the middle/right side may still make the palindrome greater.
        if possible:
            ans = make(t)
            if ans > target:
                return ans

        # Find the smallest left half strictly greater than t.
        #
        # Change the rightmost possible position and fill the suffix
        # with the smallest available characters.
        for i in range(m - 1, -1, -1):
            prefix = t[:i]
            rem = half_cnt.copy()

            # Consume the prefix.
            ok = True
            for c in prefix:
                if rem[c] == 0:
                    ok = False
                    break
                rem[c] -= 1

            if not ok:
                continue

            # Put the smallest character > t[i].
            for c in sorted(rem):
                if c > t[i] and rem[c] > 0:
                    rem[c] -= 1

                    left = prefix + c
                    left += "".join(
                        x * rem[x] for x in sorted(rem)
                    )

                    return make(left)

        return ""

