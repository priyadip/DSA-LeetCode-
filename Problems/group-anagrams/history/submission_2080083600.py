class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # mp = defaultdict(list)

        # for word in strs:
        #     cnt = [0] * 26

        #     for c in word:
        #         cnt[ord(c) - ord('a')] += 1

        #     mp[tuple(cnt)].append(word)

        # return list(mp.values())

        mp = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            mp[key].append(word)

        return list(mp.values())
        