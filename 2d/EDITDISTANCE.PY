class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        matrix = [ [float("inf")] * (len(word2) + 1) for i in range (len(word1) + 1 ) ]
         #making a 2d array with word 1 and word 2 with an extra row/column to establish the base case 

        for j in range(len(word2)+1):
            matrix[len(word1)][j] = len(word2) - j 
        for i in range(len(word1)+1):
            matrix[i][len(word2)] = len(word1) - i 
        
        # - a d c   ""
        # a          1
        # b          2
        # c          3
       # "" 1 2 3    X   #ESTABLISHING the base cases as above where the characters in string are absent and we are required to add characters (thus the operations increment)

        for i in range(len(word1)-1,-1,-1):
            for j in range(len(word2)-1,-1,-1):
                if word1[i] == word2[j]: #best case scenario where the characters match since zero operation needed for these two chars
                    matrix[i][j] = matrix[i+1][1+j]
                else: #account for min most for replace i.e same as above, delete, insert 
                    matrix[i][j] = 1 + min(matrix[i+1][j+1],matrix[i+1][j],matrix[i][j+1])
        
        return matrix[0][0]

        