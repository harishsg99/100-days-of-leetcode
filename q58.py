class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split() 
        if len(s) == 0:  
            #s == []
            return 0
        else :
            return len(s[-1])
