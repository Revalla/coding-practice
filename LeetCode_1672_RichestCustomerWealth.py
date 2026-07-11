class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxx=0
        for customer in accounts:
            wealth=sum(customer)
            if wealth>maxx:
                maxx=wealth
        return maxx
