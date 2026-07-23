class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        #Split s into alternating runs of identical characters
        runs = []
        for ch in s:
            if runs and runs[-1][0] == ch:
                runs[-1][1] += 1
            else:
                runs.append([ch, 1])

        Z = []               # lengths of all '0' blocks
        interior_ones = []   # tuples: (length_of_1_block, index_of_left_zero_block)
        total_ones = 0

        #  interior '1' blocks and build Z
        for i, (char, length) in enumerate(runs):
            if char == '1':
                total_ones += length
                # An interior '1' block must have a '0' before and after in the runs list
                if 0 < i < len(runs) - 1:
                    left_idx = len(Z) - 1   # the '0' block immediately before
                    interior_ones.append((length, left_idx))
            else:  # char == '0'
                Z.append(length)

        # If no interior '1' block exists, no trade is possible
        if not interior_ones:
            return total_ones

        m = len(Z)
        #Prefix and suffix maximums of Z
        pref = [0] * m
        suff = [0] * m
        pref[0] = Z[0]
        for i in range(1, m):
            pref[i] = max(pref[i - 1], Z[i])
        suff[-1] = Z[-1]
        for i in range(m - 2, -1, -1):
            suff[i] = max(suff[i + 1], Z[i])

        max_gain = 0

        # Evaluate each interior '1' block
        for A, left_idx in interior_ones:
            right_idx = left_idx + 1

            # flip the merged zero block
            gain_merged = Z[left_idx] + Z[right_idx]

            # flip the best zero block not adjacent to this '1' block
            best_other = 0
            if left_idx > 0:
                best_other = max(best_other, pref[left_idx - 1])
            if right_idx < m - 1:
                best_other = max(best_other, suff[right_idx + 1])
            gain_separate = best_other - A

            max_gain = max(max_gain, gain_merged, gain_separate)

        # Final answer = original ones + maximum gain (never negative because we can skip trade)
        return total_ones + max_gain