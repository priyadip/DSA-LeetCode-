
class Solution:
    def maxActiveSectionsAfterTrade(
        self, s: str, queries: List[List[int]]
    ) -> List[int]:

        t1 = s.count("1")
        n = len(s)

        hmz = []
        i = 0

        # store all zero blocks
        while i < n:

            if s[i] == '0':

                start = i

                while i < n and s[i] == '0':
                    i += 1

                hmz.append((start, i - 1))

            else:
                i += 1


        m = len(hmz)

        starts = [l for l, r in hmz]
        ends = [r for l, r in hmz]
        lengths = [r - l + 1 for l, r in hmz]


        # pair[i] =
        # length of zero block i
        # +
        # length of zero block i+1

        pair = []

        for i in range(m - 1):
            pair.append(lengths[i] + lengths[i + 1])


        # segment tree

        size = 1

        while size < len(pair):
            size *= 2


        seg = [0] * (2 * size)


        for i, x in enumerate(pair):
            seg[size + i] = x


        for i in range(size - 1, 0, -1):

            seg[i] = max(
                seg[2 * i],
                seg[2 * i + 1]
            )


        # maximum pair value
        # between left and right

        def range_max(left, right):

            if left > right:
                return 0


            left += size
            right += size

            result = 0


            while left <= right:

                if left % 2 == 1:

                    result = max(
                        result,
                        seg[left]
                    )

                    left += 1


                if right % 2 == 0:

                    result = max(
                        result,
                        seg[right]
                    )

                    right -= 1


                left //= 2
                right //= 2


            return result


        # zero block length
        # after cutting according to query [l, r]

        def cl(index, l, r):

            a, b = hmz[index]

            return max(
                0,
                min(b, r) - max(a, l) + 1
            )


        answer = []


        for l, r in queries:


            # first zero block
            # which intersects query

            first = bisect_left(
                ends,
                l
            )


            # last zero block
            # which intersects query

            last = bisect_right(
                starts,
                r
            ) - 1


            # less than two zero blocks
            # trade is impossible

            if first >= last:

                answer.append(t1)

                continue


            # first pair
            # first zero block may be cut by l

            best = (
                cl(first, l, r)
                +
                cl(first + 1, l, r)
            )


            # last pair
            # last zero block may be cut by r

            best = max(
                best,

                cl(last - 1, l, r)
                +
                cl(last, l, r)
            )


            # all completely internal pairs

            best = max(
                best,

                range_max(
                    first + 1,
                    last - 2
                )
            )


            answer.append(
                t1 + best
            )


        return answer