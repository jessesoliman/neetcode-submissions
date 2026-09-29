class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        target_row = 0
        l, r = 0, len(matrix[0]) - 1
        rf, rl = 0, len(matrix) - 1
        maxi = 0
        while rf <= rl and maxi < 10:
            maxi += 1
            rm = rf + ((rl - rf)//2)
            if matrix[rm][0] > target:
                rl = rm - 1
            elif matrix[rm][-1] < target:
                rf = rm + 1
            else:
                while l <= r:
                    m = l + ((r - l) // 2)
                    if matrix[rm][m] > target:
                        r = m - 1
                    elif matrix[rm][m] < target:
                        l = m + 1
                    else:
                        return True
        return False
        