class Solution:
    def sumAndMultiply(self,n:int)->int:
        if n==0:
            return 0
        summ=0
        x=0
        place=1
        while n>0:
            dig=n%10
            if dig!=0:
                summ+=dig
                x+=dig*place
                place*=10
            n=n//10
        return x*summ
