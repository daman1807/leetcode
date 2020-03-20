class Solution(object):
    def permute_base(self, nums, permutation, permutations):
        if len(nums) == len(permutation):
            permutations.append(permutation)
        else:
            for (i, num) in enumerate(nums):
                if num not in permutation:
                    self.permute_base(nums, permutation + [num], permutations)

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        permutations = []
        for num in nums:
            self.permute_base(nums, [num], permutations)
        return permutations


solution = Solution()
print(solution.permute([]))
print(solution.permute([1, 2, 3]))
print(solution.permute([1, 2, 3, 4]))
