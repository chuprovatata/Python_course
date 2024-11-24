"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/constrained-subsequence-sum/
"""


class Solution(object):
    def constrainedSubsetSum(self, nums, k):
        deque = []
        for i, num in enumerate(nums):
            while deque and deque[0] < i - k:
                deque.pop(0)
            if deque:
                nums[i] = nums[deque[0]] + num
            while deque and nums[deque[-1]] < nums[i]:
                deque.pop()
            if nums[i] > 0:
                deque.append(i)
        return max(nums)
