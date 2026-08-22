class Solution:
    def checkDivisibility(self, n: int) -> bool:
        su, pr = 0, 1
        m =n
        while n:
            d = n%10
            su += d
            pr *= d
            n //= 10
        return ((m%(su+pr)) == 0)
        