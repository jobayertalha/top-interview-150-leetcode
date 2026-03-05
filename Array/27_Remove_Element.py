# 27. Remove Element
# Difficulty: Easy
# Topic: Array, Two Pointers
# LeetCode: https://leetcode.com/problems/remove-element/

"""
Problem
Remove all occurrences of a given value (val) in the array in-place.

Definition
Modify the array so that elements equal to val are removed.
Return the number of remaining elements.

Idea
Use two pointers:
- i → scans every element in the array
- k → keeps track of the position where the next valid element should go

Approach
1. Traverse the array with pointer i.
2. If nums[i] is NOT equal to val:
   place it at nums[k].
3. Move k forward.
4. Continue until the end.

After the loop, the first k elements contain the valid values.

Example
nums = [3,2,2,3], val = 3
Result → [2,2]

Time Complexity
O(n)

Space Complexity
O(1)
"""

class Solution(object):
    def removeElement(self, nums, val):

        k = 0

        for i in range(len(nums)):

            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k
