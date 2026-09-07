class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        i = 0
        ans = 0

        while i < n:
            ch = chars[i]
            j = i

            # Count this group
            while i < n and chars[i] == ch:
                i += 1

            count = i - j

            # Write character
            chars[ans] = ch
            ans += 1

            # Write count if > 1
            if count > 1:
                for digit in str(count):
                    chars[ans] = digit
                    ans += 1

        return ans