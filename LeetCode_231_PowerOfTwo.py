class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        count=0
        while n:
            count+=n&1
            n=n>>1
        if count==1:
            return True
        else:
            return False    
