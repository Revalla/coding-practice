class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        l=[]
        n=len(grid)
        m=len(grid[0])
        for i in range(n):
            for j in range(m):
                l.append(grid[i][j])
        for i in range(k):
            elem=l.pop()
            l.insert(0,elem)
        idx=0
        for i in range(n):
            for j in range(m):
                grid[i][j]=l[idx]
                idx+=1
        return grid
