class Solution:
    def isValid(self, mat):
        # code here
        r = [[0 for i in range(9)]for i in range(9)]
        c = [[0 for i in range(9)]for i in range(9)]
        s = [[[0 for i in range(9)]for i in range(3)]for i in range(3)]
        
        number = 0 
        for i in range(0,9):
            for j in range(0,9):
                if(mat[i][j]>0 and mat[i][j]<=9):
                    number = mat[i][j]-1
                    if r[i][number] !=0 :
                        return 0
                    r[i][number]=1;
                    if c[j][number]!=0:
                        return 0
                    c[j][number]=1
                    if s[i//3][j//3][number]!=0:
                        return 0
                    s[i//3][j//3][number]=1
        
        return 1
