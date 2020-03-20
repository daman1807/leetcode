class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == haystack:
            return 0
        n = len(haystack)
        m = len(needle)
        for i in range(n):
            if i + m <= n:
                if haystack[i:i + m] == needle:
                    return i
        return -1


solution = Solution()
print(solution.strStr("hello", "ll"))
print(solution.strStr("", ""))
print(solution.strStr("mississippi", "pi"))
