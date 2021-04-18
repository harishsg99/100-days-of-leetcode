class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        # approach: Newton's method for root-finding

        result = x
        while not result * result - x < 1:
            result = (result + x / result) / 2

        return int(result)
        
