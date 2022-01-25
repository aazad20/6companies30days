    
    def adjacentSearch(self, board, word, i, j, l):
        if l == len(word):
            return True
        if(i < 0 or j < 0 or i >= len(board) or j >= len(board[0])):
            return False
        if(board[i][j] != word[l]):
            return False
        board[i][j] = '*'
        ans = self.adjacentSearch(board, word, i-1, j, l+1) or self.adjacentSearch(board, word, i+1, j, l+1) or self.adjacentSearch(board, word, i, j-1, l+1) or self.adjacentSearch(board, word, i, j+1, l+1)
        board[i][j] = word[l]
        
        return ans
    
    
    def isWordExist(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and self.adjacentSearch(board, word, i, j, 0):
                    return True
        return False
