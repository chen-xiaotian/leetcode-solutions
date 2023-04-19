# https://leetcode.com/problems/richest-customer-wealth/
# Solution 1
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0
        for i in range(0, len(accounts)):
            if richest < sum(accounts[i]):
                richest = sum(accounts[i])
        return richest

# Solution 2 -
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_total = 0
        for i in range(0, len(accounts)):
            curr_total = 0
            for j in range(0, len(accounts[i])):
                curr_total +=accounts[i][j]
            if max_total < curr_total:
                max_total = curr_total
        return max_total