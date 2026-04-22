class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1
    
        while left <= right:
            mid = (left + right) // 2
            if max(matrix[mid]) < target:
                left = mid + 1
            elif min(matrix[mid]) > target:
                right = mid - 1
            else:
                break

        
        left2d, right2d = 0, len(matrix[0]) - 1
        while left2d <= right2d:
            point = (left2d + right2d) // 2
            print(matrix[mid][point])
            if matrix[mid][point] < target:
                
                left2d = point + 1
            elif matrix[mid][point] > target:
                right2d = point - 1
            else:
                return True

        return False


