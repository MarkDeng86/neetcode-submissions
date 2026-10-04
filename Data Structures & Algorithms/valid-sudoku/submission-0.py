class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check = {"1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}

        # horizontal
        for i in range(len(board)):
            check = {"1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}
            for j in range(len(board)):
                if board[i][j] != ".":
                    if check[board[i][j]] == 1:
                        return False
                    else:
                        check[board[i][j]] = 1
                    
        # vertical
        for i in range(len(board)):
            check = {"1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}
            for j in range(len(board)):
                if board[j][i] != ".":
                    if check[board[j][i]] == 1:
                        return False
                    else:
                        check[board[j][i]] = 1

        # 3x3
        for i in range(3):
            for j in range(3):
                check = {"1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}
                #print("New Square")
                for subi in range(i*3,i*3+3):
                    for subj in range(j*3, j*3+3):
                        print("Check: " + str(subi) + "," + str(subj))
                        if board[subi][subj] != ".":
                            if check[board[subi][subj]] == 1:
                                return False
                            else:
                                check[board[subi][subj]] = 1
                #print(check.items())
                
        return True
