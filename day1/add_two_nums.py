# https://leetcode.com/problems/add-two-numbers/

"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def __init__(self):
        self.head = None

    def push(self, new_val):
        new_node = ListNode(new_val)
        new_node.next = self.head
        self.head = new_node

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # we need to add the 1st num in l1 with 1st num in l2
        # we need to then move to 2nd num in l1, 2nd num in l2
        # we need to account for any sums that are > 9, if yes have a way to add a 1 to the next calculation

        # poss. pointers:
        # l1_num
        # l2_num
        # carry (1, as needed)
        # result for each sum, which needs to become a node in new ll that will be returned
        # as we compute each result, we have to link that to the next node for our new LL

        # question:
        # can/what if nums have diff # of digits..ie 125 + 1250?
        # if so the 4th digit for num1 will be null, and should be treated as if it was a zero

        prev = None
        new_num_pointer = None
        carry_val = 0

        while (l1 is not None or l2 is not None):
            # initialize list 1 num as 0
            l1_num_val = 0
            # initialize list 2 num as 0
            l2_num_val = 0

            # if list 1 value is not None, reassign to its value
            if l1.val is not None:
                l1_num_val = l1.val

            # if list 2 value is not None, reassign to its value
            if l2.val is not None:
                l1_num_val = l2.val

            # add up the variables for the list 1 number + list 2 number + the value of carry_val
            num_sum = l1_num_val + l2_num_val + carry_val

            # the value of carry_val changes from 0 to 1 if the nums_sum is >= to 10
            if nums_sum >= 10:
                carry = 1

            # create new node for the nums sum
            new_num_pointer = Node(nums_sum)

            # # if no head, the head becomes our new node we just created
            # if self.head is None:
            #     self.head = new_num_pointer
            # # else, it becomes the next value
            # else:
            #     prev.next = new_num_pointer

            # prev = new_num_pointer


test = Solution()
print(Solution.addTwoNumbers([2, 4, 3], [5, 6, 4]))  # [7, 0, 8]
