class Solution:
    def findGCD(self, nums: List[int]) -> int:
        small = nums[0]
        large = nums[0]
        for i in nums:
            if i < small:
                small = i
            if i > large:
                large = i
        ans = 1
        for i in range(1, small + 1):
            if small % i == 0 and large % i == 0:
                ans = i
        return ans
