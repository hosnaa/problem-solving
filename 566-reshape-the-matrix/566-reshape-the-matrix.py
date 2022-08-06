class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        import numpy as np
        try:
            m = len(mat[0])
        except:
            m = 1
        n = len(mat)
        # To flatten into 1D list
        mat_1 = []
        for i in range(n): # thus, range works even if 1 element; also; 1D shaped arrays already have 2 len(1, #)
            for j in range(m):
                mat_1.append(mat[i][j])        

        if r*c != m*n:
            return mat
        else:
            mat2 = np.zeros((r, c), dtype=int)
            x = 0
            # access each element in flattened matrix and add to the exact place
            for i in range(r):
                for j in range(c): 
                    mat2[i][j] = int(mat_1[x])
                    x += 1

        return mat2