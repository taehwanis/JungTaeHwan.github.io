def solution(board, h, w):
    count = 0
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]

    for i in range(len(dh)):
        h_check = h + dh[i]
        w_check = w + dw[i]

        if 0 <= h_check < len(board) and 0 <= w_check < len(board):
            if board[h_check][w_check] == board[h][w]:
                count += 1
    return count