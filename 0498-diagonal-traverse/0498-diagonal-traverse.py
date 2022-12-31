class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        result = []
        row,col = len(mat),len(mat[0])
        i=j=0    
        flag = False
        
        while row-1>i or col-1>j:
            if flag:
                #move downward
                while i<row and j>=0:
                    # print(mat[i][j])
                    result.append(mat[i][j])
                    j -= 1
                    i += 1   
                
                if j<0 and i<row:
                    j = 0
                else:
                    j += 2
                    i -= 1
                    
            else:
                #move upward
                while j<col and i>=0:
                    # print(mat[i][j])
                    result.append(mat[i][j])
                    i -= 1
                    j += 1
                if i<0 and j<col:
                    i = 0 
                else:
                    i += 2
                    j -= 1
            flag = not flag

        result.append(mat[i][j])
        return result
                    