class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = False
        if x < 0:
            neg = True
        x = str(abs(x))
        x = x[::-1]
        x = int(x)
        if neg:
            x = -1 * x

        if abs(x) > 0x7FFFFFFF:
            return 0
        return x
