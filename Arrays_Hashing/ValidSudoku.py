# You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

# Each row must contain the digits 1-9 without duplicates.
# Each column must contain the digits 1-9 without duplicates.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set) #empty set for rows
        columns = collections.defaultdict(set)#empty set for columns
        square = collections.defaultdict(set) 
        #in squares we can identify by r // 3, c // 3 as its a 9x9 square
        #so basically ignoring remainder we can find what square is the small number is
        #part of
        for r in range (9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                    #ignore the value if no numbers are there
                if(board[r][c] in rows[r] or
                   board[r][c] in columns[c] or
                   board[r][c] in square[(r//3,c//3)]):
                     return False
#if the value exist in that specific column or row or the square
#square identified by r//3 and c//3
                columns[c].add(board[r][c])
                rows[r].add(board[r][c])
                square[(r//3,c//3)].add(board[r][c])
#we are adding the value in that position to check for
#dups in case of false sudoko so adding in our dict

        return True

#.add()setAdds a single element to a set.append()listAdds a single element to the end of a list.extend()listAdds multiple elements (from another iterable) to a list


        