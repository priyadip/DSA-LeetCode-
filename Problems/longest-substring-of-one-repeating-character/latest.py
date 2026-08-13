
class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:

        n = len(s)
        size = 4 * n

        # lc[node]   = leftmost character
        # rc[node]   = rightmost character
        # pre[node]  = longest equal-character prefix
        # suf[node]  = longest equal-character suffix
        # best[node] = longest equal-character substring
        lc = [0] * size
        rc = [0] * size
        pre = [0] * size
        suf = [0] * size
        best = [0] * size

        # Convert characters to integers
        a = [ord(c) - 97 for c in s]

        def build(node, l, r):
            if l == r:
                x = a[l]
                lc[node] = rc[node] = x
                pre[node] = suf[node] = best[node] = 1
                return

            mid = (l + r) >> 1
            left = node << 1
            right = left | 1

            build(left, l, mid)
            build(right, mid + 1, r)

            lc[node] = lc[left]
            rc[node] = rc[right]

            left_len = mid - l + 1
            right_len = r - mid

            # Prefix
            p = pre[left]

            # Entire left segment is uniform
            # AND boundary characters are equal
            if p == left_len and rc[left] == lc[right]:
                p += pre[right]

            pre[node] = p

            # Suffix
            su = suf[right]

            # Entire right segment is uniform
            # AND boundary characters are equal
            if su == right_len and rc[left] == lc[right]:
                su += suf[left]

            suf[node] = su

            # Best
            b = best[left]

            if best[right] > b:
                b = best[right]

            if rc[left] == lc[right]:
                cross = suf[left] + pre[right]
                if cross > b:
                    b = cross

            best[node] = b

        def update(node, l, r, idx, ch):
            if l == r:
                lc[node] = rc[node] = ch
                pre[node] = suf[node] = best[node] = 1
                return

            mid = (l + r) >> 1
            left = node << 1
            right = left | 1

            if idx <= mid:
                update(left, l, mid, idx, ch)
            else:
                update(right, mid + 1, r, idx, ch)

            lc[node] = lc[left]
            rc[node] = rc[right]

            left_len = mid - l + 1
            right_len = r - mid

            # Prefix
            p = pre[left]

            if p == left_len and rc[left] == lc[right]:
                p += pre[right]

            pre[node] = p

            # Suffix
            su = suf[right]

            if su == right_len and rc[left] == lc[right]:
                su += suf[left]

            suf[node] = su

            # Best
            b = best[left]

            if best[right] > b:
                b = best[right]

            if rc[left] == lc[right]:
                cross = suf[left] + pre[right]
                if cross > b:
                    b = cross

            best[node] = b

        build(1, 0, n - 1)

        k = len(queryIndices)
        ans = [0] * k

        for i in range(k):
            idx = queryIndices[i]
            ch = ord(queryCharacters[i]) - 97

            update(1, 0, n - 1, idx, ch)
            ans[i] = best[1]

        return ans