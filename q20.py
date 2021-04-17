class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # base case
        if len(s) == 0: return True
        d = {')':'(', '}': '{', ']':'['}
        stack = []
        for char in s:
            if char not in d:
                stack.append(char)
            else:
                if len(stack) == 0 or d[char] != stack.pop():
                    return False
                
        return len(stack) == 0
