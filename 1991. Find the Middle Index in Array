# Problem 1991. Find the Middle Index in Array
# link: https://leetcode.com/problems/find-the-middle-index-in-array/
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        key=[]
        for i in range(0,len(nums)+1):
            if nums[i] not in key:
                key.append(nums[i])
            else:
                return nums[i]
