class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        if len(nums) == 0:
            return count
        for (i, num) in enumerate(nums):
            if not num == val:
                nums[count] = nums[i]
                count += 1
        return count


solution = Solution()
print(solution.removeElement([3, 2, 2, 3], 3))
print(solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
