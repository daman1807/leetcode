rev_map = {
    "(": ")",
    "{": "}",
    "[": "]"
}


class Solution(object):
    def isValid(self, s):

        heap = []
        for c in s:
            if c in rev_map.keys():
                heap.append(rev_map[c])
            else:
                if len(heap) > 0 and heap[-1] == c:
                    heap = heap[:-1]
                else:
                    return False

        if len(heap) == 0:
            return True
        return False

        """
        :type s: str
        :rtype: bool
        """


solution = Solution()
print(solution.isValid(""))
print(solution.isValid(")"))
print(solution.isValid("()"))
print(solution.isValid("()[]{}"))
print(solution.isValid("(]"))
print(solution.isValid("{[]}"))
