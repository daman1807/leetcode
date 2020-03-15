class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        store = {}
        for (i, num) in enumerate(nums):
            if num in store:
                return [store[num], i]
            else:
                store[target - num] = i
