def noConflicts(board, current, qindex, n):
    for i in range(current):
        if board[qindex][i] == 1:
            return False
    k = 1
    while (qindex - k >= 0) and (current - k >= 0):
        if board[qindex - k][current - k] == 1:
            return False
        k += 1
    k = 1
    while (qindex + k < n) and (current - k >= 0):
        if board[qindex + k][current - k] == 1:
            return False
        k += 1
    return True

def FourQueens(n=4):
    board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(n):
        board[i][0] = 1
        for j in range(n):
            if noConflicts(board, 1, j, 4):
                board[j][1] = 1
                for k in range(n):
                    if noConflicts(board, 2, k, 4):
                        board[k][2] = 1
                        for l in range(n):
                            if noConflicts(board, 3, l, n):
                                board[l][3] = 1
                                clear = board
                                print(clear)
                                board[l][3] = 0
                        board[k][2] = 0
                board[j][1] = 0
        board[i][0] = 0
    return

FourQueens()
