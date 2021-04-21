class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        li2 = [ y for x in board for y in x]
        test = ','.join(map(str,li2))
        str1 = ""
        str1.join(test)
        N = len(word)
        M = len(str1)
 
        for i in range(N - M + 1):
 

            for j in range(M):
                if (st1[i + j] != word[j]):
                    break
             
                if j + 1 == M :
                    return True
 
        return False
            
