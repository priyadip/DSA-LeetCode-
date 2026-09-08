class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        buckets = defaultdict(list)

        for word in words:
            buckets[word[0]].append((word, 0))

        ans = 0

        for ch in s:
            current = buckets[ch]
            buckets[ch] = []

            for word, i in current:
                i += 1

                if i == len(word):
                    ans += 1
                else:
                    buckets[word[i]].append((word, i))

        return ans