'''
1. We start the backtracking if we find the first letter of the word in the grid. 
2. To prevent reusing this cell, we take an action of changing its value to # storing its original, move in all directions to find the next letter.
3. If in any direction we couldnt find we undo that path by replacing the stored value back in its place (backtrack).
4. Base case is when we are able to reach the end of the word in search. Return true. In cases like out of bounds or char mismatch, return False.

TC: O(m*n*3^s) -> since we are searching entire grid for the start m*n and from there we move in 3 directions for a distance of length of string (s)
SC: O(s) -> Recursion stack = len of string

'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or len(board) == 0:
            return False
        
        self.m = len(board)
        self.n = len(board[0])
        self.dirs = [[0,1],[0,-1],[1,0],[-1,0]]

        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == word[0]:
                    if self.backtrack(board,i,j,word,0) == True:
                        return True
        return False
    
    def backtrack(self,board, row,col,word,index):
        #base
        if index == len(word):
            return True
            
        if row < 0 or row == self.m or col < 0 or col == self.n or board[row][col] != word[index] or index >= len(word):
            return False
        
        #logic
        if board[row][col] == word[index]:
            #action
            for Dir in self.dirs:
                temp = board[row][col]
                board[row][col] = '#'
                nr = row + Dir[0]
                nc = col + Dir[1]
                #recurse
                if self.backtrack(board, nr, nc, word, index+1):
                    return True
                
                #backtrack
                board[row][col] = temp
            
        
            

