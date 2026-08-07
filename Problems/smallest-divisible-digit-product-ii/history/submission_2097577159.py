class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        #Factor t 
        temp = t
        max2 = max3 = max5 = max7 = 0
        while temp % 2 == 0:
            max2 += 1
            temp //= 2
        while temp % 3 == 0:
            max3 += 1
            temp //= 3
        while temp % 5 == 0:
            max5 += 1
            temp //= 5
        while temp % 7 == 0:
            max7 += 1
            temp //= 7
        if temp != 1:
            return "-1"

        # Precompute DP for all needed prime
        size2 = max2 + 1
        size3 = max3 + 1
        size5 = max5 + 1
        size7 = max7 + 1
        stride2 = size3 * size5 * size7
        stride3 = size5 * size7
        stride5 = size7
        stride7 = 1
        N = size2 * size3 * size5 * size7

        dig_factors = [
            (2, (1, 0, 0, 0)),
            (3, (0, 1, 0, 0)),
            (4, (2, 0, 0, 0)),
            (5, (0, 0, 1, 0)),
            (6, (1, 1, 0, 0)),
            (7, (0, 0, 0, 1)),
            (8, (3, 0, 0, 0)),
            (9, (0, 2, 0, 0))
        ]
        dig_strs = ['2', '3', '4', '5', '6', '7', '8', '9']
        dig_to_idx = {d: i for i, d in enumerate([2, 3, 4, 5, 6, 7, 8, 9])}

        min_digits = [-1] * N
        best_str = [None] * N

        start_counts = (0, 0, 0, 0, 0, 0, 0, 0)
        queue = [(0, 0, 0, 0, start_counts)]
        min_digits[0] = 0
        best_str[0] = ""
        level = 0

        while queue:
            next_cand = {}
            for c2, c3, c5, c7, cnts in queue:
                for d, (a2, a3, a5, a7) in dig_factors:
                    n2 = c2 + a2
                    if n2 > max2: n2 = max2
                    n3 = c3 + a3
                    if n3 > max3: n3 = max3
                    n5 = c5 + a5
                    if n5 > max5: n5 = max5
                    n7 = c7 + a7
                    if n7 > max7: n7 = max7
                    nidx = n2 * stride2 + n3 * stride3 + n5 * stride5 + n7
                    if min_digits[nidx] != -1:
                        continue
                    d_idx = dig_to_idx[d]
                    new_cnts = list(cnts)
                    new_cnts[d_idx] += 1
                    new_cnts = tuple(new_cnts)

                    if nidx not in next_cand:
                        next_cand[nidx] = (n2, n3, n5, n7, new_cnts)
                    else:
                        exist = next_cand[nidx][4]
                        better = False
                        for i in range(8):
                            if new_cnts[i] != exist[i]:
                                if new_cnts[i] > exist[i]:
                                    better = True
                                break
                        if better:
                            next_cand[nidx] = (n2, n3, n5, n7, new_cnts)

            if not next_cand:
                break
            next_queue = []
            for nidx, (n2, n3, n5, n7, ncnts) in next_cand.items():
                min_digits[nidx] = level + 1
                s = ''
                for d_idx, cnt in enumerate(ncnts):
                    if cnt:
                        s += dig_strs[d_idx] * cnt
                best_str[nidx] = s
                next_queue.append((n2, n3, n5, n7, ncnts))
            queue = next_queue
            level += 1

        def encode(c2, c3, c5, c7):
            return c2 * stride2 + c3 * stride3 + c5 * stride5 + c7

        #  Digit factor 
        dig_factor_map = {
            1: (0, 0, 0, 0),
            2: (1, 0, 0, 0),
            3: (0, 1, 0, 0),
            4: (2, 0, 0, 0),
            5: (0, 0, 1, 0),
            6: (1, 1, 0, 0),
            7: (0, 0, 0, 1),
            8: (3, 0, 0, 0),
            9: (0, 2, 0, 0)
        }

        L = len(num)

        
        pref2 = [0] * (L + 1)
        pref3 = [0] * (L + 1)
        pref5 = [0] * (L + 1)
        pref7 = [0] * (L + 1)
        valid_pref = [True] * (L + 1)

        r2 = r3 = r5 = r7 = 0
        v = True
        for i, ch in enumerate(num):
            if ch == '0':
                v = False
            else:
                f = dig_factor_map[int(ch)]
                r2 += f[0]
                r3 += f[1]
                r5 += f[2]
                r7 += f[3]
            pref2[i + 1] = r2
            pref3[i + 1] = r3
            pref5[i + 1] = r5
            pref7[i + 1] = r7
            valid_pref[i + 1] = v

    
        if valid_pref[L] and pref2[L] >= max2 and pref3[L] >= max3 and pref5[L] >= max5 and pref7[L] >= max7:
            return num

    
        for i in range(L - 1, -1, -1):
            if not valid_pref[i]:
                continue
            p2, p3, p5, p7 = pref2[i], pref3[i], pref5[i], pref7[i]
            curr_d = int(num[i])
            for d in range(curr_d + 1, 10):
                f = dig_factor_map[d]
                need2 = max2 - p2 - f[0]
                if need2 < 0: need2 = 0
                need3 = max3 - p3 - f[1]
                if need3 < 0: need3 = 0
                need5 = max5 - p5 - f[2]
                if need5 < 0: need5 = 0
                need7 = max7 - p7 - f[3]
                if need7 < 0: need7 = 0
                nidx = encode(need2, need3, need5, need7)
                if min_digits[nidx] <= L - 1 - i:
                    rem = L - 1 - i
                    m = min_digits[nidx]
                    suffix = '1' * (rem - m) + best_str[nidx]
                    return num[:i] + str(d) + suffix

    
        total_need = encode(max2, max3, max5, max7)
        total_min = min_digits[total_need]
        ans_len = max(L + 1, total_min)
        return '1' * (ans_len - total_min) + best_str[total_need]
