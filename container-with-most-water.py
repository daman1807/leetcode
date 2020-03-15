class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        max_area = 0
        i, j = 0, len(height) - 1
        while i < j:
            area = min(height[i], height[j]) * abs(i - j)
            max_area = max(area, max_area)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area


solution = Solution()
print(solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(solution.maxArea([1, 3, 2, 5, 25, 24, 5]))
