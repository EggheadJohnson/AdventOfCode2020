def take_step(board):
    new_board = []
    seats_changed = 0
    for i, line in enumerate(board):
        new_line = ''

        for j, c in enumerate(line):
            if board[i][j] == 'L':
                seat_occ = False
            elif board[i][j] == '#':
                seat_occ = True
            elif board[i][j] == '.':
                new_line += '.'
                continue
            adj_occ_ctr = 0
            if i > 0:
                if j > 0:
                    if board[i-1][j-1] == '#':
                        adj_occ_ctr += 1
                if board[i-1][j] == '#':
                    adj_occ_ctr += 1
                if j < len(board[i]) - 1:
                    if board[i-1][j+1] == '#':
                        adj_occ_ctr += 1
            if j > 0:
                if board[i][j-1] == '#':
                    adj_occ_ctr += 1
            if j < len(board[i]) - 1:
                if board[i][j+1] == '#':
                    adj_occ_ctr += 1
            if i < len(board) - 1:
                if j > 0:
                    if board[i+1][j-1] == '#':
                        adj_occ_ctr += 1
                if board[i+1][j] == '#':
                    adj_occ_ctr += 1
                if j < len(board[i]) - 1:
                    if board[i+1][j+1] == '#':
                        adj_occ_ctr += 1
            if not seat_occ and adj_occ_ctr == 0:
                new_line += '#'
                seats_changed += 1
            elif seat_occ and adj_occ_ctr >= 4:
                new_line += 'L'
                seats_changed += 1
            else:
                new_line += board[i][j]
        # print(new_line)
        new_board.append(new_line)
    return new_board, seats_changed

def countSeats(board):
    occ_seat_ctr = 0
    unocc_seat_ctr = 0
    for line in board:
        for c in line:
            if c == 'L':
                unocc_seat_ctr += 1
            elif c == '#':
                occ_seat_ctr += 1
    return occ_seat_ctr, unocc_seat_ctr
def a(input):
    board = input
    seats_changed = 1
    while seats_changed > 0:
        board, seats_changed = take_step(board)
        occ_seat_ctr, unocc_seat_ctr = countSeats(board)
        # print(seats_changed, occ_seat_ctr, unocc_seat_ctr)
    return occ_seat_ctr
