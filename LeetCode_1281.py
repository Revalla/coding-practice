class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        summ=0
        pro=1
        while n>0:
            dig=n%10
            summ+=dig
            pro*=dig
            n=n//10
        return pro-summ
