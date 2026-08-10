class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        leftarridx = 0
        rightarridx = len(matrix) - 1
        
        while leftarridx <= rightarridx:
            middlearridx = leftarridx + ((rightarridx-leftarridx) // 2)
            left = 0
            right = len(matrix[middlearridx]) - 1
            
            while left <= right:
                middle = left + ((right-left) // 2)

                if matrix[middlearridx][middle] == target:
                    return True
                elif matrix[middlearridx][middle] > target:
                    right = middle - 1
                else:
                    left = middle + 1

            if left == 0:
                rightarridx = middlearridx - 1
            else:
                leftarridx = middlearridx + 1

        return False