# https://leetcode.com/problems/running-sum-of-1d-array/
# Solution 1 - Faster
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_num = [nums[0]]
        temp_sum = nums[0]
        for i in range(0, len(nums)-1):
            temp_sum += nums[i+1]
            running_num.append(temp_sum)
        return running_num


# Solution 2
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_num = [nums[0]]
        for i in range(1, len(nums)):
            running_num.append(nums[i]+running_num[i-1])
        return running_num

# Solution 3 - modify the given list
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_num = [nums[0]]
        temp_sum = nums[0]
        for i in range(0, len(nums)-1):
            temp_sum += nums[i+1]
            running_num.append(temp_sum)
        return running_num