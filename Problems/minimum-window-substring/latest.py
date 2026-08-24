class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        def index(ch):
            c = ord(ch)
            return c - 97 if c >= 97 else c - 65 + 26

        need = [0] * 52

        # Count characters required from t
        for ch in t:
            need[index(ch)] += 1
            
        left = 0
        required = len(t)
        best_start = 0
        best_len = float("inf")

        for right, ch in enumerate(s):
            idx = index(ch)

            # This character was needed
            if need[idx] > 0:
                required -= 1

            # Add character to window
            need[idx] -= 1

            # Try shrinking the window
            while required == 0:
                window_len = right - left + 1

                if window_len < best_len:
                    best_len = window_len
                    best_start = left

                # Remove s[left]
                left_idx = index(s[left])
                need[left_idx] += 1

                # We removed a required character
                if need[left_idx] > 0:
                    required += 1

                left += 1

        if best_len == float("inf"):
            return ""

        return s[best_start:best_start + best_len]


        