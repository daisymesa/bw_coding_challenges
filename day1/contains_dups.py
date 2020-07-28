# https://leetcode.com/problems/contains-duplicate/

"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_dict = {}

        for num in nums:
            if num in nums_dict:
                return True
            else:
                nums_dict[num] = 1

        return False


test1 = Solution()
print(test1.containsDuplicate([1, 2, 3, 1]))  # True

test2 = Solution()
print(test2.containsDuplicate([1, 2, 3, 4]))  # False

test3 = Solution()
print(test3.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # True
