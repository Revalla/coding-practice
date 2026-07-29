class Solution:
    def spiralOrder(self,matrix:List[List[int]])->List[int]:
        n=len(matrix)
        m=len(matrix[0])
        sr=0
        er=n-1
        sc=0
        ec=m-1
        l=[]
        while sr<=er and sc<=ec:
            for j in range(sc,ec+1):
                l.append(matrix[sr][j])
            for i in range(sr+1,er+1):
                l.append(matrix[i][ec])
            if sr<er:
                for j in range(ec-1,sc-1,-1):
                    l.append(matrix[er][j])
            if sc<ec:
                for i in range(er-1,sr,-1):
                    l.append(matrix[i][sc])
            sr+=1
            er-=1
            sc+=1
            ec-=1
        return l
