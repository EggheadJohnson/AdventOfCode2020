from a import countSeats

def checkDirection(spot, step, board):
    while spot[0] + step[0] >=0 and spot[0] + step[0] < len(board) and spot[1] + step[1] >= 0 and spot[1] + step[1] < len(board[0]):
        if board[spot[0]+step[0]][spot[1]+step[1]] != '.':
            return board[spot[0]+step[0]][spot[1]+step[1]]
        else:
            spot = (spot[0] + step[0], spot[1] + step[1])
    return None

def checkBoard(board):
    new_board = []
    seats_changed = 0
    for i, line in enumerate(board):
        new_line = ''
        for j, c in enumerate(line):
            if c == '.':
                new_line += '.'
                continue
            if c == 'L':
                seat_occ = False
            if c == '#':
                seat_occ = True
            vis_seat_occ = 0
            for direction in (
                (-1, -1),
                (-1,  0),
                (-1,  1),
                ( 0, -1),
                ( 0,  1),
                ( 1, -1),
                ( 1,  0),
                ( 1,  1),
            ):
                dir_res = checkDirection((i, j), direction, board)
                if dir_res == '#':
                    vis_seat_occ += 1
            if seat_occ and vis_seat_occ >= 5:
                new_line += 'L'
                seats_changed += 1
            elif not seat_occ and vis_seat_occ == 0:
                new_line += '#'
                seats_changed += 1
            else:
                new_line += c

        new_board.append(new_line)
    return new_board, seats_changed

def b(input):
    board = input
    seats_changed = 1
    while seats_changed > 0:
        board, seats_changed = checkBoard(board)
        occ_seat_ctr, unocc_seat_ctr = countSeats(board)
        # print(seats_changed, occ_seat_ctr, unocc_seat_ctr)
    return occ_seat_ctr
