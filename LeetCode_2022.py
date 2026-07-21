class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original)!=m*n:
            return []
        ans=[]
        k=0
        for i in range(m):
            row=[]
            for j in range(n):
                row.append(original[k])
                k+=1
            ans.append(row)
        return ans
