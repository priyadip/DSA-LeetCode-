class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        save = defaultdict(list)
        # for word in strs:
        #     cn = [0]*26
        #     for ch in word:
        #         cn[ord(ch) - ord('a')] += 1
        #     save[tuple(cn)].append(word)
        # return list(save.values())
        for word in strs:
            key = ''.join(sorted(word))
            save[key].append(word)
        return list(save.values())


























        # mp = defaultdict(list)

        # for word in strs:
        #     cnt = [0] * 26

        #     for c in word:
        #         cnt[ord(c) - ord('a')] += 1

        #     mp[tuple(cnt)].append(word)

        # return list(mp.values())

        # mp = defaultdict(list)

        # for word in strs:
        #     key = "".join(sorted(word))
        #     mp[key].append(word)

        # return list(mp.values())



























        