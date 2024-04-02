'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

class Solution(object):
    def twoSum(self,nums, target):
        numsWithIndex = [(num, i) for i, num in enumerate(nums)]
        numsWithIndex.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            num_sum = numsWithIndex[left][0] + numsWithIndex[right][0]
            if num_sum == target:
                return [numsWithIndex[left][1], numsWithIndex[right][1]]
            elif num_sum < target:
                left += 1
            else:
                right -= 1
        return []  # No solution found!

    '''
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        numMap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i
    '''

    '''
    def twoSum(self, nums, target):
        #import numpy as np
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        args=np.argsort(nums)
        nums=np.array(nums)[args]
        j=len(nums)-1
        i=0
        for _ in range(len(nums)):
            s=nums[i]+nums[j]
            if s==target:
                return list(args[[i,j]])
            elif s<target:
                i+=1
            else:
                j-=1
    '''
