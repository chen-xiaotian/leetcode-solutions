# Problem 35. Search Insert Position
# Link: https://leetcode.com/problems/search-insert-position/
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if sum(nums[1:])==0:
            return 0
        i=0
        while i < len(nums):
            if sum(nums[0:i])==sum(nums[i+1:]):
                return i
            else:
                i+=1
        if sum(nums[:-1])==0:
            return len(nums)-1
        return -1
