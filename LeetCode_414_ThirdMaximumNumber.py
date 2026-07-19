class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique = []
        for i in nums:
            if i not in unique:
                unique.append(i)
        unique.sort()
        if len(unique) >= 3:
            return unique[-3]
        else:
            return unique[-1]
