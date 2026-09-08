class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        positions = [[] for _ in range(26)]

        # Store positions of every character in s
        for i, ch in enumerate(s):
            positions[ord(ch) - ord('a')].append(i)

        ans = 0

        for word in words:
            prev = -1

            for ch in word:
                arr = positions[ord(ch) - ord('a')]

                # Find first position > prev
                idx = bisect_right(arr, prev)

                if idx == len(arr):
                    break

                prev = arr[idx]
            else:
                ans += 1

        return ans