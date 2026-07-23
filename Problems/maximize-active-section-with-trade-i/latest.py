class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        # split into runs of identical characters
        runs = []
        for ch in s:
            if runs and runs[-1][0] == ch:
                runs[-1][1] += 1
            else:
                runs.append([ch, 1])

        Z = []                # lengths of all '0' runs
        interior = []         # (length_A, left_zero_index)
        total_ones = 0

        for i, (ch, ln) in enumerate(runs):
            if ch == '1':
                total_ones += ln
               
                if 0 < i < len(runs) - 1:
                    left_idx = len(Z) - 1   # previous '0' is the last element in Z
                    interior.append((ln, left_idx))
            else:
                Z.append(ln)

        if not interior:
            return total_ones

        #  top three zero blocks by length (value, index)
        top3 = [(0, -1), (0, -1), (0, -1)]
        for idx, length in enumerate(Z):
            if length > top3[0][0]:
                top3 = [(length, idx), top3[0], top3[1]]
            elif length > top3[1][0]:
                top3 = [top3[0], (length, idx), top3[1]]
            elif length > top3[2][0]:
                top3[2] = (length, idx)

        max_gain = 0
        for A, left_idx in interior:
            right_idx = left_idx + 1
            #  flip the merged zero block
            gain_merged = Z[left_idx] + Z[right_idx]

            #  flip the best zero block elsewhere
            best_other = 0
            for ln, idx in top3:
                if idx != left_idx and idx != right_idx:
                    best_other = ln
                    break
            gain_sep = best_other - A

            max_gain = max(max_gain, gain_merged, gain_sep)

        return total_ones + max_gain