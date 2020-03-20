class Solution(object):

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        res = []

        if numRows == 1:
            return s

        n = len(s)
        cycle = numRows * 2 - 2

        for i in range(numRows):
            for j in range(i, n, cycle):
                res.append(s[j])
                if not i == numRows - 1 and \
                        not i == 0 and j + cycle - 2 * i < n:
                    res.append(s[j + cycle - 2 * i])

        return "".join(res)


solution = Solution()
print(solution.convert("", 3))
print(solution.convert("DAMAN", 10))
print(solution.convert("PAYPALISHIRING", 3))
print(solution.convert("PAYPALISHIRING", 4))
