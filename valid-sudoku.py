from math import floor
from pprint import pprint


class Solution(object):
    def add(self, i, j, val):
        if not val == ".":
            key = "{}|{}".format(
                floor(i), floor(j)
            )
            if key in self.boxes:
                if val in self.boxes[key]:
                    return False
                else:
                    self.boxes[key].add(val)
            else:
                self.boxes[key] = {val}
        return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        m = len(board)
        n = len(board[0])

        if m == 0 and n == 0:
            return False

        self.boxes = {}
        for i in range(m):
            for j in range(n):
                # vertical check
                if not self.add(-1, i, board[i][j]):
                    return False
                # horizontal check
                if not self.add(j, -1, board[i][j]):
                    return False
                # box check
                if not self.add(i / 3, j / 3, board[i][j]):
                    return False
        pprint(self.boxes)
        return True


solution = Solution()
print(solution.isValidSudoku([
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]))

print(solution.isValidSudoku([
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]))

print(solution.isValidSudoku([
    [".", ".", "5", ".", ".", ".", ".", ".", "."],
    ["1", ".", ".", "2", ".", ".", ".", ".", "."],
    [".", ".", "6", ".", ".", "3", ".", ".", "."],
    ["8", ".", ".", ".", ".", ".", ".", ".", "."],
    ["3", ".", "1", "5", "2", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "4", "."],
    [".", ".", "6", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "9", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."]
]))
