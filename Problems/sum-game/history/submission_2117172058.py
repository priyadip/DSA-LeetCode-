class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        h = n // 2
        d = l = r = 0

        for i, ch in enumerate(num):
            if ch == '?':
                if i < h:
                    l += 1
                else:
                    r += 1
            elif i < h:
                d += int(ch)
            else:
                d -= int(ch)

        # Bob wins only when this condition holds
        return 2 * d != 9 * (r - l)
        