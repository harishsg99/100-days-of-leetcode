class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = len(s)
        b = []
        for i in range(a-1):
            if(s[i].isalpha()==False):
                s[i].replace(s[i], '')
                b.append(s[i])
        
        c = len(b)
        for i in range(c-1):
            if(b[i] == b[c-i-1]):
                return True
            else:
                return False
        
