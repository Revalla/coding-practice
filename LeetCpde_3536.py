class Solution:
    def maxProduct(self, n: int) -> int:
        l=[]
        while n>0:
            l.append(n%10)
            n=n//10
        max1=max(l)
        l.remove(max1)
        max2=max(l)
        return max1*max2
