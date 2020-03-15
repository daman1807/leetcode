digit_map = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
}


class Solution(object):
    def getCombinations(self, prefix, digits, combinations):
        if len(digits) == 0:
            if len(prefix) > 0 :
                combinations.append(prefix)
            return
        else:
            for char in digit_map[digits[0]]:
                self.getCombinations(prefix + char, digits[1:], combinations)

    def letterCombinations(self, digits):
        combinations = []
        self.getCombinations("", digits, combinations)
        return combinations
        """
        :type digits: str
        :rtype: List[str]
        """


solution = Solution()
print(solution.letterCombinations("23"))
print(solution.letterCombinations(""))
