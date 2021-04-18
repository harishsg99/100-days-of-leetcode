class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        t = len(digits)
        c = digits[t-1]
        a = digits[t-1] + 1
        digits.remove(c)
        digits.append(a)
        return digits
        
