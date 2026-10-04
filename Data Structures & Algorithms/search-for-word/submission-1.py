class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        def nearSearch(row,col, index):
            if index == len(word):
                return True
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[index] or (row,col) in path:
                return False
            path.add((row,col))
            res = nearSearch(row+1,col,index+1) or nearSearch(row-1,col,index+1) or nearSearch(row,col+1,index+1) or nearSearch(row,col-1,index+1)
            path.remove((row,col))
            return res
            

        for i in range(len(board)):
            for j in range(len(board[0])):
                if nearSearch(i,j,0):
                    return True
        return False