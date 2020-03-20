class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        count = 1
        for i in range(1, len(nums)):
            if not nums[i] == nums[i - 1]:
                nums[count] = nums[i]
                count += 1
        return count


solution = Solution()
print(solution.removeDuplicates([]))
print(solution.removeDuplicates([1, 1]))
print(solution.removeDuplicates([1, 1, 2]))
print(solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
