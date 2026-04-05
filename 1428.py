from typing import List


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: "BinaryMatrix") -> int:
        rows, cols = binaryMatrix.dimensions()
        leftmost_col = -1
        for row_idx in range(rows):
            left, right = 0, cols - 1 # change right to min of previous rows 1 index-1
            first_one_in_row = -1

            while left <= right:
                mid = (left + right) // 2
                if binaryMatrix.get(row_idx, mid) == 1:
                    first_one_in_row = mid
                    right = mid - 1
                else:
                    left = mid + 1

            if first_one_in_row != -1:
                if leftmost_col == -1:
                    leftmost_col = first_one_in_row
                else:
                    leftmost_col = min(leftmost_col, first_one_in_row)

        return leftmost_col
