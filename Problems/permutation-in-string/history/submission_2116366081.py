class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = Counter(s1)
        window = Counter(s2[:len(s1)])

        if window == target:
            return True

        for right in range(len(s1), len(s2)):
            window[s2[right]] += 1

            left_char = s2[right - len(s1)]
            window[left_char] -= 1

            if window[left_char] == 0:
                del window[left_char]

            if window == target:
                return True

        return False