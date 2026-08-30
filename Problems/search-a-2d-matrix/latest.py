class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        l = 0
        r  = rows*cols - 1

        while l <= r:
            mid  = l +(r-l)//2
            ri = mid // cols
            ci = mid % cols

            if matrix[ri][ci] == target:
                return True
            elif matrix[ri][ci] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
        