class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        n=len(matrix)
        for row in range(n):
            for column in range(row+1,n):
                matrix[row][column],matrix[column][row]=matrix[column][row],matrix[row][column]
            
        for i in matrix:
            i.reverse()
        return matrix
        