class Solution(object):

    def isValid(self, s):

        heap = []
        for c in s:
            if c == "(":
                heap.append("(")
            else:
                if len(heap) > 0 and heap[-1] == "(":
                    heap = heap[:-1]
                else:
                    return False

        if len(heap) == 0:
            return True
        return False

    def createCombinations(self, prefix, n, combinations):
        if n == 0:
            if self.isValid(prefix):
                combinations.append(prefix)
        else:
            self.createCombinations(prefix + "(", n - 1, combinations)
            self.createCombinations(prefix + ")", n - 1, combinations)

    def generateParenthesis(self, n):
        combinations = []
        self.createCombinations("", n * 2, combinations)
        return combinations
        """
        :type n: int
        :rtype: List[str]
        """


solution = Solution()
print(solution.generateParenthesis(0))
print(solution.generateParenthesis(1))
print(solution.generateParenthesis(2))
print(solution.generateParenthesis(3))
