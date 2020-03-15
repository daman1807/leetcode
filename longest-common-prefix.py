class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""

        prefix = strs[0]
        for string in strs[1:]:
            new_prefix = ""
            for (p_char, s_char) in zip(prefix, string):
                if p_char == s_char:
                    new_prefix += s_char
                else:
                    break
            prefix = new_prefix
        return prefix


solution = Solution()
print(solution.longestCommonPrefix(["flower", "flow", "flight"]))
print(solution.longestCommonPrefix(["dog", "racecar", "car"]))
