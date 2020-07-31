# https://leetcode.com/problems/two-sum/

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # we can create a dict that stores the num as a key
        # the value can be the target - key
        # if any key matches up with any value, those are the two numbers we need to return in a list
        # we need to return the INDEX for each of those two numbers

        nums_dict = {}

        for num in nums:
            nums_dict[num] = target - num

        for key, value in nums_dict.items():
            if value in nums:
                return([nums.index(key), nums.index(value)])

        # result.append(nums.index(num1))
        # result.append(nums.index(num2))
        # return result

        # return([nums.index(num1), nums.index(num2)])


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))  # [0, 1]
