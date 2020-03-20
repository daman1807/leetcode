class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for c in s:
            if c != " ":
                count += 1
            else:
                count = 0
        # print(count, max_count)
        return count


solution = Solution()
print(solution.lengthOfLastWord("Hello World"))
print(solution.lengthOfLastWord("HelloWorld"))
print(solution.lengthOfLastWord("a "))
print(solution.lengthOfLastWord("b a   "))
