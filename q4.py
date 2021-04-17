class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <=1: return s
        dp = [[False for _ in range (len(s))] for _ in range(len(s))]
        start, maxlen = -1, 0
        for j in range(len(s)):
            for i in range(0,j+1):
                if i == j:
                    dp[i][j] = True
                elif j - i == 1:
                    dp[i][j] = s[i]==s[j]
                elif j - i > 1:
                    if dp[i+1][j-1] and s[i]==s[j]:
                        dp[i][j] = True
                if dp[i][j]:
                    if j - i + 1 > maxlen:
                        start = i
                        maxlen = j-i+1
        return s[start:start+maxlen]
