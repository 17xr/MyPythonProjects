def done_or_not(board):
    done = False
    check = []
    for i in board:
        check.extend(i)
        if len(set(check)) != 9:
            done = True
        check.clear()
    for i in range(9):
        for j in board:
            check.append(j[i])
        if len(set(check)) != 9:
            done = True
        check.clear()
    regions = [board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3] for i in range(0,9,3) for j in range(0,9,3)]
    for region in regions:
        if len(set(region)) != 9:
            done = True
    if done:
        return 'Try again!'
    return 'Finished!'
############################################
def done_or_not2(board):
    regions = [board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3] for i in range(0,9,3) for j in range(0,9,3)]
    for elements in (board, zip(*board) ,regions):
        for element in elements:
            if len(set(element)) != 9:
                return 'Try again!'
    return 'Finished!'
