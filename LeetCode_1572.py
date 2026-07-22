class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n=len(mat)
        m=len(mat[0])
        sum=0
        for i in range(n):
            for j in range(m):
              if i==j or i+j==m-1:
                sum+=mat[i][j]
        return sum
