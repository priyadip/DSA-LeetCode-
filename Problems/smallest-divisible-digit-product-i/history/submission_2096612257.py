class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        def pd(m):
            pr = 1
            while m > 0:
                d = m%10
                pr *= d
                m //= 10
            return pr

        while pd(n) %t != 0:
            n += 1
        return n

        