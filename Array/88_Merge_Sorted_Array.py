# 88. Merge Sorted Array
# Difficulty: Easy
# Topic: Array, Two Pointers
# LeetCode: https://leetcode.com/problems/merge-sorted-array/

"""
Problem
Merge nums2 into nums1 as one sorted array.

Definition
nums1 has enough space to hold elements of nums2.

Idea
Use three pointers starting from the end.

Pointers
i → last element of nums1
j → last element of nums2
k → last position of nums1

Approach
Compare nums1[i] and nums2[j].
Place the larger value at nums1[k].

Move pointers backward.

If nums2 still has elements left,
copy them into nums1.

Time Complexity
O(m + n)

Space Complexity
O(1)
"""
""" more easy solutions
    class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[m:] = nums2
        nums1.sort()"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead."""
        i=m-1
        j=n-1
        k=m+n-1

        while i >= 0 and j >=0:
         if nums1[i]>nums2[j]:
            nums1[k]=nums1[i]
            i=i-1
         else:
            nums1[k]= nums2[j]
            j=j-1
         k=k-1
        nums1[:j+1] = nums2[:j+1]     
               

