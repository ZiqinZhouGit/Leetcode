class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix)==0:
            return
        
        indicators_row = [False for i in range(len(matrix))]
        indicators_col = [False for j in range(len(matrix[0]))]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    indicators_row[i] = True
                    indicators_col[j] = True
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if indicators_row[i] or indicators_col[j]:
                    matrix[i][j] = 0
