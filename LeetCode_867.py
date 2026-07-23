class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n=len(matrix)
        m=len(matrix[0])
        ans=[]
        for j in range(m):
          l=[0]*n
          ans.append(l)
        for i in range(n):
            for j in range(m):
                ans[j][i]=matrix[i][j]
        return ans
