class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix) - 1

        while left < right:          

            for i in range(right - left):
                top, bottom = left, right

                #save the topleft in temp
                temp = matrix[top][left + i]

                #save bottomleft in topleft
                matrix[top][left + i] = matrix[bottom - i][left]

                #save bottomright in bottomleft
                matrix[bottom - i][left] = matrix[bottom][right - i]

                #save topright in bottomright
                matrix[bottom][right - i] = matrix[top + i][right]

                #save topleft in topright
                matrix[top + i][right] = temp

            left += 1
            right -= 1

#solution 2
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        matrix[:] = zip(*matrix[::-1])