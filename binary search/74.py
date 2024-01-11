class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bs(arr, target):
            left = 0
            right = len(arr)
            while left <= right:
                middle = (left + right) // 2
                if arr[middle] == target:
                    return True
                elif arr[middle] < target:
                    left = middle + 1
                else:
                    right = middle - 1

            return False
        
        
        left = 0
        right = len(matrix) - 1
        while left <= right:
            middle = (left + right) // 2
            if target >= matrix[middle][0] and target <= matrix[middle][-1]:
                return bs(matrix[middle],target)
            elif target < matrix[middle][0]:
                right = middle - 1

            else:
                left = middle + 1