class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if len(mat)==1: return mat[0]
        if len(mat[0])==1:
            return [x[0] for x in mat]
        result = []
        row = len(mat)
        col = len(mat[0])
        i=0
        j=0
        
        flag = False
        while row-1>i or col-1>j:
            if flag:
                while i<row and j>=0:
                    # print(mat[i][j])
                    result.append(mat[i][j])
                    j -= 1
                    i += 1
                j += 1
                i -= 1   
                
                if i+1<row and j==0:
                    i += 1
                else:
                    j += 1
                flag = False
            else:
                while j<col and i>=0:
                    # print(mat[i][j])
                    result.append(mat[i][j])
                    i -= 1
                    j += 1
                i += 1
                j -= 1
                if j+1<col and i==0:
                    j += 1
                else:
                    i += 1
                flag = True

        result.append(mat[i][j])
        return result
                    