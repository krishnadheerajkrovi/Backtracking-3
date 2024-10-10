'''
1. We start by creating a grid of falses where we can place the queens. We are filling queens row by row.
2. In backtracking we do the following. If in any column it is safe to place the queen, we do by updating grid and moving down to next row.
3. In the case we cannot place it at no col in a row we would just return back to previous row and moving to next col undoing current placement.
4. The base case is when row reaches out of board. In that case take the status of the grid, form response and append to result array.

TC: O(n!) -> Since we have n chances to place in first, n-2 in second once placed first, n-3 in third...
SC: O(n^2) -> As we are using a grid to store the results
'''

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 0:
            return []
 
        self.answer = []
        self.grid = [[False for i in range(n)] for j in range(n)]

        self.backtrack(0)

        return self.answer

    def backtrack(self, row : int) -> None:
        # base
        n = len(self.grid)
        if row == n:
            res = []
            for i in range(n):
                row_res = []
                for j in range(n):
                    if self.grid[i][j]:
                        row_res.append('Q')
                    else:
                        row_res.append('.')
                res.append("".join(row_res))
            self.answer.append(res)
            return

        #logic
        for j in range(n):
            if self.isSafe(row, j):
                # action
                self.grid[row][j] = True
                
                #recurse
                self.backtrack(row + 1)

                #backtrack
                self.grid[row][j] = False

        
    def isSafe(self, row: int, col: int) -> bool:
        # Check upper rows
        for i in range(row, -1, -1):
            if self.grid[i][col]:
                return False
        # Upper left diagonal
        i = row
        j = col
        while i >= 0 and j >= 0:
            if self.grid[i][j]:
                return False
            i -= 1
            j -= 1
        
        # Upper right diagonal
        i = row
        j = col
        while i >= 0 and j < len(self.grid):
            if self.grid[i][j]:
                return False
            i -= 1
            j += 1
        
        return True
        
    