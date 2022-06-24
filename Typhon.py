import keyboard
import time
import os
import turtle

t = turtle.Turtle()
w = turtle.Screen()

board_size = 1.0
background_color = "black"
light_boardcolor = "ivory"
dark_boardcolor = "burlywood"
light_piececolor = "wheat"
dark_piececolor = "saddle brown"
crown_color = "gold"
t.speed(0)
w.title("Typhon")
w.bgcolor(background_color)
t.hideturtle()
bp = 'RNBQKBNRPPPPPPPP00000000000000000000000000000000pppppppprnbqkbnr'
global new_bp, past_bp
directory = 'D:\\Pycharm_Database\\Typhon_Directory\\'
bp_library = directory + 'BP_Library\\'


####################################################################################
# GRAPHICS FUNCTIONS
####################################################################################


def goto_pos(x, y):
    t.up()
    t.goto(-350 * board_size, -350 * board_size)
    t.setheading(0)
    t.forward((x - 1) * 100 * board_size)
    t.setheading(90)
    t.forward((y - 1) * 100 * board_size)
    t.down()


def square(x, y, color):
    t.up()
    t.goto(x, y)
    t.down()
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.forward(100 * board_size)
        t.left(90)
    t.end_fill()
    t.hideturtle()


def draw_board():
    t.setheading(0)
    t.up()
    t.goto(-400 * board_size, -400 * board_size)
    t.down()
    t.fillcolor(light_boardcolor)
    t.begin_fill()
    for i in range(4):
        t.forward(800 * board_size)
        t.left(90)
    t.end_fill()
    for i in range(4):
        square(-400 * board_size + i * 200 * board_size, -400 * board_size, dark_boardcolor)
        square(-300 * board_size + i * 200 * board_size, -300 * board_size, dark_boardcolor)
        square(-400 * board_size + i * 200 * board_size, -200 * board_size, dark_boardcolor)
        square(-300 * board_size + i * 200 * board_size, -100 * board_size, dark_boardcolor)
        square(-400 * board_size + i * 200 * board_size, 0, dark_boardcolor)
        square(-300 * board_size + i * 200 * board_size, 100 * board_size, dark_boardcolor)
        square(-400 * board_size + i * 200 * board_size, 200 * board_size, dark_boardcolor)
        square(-300 * board_size + i * 200 * board_size, 300 * board_size, dark_boardcolor)


def set_board():
    for i in range(8):
        pawn(i + 1, 2, light_piececolor)
    for i in range(8):
        pawn(i + 1, 7, dark_piececolor)
    byshop(3, 1, light_piececolor)
    byshop(3, 8, dark_piececolor)
    byshop(6, 1, light_piececolor)
    byshop(6, 8, dark_piececolor)
    queen(4, 1, light_piececolor)
    queen(4, 8, dark_piececolor)
    king(5, 1, light_piececolor)
    king(5, 8, dark_piececolor)
    rook(1, 1, light_piececolor)
    rook(1, 8, dark_piececolor)
    rook(8, 1, light_piececolor)
    rook(8, 8, dark_piececolor)
    knight(2, 1, light_piececolor)
    knight(2, 8, dark_piececolor)
    knight(7, 1, light_piececolor)
    knight(7, 8, dark_piececolor)


def erase_piece(x, y):
    # print('x in erase: ' + str(x))
    # print('y in erase: ' + str(y))
    global square_color
    t.hideturtle()
    t.color("black")
    if (y % 2 == 1) and ((x == 1) or (x == 3) or (x == 5) or (x == 7)):
        square_color = dark_boardcolor
        # print(square_color, "1st")
    elif (y % 2 == 0) and ((x == 1) or (x == 3) or (x == 5) or (x == 7)):
        square_color = light_boardcolor
        # print(square_color, "2nd")
    elif (y % 2 == 1) and ((x == 2) or (x == 4) or (x == 6) or (x == 8)):
        square_color = light_boardcolor
        # print(square_color, "3rd")
    elif (y % 2 == 0) and ((x == 2) or (x == 4) or (x == 6) or (x == 8)):
        square_color = dark_boardcolor
        # print(square_color, "4th")
    t.goto(-400 * board_size, -400 * board_size)
    t.setheading(0)
    t.forward(100 * x * board_size)
    t.setheading(90)
    t.forward(100 * y * board_size)
    t.fillcolor(square_color)
    t.begin_fill()
    t.down()
    for i in range(4):
        t.left(90)
        t.forward(100 * board_size)
    t.end_fill()
    t.up()
    # print('square filled with: ' + square_color)


def pawn(x, y, color):
    goto_pos(x, y)
    t.down()
    t.fillcolor(color)
    t.setheading(0)
    t.begin_fill()
    t.circle(12 * board_size)
    t.setheading(230)
    t.forward(40 * board_size)
    t.setheading(0)
    t.forward(51 * board_size)
    t.setheading(130)
    t.forward(40 * board_size)
    t.end_fill()
    t.up()


def byshop(x, y, color):
    goto_pos(x, y)
    t.down()
    t.fillcolor(color)
    t.setheading(0)
    t.begin_fill()
    t.circle(12 * board_size)
    t.setheading(230)
    t.forward(40 * board_size)
    t.setheading(0)
    t.forward(51 * board_size)
    t.setheading(130)
    t.forward(40 * board_size)
    t.end_fill()
    t.up()
    t.setheading(90)
    t.forward(20 * board_size)
    t.down()
    t.begin_fill()
    t.setheading(0)
    t.forward(15 * board_size)
    t.backward(30 * board_size)
    t.setheading(60)
    t.forward(30 * board_size)
    t.setheading(-60)
    t.forward(30 * board_size)
    t.setheading(180)
    t.forward(15 * board_size)
    t.end_fill()
    t.up()


def king(x, y, color):
    goto_pos(x, y)
    t.down()
    t.fillcolor(color)
    t.setheading(0)
    t.begin_fill()
    t.circle(12 * board_size)
    t.setheading(230)
    t.forward(40 * board_size)
    t.setheading(0)
    t.forward(51 * board_size)
    t.setheading(130)
    t.forward(40 * board_size)
    t.end_fill()
    t.fillcolor(crown_color)
    t.up()
    t.setheading(90)
    t.forward(15 * board_size)
    t.down()
    t.begin_fill()
    t.setheading(0)
    t.forward(15 * board_size)
    t.setheading(90)
    t.forward(10 * board_size)
    t.setheading(180)
    t.forward(30 * board_size)
    t.setheading(270)
    t.forward(10 * board_size)
    t.setheading(0)
    t.forward(30 * board_size)
    t.setheading(90)
    t.forward(10 * board_size)
    for i in range(3):
        t.setheading(120)
        t.forward(10 * board_size)
        t.setheading(-120)
        t.forward(10 * board_size)
    t.end_fill()
    t.up()


def queen(x, y, color):
    goto_pos(x, y)
    t.down()
    t.fillcolor(color)
    t.setheading(0)
    t.begin_fill()
    t.circle(12 * board_size)
    t.setheading(230)
    t.forward(40 * board_size)
    t.setheading(0)
    t.forward(51 * board_size)
    t.setheading(130)
    t.forward(40 * board_size)
    t.end_fill()
    t.fillcolor(crown_color)
    t.up()
    t.setheading(90)
    t.forward(15 * board_size)
    t.down()
    t.begin_fill()
    t.setheading(0)
    t.forward(15 * board_size)
    t.backward(30 * board_size)
    t.setheading(60)
    t.forward(30 * board_size)
    t.setheading(-60)
    t.forward(30 * board_size)
    t.setheading(180)
    t.forward(15 * board_size)
    t.end_fill()
    t.up()


def rook(x, y, color):
    t.fillcolor(color)
    goto_pos(x, y)
    t.setheading(270)
    t.forward(30 * board_size)
    t.down()
    t.begin_fill()
    t.setheading(0)
    t.backward(15 * board_size)
    t.forward(30 * board_size)
    t.setheading(90)
    t.forward(50 * board_size)
    t.setheading(180)
    t.forward(30 * board_size)
    t.setheading(270)
    t.forward(50 * board_size)
    t.end_fill()
    t.begin_fill()
    t.backward(50 * board_size)
    t.setheading(180)
    t.forward(10 * board_size)
    t.setheading(90)
    t.forward(15 * board_size)
    t.setheading(0)
    t.forward(50 * board_size)
    t.setheading(270)
    t.forward(15 * board_size)
    t.setheading(180)
    t.forward(25 * board_size)
    t.end_fill()
    t.up()
    t.forward(25 * board_size)
    t.setheading(90)
    t.forward(15 * board_size)
    for i in range(3):
        t.begin_fill()
        t.setheading(90)
        t.forward(5 * board_size)
        t.setheading(0)
        t.forward(8 * board_size)
        t.setheading(270)
        t.forward(5 * board_size)
        t.end_fill()
        t.setheading(0)
        t.forward(6 * board_size)
    t.begin_fill()
    t.setheading(90)
    t.forward(5 * board_size)
    t.setheading(0)
    t.forward(8 * board_size)
    t.setheading(270)
    t.forward(5 * board_size)
    t.end_fill()
    t.up()


def knight(x, y, color):
    goto_pos(x, y)
    t.down()
    t.fillcolor(color)
    t.setheading(0)
    t.begin_fill()
    t.circle(12 * board_size)
    t.setheading(230)
    t.forward(40 * board_size)
    t.setheading(0)
    t.forward(51 * board_size)
    t.setheading(130)
    t.forward(40 * board_size)
    t.end_fill()
    t.begin_fill()
    t.setheading(180)
    t.forward(30 * board_size)
    t.circle(-6 * board_size)
    t.up()
    t.setheading(90)
    t.forward(12 * board_size)
    t.setheading(20)
    t.forward(30 * board_size)
    t.end_fill()
    t.begin_fill()
    t.setheading(-25)
    for i in range(3):
        t.forward(15 * board_size)
        t.left(120)
    t.end_fill()
    t.up()


def y_coordinate(num):
    for i in range(8):
        if (9 + (i * 8)) > (num) > (0 + (i * 8)):
            return int(i + 1)


def update_board(new_board, old_board):
    for i in range(64):
        x = ((i % 8) + 1)
        y = y_coordinate(i + 1)
        j = i + 1
        if new_board[i:j] != old_board[i:j]:
            if new_board[i:j] == '0':
                erase_piece(x, y)
            elif new_board[i:j] == 'p':
                erase_piece(x, y)
                pawn(((i % 8) + 1), y_coordinate(j), dark_piececolor)
            elif new_board[i:j] == 'r':
                erase_piece(x, y)
                rook(((i % 8) + 1), y_coordinate(j), dark_piececolor)
            elif new_board[i:j] == 'n':
                erase_piece(x, y)
                knight(((i % 8) + 1), y_coordinate(j), dark_piececolor)
            elif new_board[i:j] == 'b':
                erase_piece(x, y)
                byshop(((i % 8) + 1), y_coordinate(j), dark_piececolor)
            elif new_board[i:j] == 'q':
                erase_piece(x, y)
                queen(((i % 8) + 1), y_coordinate(j), dark_piececolor)
            elif new_board[i:j] == 'k':
                erase_piece(x, y)
                king(((i % 8) + 1), y_coordinate(j), dark_piececolor)
            elif new_board[i:j] == 'P':
                erase_piece(x, y)
                pawn(((i % 8) + 1), y_coordinate(j), light_piececolor)
            elif new_board[i:j] == 'R':
                erase_piece(x, y)
                rook(((i % 8) + 1), y_coordinate(j), light_piececolor)
            elif new_board[i:j] == 'N':
                erase_piece(x, y)
                knight(((i % 8) + 1), y_coordinate(j), light_piececolor)
            elif new_board[i:j] == 'B':
                erase_piece(x, y)
                byshop(((i % 8) + 1), y_coordinate(j), light_piececolor)
            elif new_board[i:j] == 'Q':
                erase_piece(x, y)
                queen(((i % 8) + 1), y_coordinate(j), light_piececolor)
            elif new_board[i:j] == 'K':
                erase_piece(x, y)
                king(((i % 8) + 1), y_coordinate(j), light_piececolor)


####################################################################################
# ADD PIECE MOVES FUNCTIONS
####################################################################################


def add_dark_rooks(num):
    x = ((num % 8) + 1)
    y = y_coordinate(num + 1)
    global new_bp, bp
    for i in range(7):
        if 9 > (x + (i + 1)) > 0:
            if between_target(x, y, (x + (i + 1)), y):
                break
            elif target((x + (i + 1)), y, 'black'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = (x + (i + 1))
                x_position = new_x - 1
                position = x_position + ((y - 1) * 8)
                new_bp[position] = 'r'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
    for i in range(7):
        if 9 > (x - (i + 1)) > 0:
            if between_target(x, y, (x - (i + 1)), y):
                break
            elif target((x - (i + 1)), y, 'black'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = (x - (i + 1))
                x_position = new_x - 1
                position = x_position + ((y - 1) * 8)
                new_bp[position] = 'r'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
    for i in range(7):
        if 9 > (y + (i + 1)) > 0:
            if between_target(x, y, x, (y + (i + 1))):
                break
            elif target(x, (y + (i + 1)), 'black'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_y = (y + (i + 1))
                x_position = x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'r'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
    for i in range(7):
        if 9 > (y - (i + 1)) > 0:
            if between_target(x, y, x, (y - (i + 1))):
                break
            elif target(x, (y - (i + 1)), 'black'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_y = (y - (i + 1))
                x_position = x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'r'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
    if check_board(bp, 2, 8, '0'):
        if check_board(bp, 3, 8, '0'):
            if check_board(bp, 4, 8, '0'):
                if never_moved(56):
                    if not check_king(bp, 'black'):
                        if not check_square(bp, 4, 8, 'black'):
                            new_bp = list(bp)
                            new_bp[56] = '0'
                            new_bp[60] = '0'
                            new_bp[58] = 'k'
                            new_bp[59] = 'r'
                            new_bp = str(new_bp)
                            new_bp = new_bp.replace(' ', '')
                            new_bp = new_bp.replace('[', '')
                            new_bp = new_bp.replace(']', '')
                            new_bp = new_bp.replace(',', '')
                            new_bp = new_bp.replace("'", '')
                            moves_on_board.append(str(new_bp))
    if check_board(bp, 6, 8, '0'):
        if check_board(bp, 7, 8, '0'):
            if never_moved(63):
                if not check_king(bp, 'black'):
                    if not check_square(bp, 6, 8, 'black'):
                        new_bp = list(bp)
                        new_bp[60] = '0'
                        new_bp[63] = '0'
                        new_bp[62] = 'k'
                        new_bp[61] = 'r'
                        new_bp = str(new_bp)
                        new_bp = new_bp.replace(' ', '')
                        new_bp = new_bp.replace('[', '')
                        new_bp = new_bp.replace(']', '')
                        new_bp = new_bp.replace(',', '')
                        new_bp = new_bp.replace("'", '')
                        moves_on_board.append(str(new_bp))


def add_light_rooks(num):
    x = ((num % 8) + 1)
    y = y_coordinate(num + 1)
    global new_bp
    for i in range(7):
        if 9 > (x + (i + 1)) > 0:
            if between_target(x, y, (x + (i + 1)), y):
                break
            elif target((x + (i + 1)), y, 'white'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = (x + (i + 1))
                x_position = new_x - 1
                position = x_position + ((y - 1) * 8)
                new_bp[position] = 'R'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
    for i in range(7):
        if 9 > (x - (i + 1)) > 0:
            if between_target(x, y, (x - (i + 1)), y):
                break
            elif target((x - (i + 1)), y, 'white'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = (x - (i + 1))
                x_position = new_x - 1
                position = x_position + ((y - 1) * 8)
                new_bp[position] = 'R'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
    for i in range(7):
        if 9 > (y + (i + 1)) > 0:
            if between_target(x, y, x, (y + (i + 1))):
                break
            elif target(x, (y + (i + 1)), 'white'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_y = (y + (i + 1))
                x_position = x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'R'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
    for i in range(7):
        if 9 > (y - (i + 1)) > 0:
            if between_target(x, y, x, (y - (i + 1))):
                break
            elif target(x, (y - (i + 1)), 'white'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_y = (y - (i + 1))
                x_position = x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'R'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
    if check_board(bp, 2, 1, '0'):
        if check_board(bp, 3, 1, '0'):
            if check_board(bp, 4, 1, '0'):
                if never_moved(0):
                    if not check_king(bp, 'white'):
                        if not check_square(bp, 4, 1, 'white'):
                            new_bp = list(bp)
                            new_bp[0] = '0'
                            new_bp[4] = '0'
                            new_bp[2] = 'K'
                            new_bp[3] = 'R'
                            new_bp = str(new_bp)
                            new_bp = new_bp.replace(' ', '')
                            new_bp = new_bp.replace('[', '')
                            new_bp = new_bp.replace(']', '')
                            new_bp = new_bp.replace(',', '')
                            new_bp = new_bp.replace("'", '')
                            moves_on_board.append(str(new_bp))
    if check_board(bp, 6, 1, '0'):
        if check_board(bp, 7, 1, '0'):
            if never_moved(7):
                if not check_king(bp, 'white'):
                    if not check_square(bp, 6, 1, 'white'):
                        new_bp = list(bp)
                        new_bp[4] = '0'
                        new_bp[7] = '0'
                        new_bp[6] = 'K'
                        new_bp[5] = 'R'
                        new_bp = str(new_bp)
                        new_bp = new_bp.replace(' ', '')
                        new_bp = new_bp.replace('[', '')
                        new_bp = new_bp.replace(']', '')
                        new_bp = new_bp.replace(',', '')
                        new_bp = new_bp.replace("'", '')
                        moves_on_board.append(str(new_bp))


def add_dark_knights(num):
    x = ((num % 8) + 1)
    y = y_coordinate(num + 1)
    global moves_on_board
    global new_bp
    if 9 > (x + 1) > 0:
        if 9 > (y + 2) > 0:
            if target((x + 1), (y + 2), 'black'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = x + 1
                new_y = y + 2
                x_position = new_x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'n'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
        if 9 > (y - 2) > 0:
            if target((x + 1), (y - 2), 'black'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = x + 1
                new_y = y - 2
                x_position = new_x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'n'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
    if 9 > (x - 1) > 0:
        if 9 > (y + 2) > 0:
            if target((x - 1), (y + 2), 'black'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = x - 1
                new_y = y + 2
                x_position = new_x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'n'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
        if 9 > (y - 2) > 0:
            if target((x - 1), (y - 2), 'black'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = x - 1
                new_y = y - 2
                x_position = new_x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'n'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
    if 9 > (x + 2) > 0:
        if 9 > (y + 1) > 0:
            if target((x + 2), (y + 1), 'black'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = x + 2
                new_y = y + 1
                x_position = new_x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'n'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
        if 9 > (y - 1) > 0:
            if target((x + 2), (y - 1), 'black'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = x + 2
                new_y = y - 1
                x_position = new_x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'n'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
    if 9 > (x - 2) > 0:
        if 9 > (y + 1) > 0:
            if target((x - 2), (y + 1), 'black'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = x - 2
                new_y = y + 1
                x_position = new_x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'n'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
        if 9 > (y - 1) > 0:
            if target((x - 2), (y - 1), 'black'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = x - 2
                new_y = y - 1
                x_position = new_x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'n'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))


def add_light_knights(num):
    x = ((num % 8) + 1)
    y = y_coordinate(num + 1)
    global moves_on_board
    global new_bp
    if 9 > (x + 1) > 0:
        if 9 > (y + 2) > 0:
            if target((x + 1), (y + 2), 'white'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = x + 1
                new_y = y + 2
                x_position = new_x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'N'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
        if 9 > (y - 2) > 0:
            if target((x + 1), (y - 2), 'white'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = x + 1
                new_y = y - 2
                x_position = new_x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'N'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
    if 9 > (x - 1) > 0:
        if 9 > (y + 2) > 0:
            if target((x - 1), (y + 2), 'white'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = x - 1
                new_y = y + 2
                x_position = new_x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'N'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
        if 9 > (y - 2) > 0:
            if target((x - 1), (y - 2), 'white'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = x - 1
                new_y = y - 2
                x_position = new_x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'N'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
    if 9 > (x + 2) > 0:
        if 9 > (y + 1) > 0:
            if target((x + 2), (y + 1), 'white'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = x + 2
                new_y = y + 1
                x_position = new_x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'N'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
        if 9 > (y - 1) > 0:
            if target((x + 2), (y - 1), 'white'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = x + 2
                new_y = y - 1
                x_position = new_x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'N'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
    if 9 > (x - 2) > 0:
        if 9 > (y + 1) > 0:
            if target((x - 2), (y + 1), 'white'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = x - 2
                new_y = y + 1
                x_position = new_x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'N'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
        if 9 > (y - 1) > 0:
            if target((x - 2), (y - 1), 'white'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = x - 2
                new_y = y - 1
                x_position = new_x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'N'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))


def add_dark_byshops(num):
    x = ((num % 8) + 1)
    y = y_coordinate(num + 1)
    global new_bp
    for i in range(7):
        if (9 > (x + (i + 1)) > 0) and (9 > (y + (i + 1)) > 0):
            if between_target(x, y, (x - (i + 1)), (y + (i + 1))):
                break
            elif target((x + (i + 1)), (y + (i + 1)), 'black'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = (x + (i + 1))
                x_position = new_x - 1
                position = x_position + (((y + (i + 1)) - 1) * 8)
                new_bp[position] = 'b'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
    for i in range(7):
        if (9 > (x - (i + 1)) > 0) and (9 > (y + (i + 1)) > 0):
            if between_target(x, y, (x - (i + 1)), (y + (i + 1))):
                break
            elif target((x - (i + 1)), (y + (i + 1)), 'black'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = (x - (i + 1))
                x_position = new_x - 1
                position = x_position + (((y + (i + 1)) - 1) * 8)
                new_bp[position] = 'b'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
    for i in range(7):
        if (9 > (x + (i + 1)) > 0) and (9 > (y - (i + 1)) > 0):
            if between_target(x, y, (x + (i + 1)), (y - (i + 1))):
                break
            elif target((x + (i + 1)), (y - (i + 1)), 'black'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = (x + (i + 1))
                x_position = new_x - 1
                position = x_position + (((y - (i + 1)) - 1) * 8)
                new_bp[position] = 'b'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
    for i in range(7):
        if (9 > (x - (i + 1)) > 0) and (9 > (y - (i + 1)) > 0):
            if between_target(x, y, (x - (i + 1)), (y - (i + 1))):
                break
            elif target((x - (i + 1)), (y - (i + 1)), 'black'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = (x - (i + 1))
                x_position = new_x - 1
                position = x_position + (((y - (i + 1)) - 1) * 8)
                new_bp[position] = 'b'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))


def add_light_byshops(num):
    x = ((num % 8) + 1)
    y = y_coordinate(num + 1)
    global new_bp
    for i in range(7):
        if (9 > (x + (i + 1)) > 0) and (9 > (y + (i + 1)) > 0):
            if between_target(x, y, (x + (i + 1)), (y + (i + 1))):
                break
            elif target((x + (i + 1)), (y + (i + 1)), 'white'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = (x + (i + 1))
                x_position = new_x - 1
                position = x_position + (((y + (i + 1)) - 1) * 8)
                new_bp[position] = 'B'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
    for i in range(7):
        if (9 > (x - (i + 1)) > 0) and (9 > (y + (i + 1)) > 0):
            if between_target(x, y, (x - (i + 1)), (y + (i + 1))):
                break
            elif target((x - (i + 1)), (y + (i + 1)), 'white'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = (x - (i + 1))
                x_position = new_x - 1
                position = x_position + (((y + (i + 1)) - 1) * 8)
                new_bp[position] = 'B'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
    for i in range(7):
        if (9 > (x + (i + 1)) > 0) and (9 > (y - (i + 1)) > 0):
            if between_target(x, y, (x + (i + 1)), (y - (i + 1))):
                break
            elif target((x + (i + 1)), (y - (i + 1)), 'white'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = (x + (i + 1))
                x_position = new_x - 1
                position = x_position + (((y - (i + 1)) - 1) * 8)
                new_bp[position] = 'B'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
    for i in range(7):
        if (9 > (x - (i + 1)) > 0) and (9 > (y - (i + 1)) > 0):
            if between_target(x, y, (x - (i + 1)), (y - (i + 1))):
                break
            elif target((x - (i + 1)), (y - (i + 1)), 'white'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = (x - (i + 1))
                x_position = new_x - 1
                position = x_position + (((y - (i + 1)) - 1) * 8)
                new_bp[position] = 'B'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))


def add_dark_pawns(num):
    x = ((num % 8) + 1)
    y = y_coordinate(num + 1)
    global moves_on_board
    global new_bp
    if y == 7:
        if (9 > (y - 1) > 0) and pawn_move(x, (y - 1)):
            new_bp = list(bp)
            new_bp[num] = '0'
            new_y = y - 1
            x_position = x - 1
            position = x_position + ((new_y - 1) * 8)
            new_bp[position] = 'p'
            new_bp = str(new_bp)
            new_bp = new_bp.replace(' ', '')
            new_bp = new_bp.replace('[', '')
            new_bp = new_bp.replace(']', '')
            new_bp = new_bp.replace(',', '')
            new_bp = new_bp.replace("'", '')
            moves_on_board.append(str(new_bp))
        if 9 > (y - 2) > 0:
            if pawn_move(x, (y - 1)) and pawn_move(x, (y - 2)):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_y = y - 2
                x_position = x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'p'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
        if (9 > (y - 1) > 0) and (9 > (x - 1) > 0):
            if pawn_target((x - 1), (y - 1), 'black'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = x - 1
                new_y = y - 1
                x_position = new_x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'p'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
        if (9 > (y - 1) > 0) and (9 > (x + 1) > 0):
            if pawn_target((x + 1), (y - 1), 'black'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = x + 1
                new_y = y - 1
                x_position = new_x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'p'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
    elif y == 2:
        if 9 > (y - 1) > 0:
            if pawn_move(x, (y - 1)):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_y = y - 1
                x_position = x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'n'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
                new_bp = list(bp)
                new_bp[num] = '0'
                new_y = y - 1
                x_position = x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'q'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
        if (9 > (y - 1) > 0) and (9 > (x - 1) > 0):
            if pawn_target((x - 1), (y - 1), 'black'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = x - 1
                new_y = y - 1
                x_position = new_x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'n'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = x - 1
                new_y = y - 1
                x_position = new_x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'q'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
        if (9 > (y - 1) > 0) and (9 > (x + 1) > 0):
            if pawn_target((x + 1), (y - 1), 'black'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = x + 1
                new_y = y - 1
                x_position = new_x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'n'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = x + 1
                new_y = y - 1
                x_position = new_x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'q'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
    else:
        if 9 > (y - 1) > 0:
            if pawn_move(x, (y - 1)):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_y = y - 1
                x_position = x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'p'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
        if (9 > (y - 1) > 0) and (9 > (x - 1) > 0):
            if pawn_target((x - 1), (y - 1), 'black'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = x - 1
                new_y = y - 1
                x_position = new_x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'p'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
        if (9 > (y - 1) > 0) and (9 > (x + 1) > 0):
            if pawn_target((x + 1), (y - 1), 'black'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = x + 1
                new_y = y - 1
                x_position = new_x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'p'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))


def add_light_pawns(num):
    x = ((num % 8) + 1)
    y = y_coordinate(num + 1)
    global moves_on_board
    global new_bp
    if y == 2:
        if 9 > (y + 1) > 0:
            if pawn_move(x, (y + 1)):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_y = y + 1
                x_position = x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'P'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
        if 9 > (y + 2) > 0:
            if pawn_move(x, (y + 1)) and pawn_move(x, (y + 2)):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_y = y + 2
                x_position = x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'P'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
        if (9 > (y + 1) > 0) and (9 > (x - 1) > 0):
            if pawn_target((x - 1), (y + 1), 'white'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = x - 1
                new_y = y + 1
                x_position = new_x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'P'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
        if (9 > (y + 1) > 0) and (9 > (x + 1) > 0):
            if pawn_target((x + 1), (y + 1), 'white'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = x + 1
                new_y = y + 1
                x_position = new_x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'P'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
    elif y == 7:
        if 9 > (y + 1) > 0:
            if pawn_move(x, (y + 1)):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_y = y + 1
                x_position = x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'N'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
                new_bp = list(bp)
                new_bp[num] = '0'
                new_y = y + 1
                x_position = x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'Q'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
        if (9 > (y + 1) > 0) and (9 > (x - 1) > 0):
            if pawn_target((x - 1), (y + 1), 'white'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = x - 1
                new_y = y + 1
                x_position = new_x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'N'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = x - 1
                new_y = y + 1
                x_position = new_x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'Q'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
        if (9 > (y + 1) > 0) and (9 > (x + 1) > 0):
            if pawn_target((x + 1), (y + 1), 'white'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = x + 1
                new_y = y + 1
                x_position = new_x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'N'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = x + 1
                new_y = y + 1
                x_position = new_x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'Q'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
    else:
        if 9 > (y + 1) > 0:
            if pawn_move(x, (y + 1)):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_y = y + 1
                x_position = x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'P'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
        if (9 > (y + 1) > 0) and (9 > (x - 1) > 0):
            if pawn_target((x - 1), (y + 1), 'white'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = x - 1
                new_y = y + 1
                x_position = new_x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'P'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
        if (9 > (y + 1) > 0) and (9 > (x + 1) > 0):
            if pawn_target((x + 1), (y + 1), 'white'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = x + 1
                new_y = y + 1
                x_position = new_x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'P'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))


def add_dark_kings(num):
    x = ((num % 8) + 1)
    y = y_coordinate(num + 1)
    global moves_on_board
    global new_bp
    if 9 > (x + 1) > 0:
        if target((x + 1), y, 'black'):
            new_bp = list(bp)
            new_bp[num] = '0'
            new_x = (x + 1)
            x_position = new_x - 1
            position = x_position + ((y - 1) * 8)
            new_bp[position] = 'k'
            new_bp = str(new_bp)
            new_bp = new_bp.replace(' ', '')
            new_bp = new_bp.replace('[', '')
            new_bp = new_bp.replace(']', '')
            new_bp = new_bp.replace(',', '')
            new_bp = new_bp.replace("'", '')
            moves_on_board.append(str(new_bp))
    if 9 > (x - 1) > 0:
        if target((x - 1), y, 'black'):
            new_bp = list(bp)
            new_bp[num] = '0'
            new_x = (x - 1)
            x_position = new_x - 1
            position = x_position + ((y - 1) * 8)
            new_bp[position] = 'k'
            new_bp = str(new_bp)
            new_bp = new_bp.replace(' ', '')
            new_bp = new_bp.replace('[', '')
            new_bp = new_bp.replace(']', '')
            new_bp = new_bp.replace(',', '')
            new_bp = new_bp.replace("'", '')
            moves_on_board.append(str(new_bp))
    if 9 > (y + 1) > 0:
        if target(x, (y + 1), 'black'):
            new_bp = list(bp)
            new_bp[num] = '0'
            new_y = (y + 1)
            x_position = x - 1
            position = x_position + ((new_y - 1) * 8)
            new_bp[position] = 'k'
            new_bp = str(new_bp)
            new_bp = new_bp.replace(' ', '')
            new_bp = new_bp.replace('[', '')
            new_bp = new_bp.replace(']', '')
            new_bp = new_bp.replace(',', '')
            new_bp = new_bp.replace("'", '')
            moves_on_board.append(str(new_bp))
    if 9 > (y - 1) > 0:
        if target(x, (y - 1), 'black'):
            new_bp = list(bp)
            new_bp[num] = '0'
            new_y = (y - 1)
            x_position = x - 1
            position = x_position + ((new_y - 1) * 8)
            new_bp[position] = 'k'
            new_bp = str(new_bp)
            new_bp = new_bp.replace(' ', '')
            new_bp = new_bp.replace('[', '')
            new_bp = new_bp.replace(']', '')
            new_bp = new_bp.replace(',', '')
            new_bp = new_bp.replace("'", '')
            moves_on_board.append(str(new_bp))
    if (9 > (x + 1) > 0) and (9 > (y + 1) > 0):
        if target((x + 1), (y + 1), 'black'):
            new_bp = list(bp)
            new_bp[num] = '0'
            new_x = (x + 1)
            new_y = (y + 1)
            x_position = new_x - 1
            position = x_position + ((new_y - 1) * 8)
            new_bp[position] = 'k'
            new_bp = str(new_bp)
            new_bp = new_bp.replace(' ', '')
            new_bp = new_bp.replace('[', '')
            new_bp = new_bp.replace(']', '')
            new_bp = new_bp.replace(',', '')
            new_bp = new_bp.replace("'", '')
            moves_on_board.append(str(new_bp))
    if (9 > (x - 1) > 0) and (9 > (y + 1) > 0):
        if target((x - 1), (y + 1), 'black'):
            new_bp = list(bp)
            new_bp[num] = '0'
            new_x = (x - 1)
            new_y = (y + 1)
            x_position = new_x - 1
            position = x_position + ((new_y - 1) * 8)
            new_bp[position] = 'k'
            new_bp = str(new_bp)
            new_bp = new_bp.replace(' ', '')
            new_bp = new_bp.replace('[', '')
            new_bp = new_bp.replace(']', '')
            new_bp = new_bp.replace(',', '')
            new_bp = new_bp.replace("'", '')
            moves_on_board.append(str(new_bp))
    if (9 > (x - 1) > 0) and (9 > (y - 1) > 0):
        if target((x - 1), (y - 1), 'black'):
            new_bp = list(bp)
            new_bp[num] = '0'
            new_x = (x - 1)
            new_y = (y - 1)
            x_position = new_x - 1
            position = x_position + ((new_y - 1) * 8)
            new_bp[position] = 'k'
            new_bp = str(new_bp)
            new_bp = new_bp.replace(' ', '')
            new_bp = new_bp.replace('[', '')
            new_bp = new_bp.replace(']', '')
            new_bp = new_bp.replace(',', '')
            new_bp = new_bp.replace("'", '')
            moves_on_board.append(str(new_bp))
    if (9 > (x + 1) > 0) and (9 > (y - 1) > 0):
        if target((x + 1), (y - 1), 'black'):
            new_bp = list(bp)
            new_bp[num] = '0'
            new_x = (x + 1)
            new_y = (y - 1)
            x_position = new_x - 1
            position = x_position + ((new_y - 1) * 8)
            new_bp[position] = 'k'
            new_bp = str(new_bp)
            new_bp = new_bp.replace(' ', '')
            new_bp = new_bp.replace('[', '')
            new_bp = new_bp.replace(']', '')
            new_bp = new_bp.replace(',', '')
            new_bp = new_bp.replace("'", '')
            moves_on_board.append(str(new_bp))


def add_light_kings(num):
    x = ((num % 8) + 1)
    y = y_coordinate(num + 1)
    global moves_on_board
    global new_bp
    if 9 > (x + 1) > 0:
        if target((x + 1), y, 'white'):
            new_bp = list(bp)
            new_bp[num] = '0'
            new_x = (x + 1)
            x_position = new_x - 1
            position = x_position + ((y - 1) * 8)
            new_bp[position] = 'K'
            new_bp = str(new_bp)
            new_bp = new_bp.replace(' ', '')
            new_bp = new_bp.replace('[', '')
            new_bp = new_bp.replace(']', '')
            new_bp = new_bp.replace(',', '')
            new_bp = new_bp.replace("'", '')
            moves_on_board.append(str(new_bp))
    if 9 > (x - 1) > 0:
        if target((x - 1), y, 'white'):
            new_bp = list(bp)
            new_bp[num] = '0'
            new_x = (x - 1)
            x_position = new_x - 1
            position = x_position + ((y - 1) * 8)
            new_bp[position] = 'K'
            new_bp = str(new_bp)
            new_bp = new_bp.replace(' ', '')
            new_bp = new_bp.replace('[', '')
            new_bp = new_bp.replace(']', '')
            new_bp = new_bp.replace(',', '')
            new_bp = new_bp.replace("'", '')
            moves_on_board.append(str(new_bp))
    if 9 > (y + 1) > 0:
        if target(x, (y + 1), 'white'):
            new_bp = list(bp)
            new_bp[num] = '0'
            new_y = (y + 1)
            x_position = x - 1
            position = x_position + ((new_y - 1) * 8)
            new_bp[position] = 'K'
            new_bp = str(new_bp)
            new_bp = new_bp.replace(' ', '')
            new_bp = new_bp.replace('[', '')
            new_bp = new_bp.replace(']', '')
            new_bp = new_bp.replace(',', '')
            new_bp = new_bp.replace("'", '')
            moves_on_board.append(str(new_bp))
    if 9 > (y - 1) > 0:
        if target(x, (y - 1), 'white'):
            new_bp = list(bp)
            new_bp[num] = '0'
            new_y = (y - 1)
            x_position = x - 1
            position = x_position + ((new_y - 1) * 8)
            new_bp[position] = 'K'
            new_bp = str(new_bp)
            new_bp = new_bp.replace(' ', '')
            new_bp = new_bp.replace('[', '')
            new_bp = new_bp.replace(']', '')
            new_bp = new_bp.replace(',', '')
            new_bp = new_bp.replace("'", '')
            moves_on_board.append(str(new_bp))
    if (9 > (x + 1) > 0) and (9 > (y + 1) > 0):
        if target((x + 1), (y + 1), 'white'):
            new_bp = list(bp)
            new_bp[num] = '0'
            new_x = (x + 1)
            new_y = (y + 1)
            x_position = new_x - 1
            position = x_position + ((new_y - 1) * 8)
            new_bp[position] = 'K'
            new_bp = str(new_bp)
            new_bp = new_bp.replace(' ', '')
            new_bp = new_bp.replace('[', '')
            new_bp = new_bp.replace(']', '')
            new_bp = new_bp.replace(',', '')
            new_bp = new_bp.replace("'", '')
            moves_on_board.append(str(new_bp))
    if (9 > (x - 1) > 0) and (9 > (y + 1) > 0):
        if target((x - 1), (y + 1), 'white'):
            new_bp = list(bp)
            new_bp[num] = '0'
            new_x = (x - 1)
            new_y = (y + 1)
            x_position = new_x - 1
            position = x_position + ((new_y - 1) * 8)
            new_bp[position] = 'K'
            new_bp = str(new_bp)
            new_bp = new_bp.replace(' ', '')
            new_bp = new_bp.replace('[', '')
            new_bp = new_bp.replace(']', '')
            new_bp = new_bp.replace(',', '')
            new_bp = new_bp.replace("'", '')
            moves_on_board.append(str(new_bp))
    if (9 > (x - 1) > 0) and (9 > (y - 1) > 0):
        if target((x - 1), (y - 1), 'white'):
            new_bp = list(bp)
            new_bp[num] = '0'
            new_x = (x - 1)
            new_y = (y - 1)
            x_position = new_x - 1
            position = x_position + ((new_y - 1) * 8)
            new_bp[position] = 'K'
            new_bp = str(new_bp)
            new_bp = new_bp.replace(' ', '')
            new_bp = new_bp.replace('[', '')
            new_bp = new_bp.replace(']', '')
            new_bp = new_bp.replace(',', '')
            new_bp = new_bp.replace("'", '')
            moves_on_board.append(str(new_bp))
    if (9 > (x + 1) > 0) and (9 > (y - 1) > 0):
        if target((x + 1), (y - 1), 'white'):
            new_bp = list(bp)
            new_bp[num] = '0'
            new_x = (x + 1)
            new_y = (y - 1)
            x_position = new_x - 1
            position = x_position + ((new_y - 1) * 8)
            new_bp[position] = 'K'
            new_bp = str(new_bp)
            new_bp = new_bp.replace(' ', '')
            new_bp = new_bp.replace('[', '')
            new_bp = new_bp.replace(']', '')
            new_bp = new_bp.replace(',', '')
            new_bp = new_bp.replace("'", '')
            moves_on_board.append(str(new_bp))


def add_dark_queens(num):
    x = ((num % 8) + 1)
    y = y_coordinate(num + 1)
    global new_bp
    for i in range(7):
        if 9 > (x + (i + 1)) > 0:
            if between_target(x, y, (x + (i + 1)), y):
                break
            elif target((x + (i + 1)), y, 'black'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = (x + (i + 1))
                x_position = new_x - 1
                position = x_position + ((y - 1) * 8)
                new_bp[position] = 'q'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
    for i in range(7):
        if 9 > (x - (i + 1)) > 0:
            if between_target(x, y, (x - (i + 1)), y):
                break
            elif target((x - (i + 1)), y, 'black'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = (x - (i + 1))
                x_position = new_x - 1
                position = x_position + ((y - 1) * 8)
                new_bp[position] = 'q'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
    for i in range(7):
        if 9 > (y + (i + 1)) > 0:
            if between_target(x, y, x, (y + (i + 1))):
                break
            elif target(x, (y + (i + 1)), 'black'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_y = (y + (i + 1))
                x_position = x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'q'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
    for i in range(7):
        if 9 > (y - (i + 1)) > 0:
            if between_target(x, y, x, (y - (i + 1))):
                break
            elif target(x, (y - (i + 1)), 'black'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_y = (y - (i + 1))
                x_position = x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'q'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
    for i in range(7):
        if (9 > (x + (i + 1)) > 0) and (9 > (y + (i + 1)) > 0):
            if between_target(x, y, (x + (i + 1)), (y + (i + 1))):
                break
            elif target((x + (i + 1)), (y + (i + 1)), 'black'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = (x + (i + 1))
                x_position = new_x - 1
                position = x_position + (((y + (i + 1)) - 1) * 8)
                new_bp[position] = 'q'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
    for i in range(7):
        if (9 > (x - (i + 1)) > 0) and (9 > (y + (i + 1)) > 0):
            if between_target(x, y, (x - (i + 1)), (y + (i + 1))):
                break
            elif target((x - (i + 1)), (y + (i + 1)), 'black'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = (x - (i + 1))
                x_position = new_x - 1
                position = x_position + (((y + (i + 1)) - 1) * 8)
                new_bp[position] = 'q'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
    for i in range(7):
        if (9 > (x + (i + 1)) > 0) and (9 > (y - (i + 1)) > 0):
            if between_target(x, y, (x + (i + 1)), (y - (i + 1))):
                break
            elif target((x + (i + 1)), (y - (i + 1)), 'black'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = (x + (i + 1))
                x_position = new_x - 1
                position = x_position + (((y - (i + 1)) - 1) * 8)
                new_bp[position] = 'q'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
    for i in range(7):
        if (9 > (x - (i + 1)) > 0) and (9 > (y - (i + 1)) > 0):
            if between_target(x, y, (x - (i + 1)), (y - (i + 1))):
                break
            elif target((x - (i + 1)), (y - (i + 1)), 'black'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = (x - (i + 1))
                x_position = new_x - 1
                position = x_position + (((y - (i + 1)) - 1) * 8)
                new_bp[position] = 'q'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))


def add_light_queens(num):
    x = ((num % 8) + 1)
    y = y_coordinate(num + 1)
    global new_bp
    for i in range(7):
        if 9 > (x + (i + 1)) > 0:
            if between_target(x, y, (x + (i + 1)), y):
                break
            elif target((x + (i + 1)), y, 'white'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = (x + (i + 1))
                x_position = new_x - 1
                position = x_position + ((y - 1) * 8)
                new_bp[position] = 'Q'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
    for i in range(7):
        if 9 > (x - (i + 1)) > 0:
            if between_target(x, y, (x - (i + 1)), y):
                break
            elif target((x - (i + 1)), y, 'white'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = (x - (i + 1))
                x_position = new_x - 1
                position = x_position + ((y - 1) * 8)
                new_bp[position] = 'Q'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
    for i in range(7):
        if 9 > (y + (i + 1)) > 0:
            if between_target(x, y, x, (y + (i + 1))):
                break
            elif target(x, (y + (i + 1)), 'white'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_y = (y + (i + 1))
                x_position = x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'Q'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
    for i in range(7):
        if 9 > (y - (i + 1)) > 0:
            if between_target(x, y, x, (y - (i + 1))):
                break
            elif target(x, (y - (i + 1)), 'white'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_y = (y - (i + 1))
                x_position = x - 1
                position = x_position + ((new_y - 1) * 8)
                new_bp[position] = 'Q'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
    for i in range(7):
        if (9 > (x + (i + 1)) > 0) and (9 > (y + (i + 1)) > 0):
            if between_target(x, y, (x + (i + 1)), (y + (i + 1))):
                break
            elif target((x + (i + 1)), (y + (i + 1)), 'white'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = (x + (i + 1))
                x_position = new_x - 1
                position = x_position + (((y + (i + 1)) - 1) * 8)
                new_bp[position] = 'Q'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
    for i in range(7):
        if (9 > (x - (i + 1)) > 0) and (9 > (y + (i + 1)) > 0):
            if between_target(x, y, (x - (i + 1)), (y + (i + 1))):
                break
            elif target((x - (i + 1)), (y + (i + 1)), 'white'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = (x - (i + 1))
                x_position = new_x - 1
                position = x_position + (((y + (i + 1)) - 1) * 8)
                new_bp[position] = 'Q'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
    for i in range(7):
        if (9 > (x + (i + 1)) > 0) and (9 > (y - (i + 1)) > 0):
            if between_target(x, y, (x + (i + 1)), (y - (i + 1))):
                break
            elif target((x + (i + 1)), (y - (i + 1)), 'white'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = (x + (i + 1))
                x_position = new_x - 1
                position = x_position + (((y - (i + 1)) - 1) * 8)
                new_bp[position] = 'Q'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))
    for i in range(7):
        if (9 > (x - (i + 1)) > 0) and (9 > (y - (i + 1)) > 0):
            if between_target(x, y, (x - (i + 1)), (y - (i + 1))):
                break
            elif target((x - (i + 1)), (y - (i + 1)), 'white'):
                new_bp = list(bp)
                new_bp[num] = '0'
                new_x = (x - (i + 1))
                x_position = new_x - 1
                position = x_position + (((y - (i + 1)) - 1) * 8)
                new_bp[position] = 'Q'
                new_bp = str(new_bp)
                new_bp = new_bp.replace(' ', '')
                new_bp = new_bp.replace('[', '')
                new_bp = new_bp.replace(']', '')
                new_bp = new_bp.replace(',', '')
                new_bp = new_bp.replace("'", '')
                moves_on_board.append(str(new_bp))


####################################################################################
# TARGETING FUNCTIONS
####################################################################################

# needs to return true if nothing is in between


def between_target(x1, y1, x2, y2):
    global bp
    x_difference = abs(x2 - x1) - 1
    y_difference = abs(y2 - y1) - 1
    if (x1 != x2) and (y1 == y2):
        if x_difference == 0:
            return False
        else:
            if x2 > x1:
                for i in range(x_difference):
                    if not check_board(bp, (x1 + (i + 1)), y1, '0'):
                        break
                    elif check_board(bp, (x1 + (i + 1)), y1, '0') and ((i + 1) == x_difference):
                        return False
                return True
            if x2 < x1:
                for i in range(x_difference):
                    if not check_board(bp, (x2 + (i + 1)), y1, '0'):
                        break
                    elif check_board(bp, (x2 + (i + 1)), y1, '0') and ((i + 1) == x_difference):
                        return False
                return True
    elif (x1 == x2) and (y1 != y2):
        if y_difference == 0:
            return False
        else:
            if y2 > y1:
                for i in range(y_difference):
                    if not check_board(bp, x1, (y1 + (i + 1)), '0'):
                        break
                    elif check_board(bp, x1, (y1 + (i + 1)), '0') and ((i + 1) == y_difference):
                        return False
                return True
            if y2 < y1:
                for i in range(y_difference):
                    if not check_board(bp, x1, (y1 - (i + 1)), '0'):
                        break
                    elif check_board(bp, x1, (y1 - (i + 1)), '0') and ((i + 1) == y_difference):
                        return False
                return True
    elif (x1 != x2) and (y1 != y2):
        if x_difference == 0:
            return False
        else:
            if (x2 > x1) and (y2 > y1):
                for i in range(x_difference):
                    if not check_board(bp, (x1 + (i + 1)), (y1 + (i + 1)), '0'):
                        break
                    elif check_board(bp, (x1 + (i + 1)), (y1 + (i + 1)), '0') and ((i + 1) == x_difference):
                        return False
                return True
            elif (x2 < x1) and (y2 > y1):
                for i in range(x_difference):
                    if not check_board(bp, (x1 - (i + 1)), (y1 + (i + 1)), '0'):
                        break
                    elif check_board(bp, (x1 - (i + 1)), (y1 + (i + 1)), '0') and ((i + 1) == x_difference):
                        return False
                return True
            elif (x2 > x1) and (y2 < y1):
                for i in range(x_difference):
                    if not check_board(bp, (x1 + (i + 1)), (y1 - (i + 1)), '0'):
                        break
                    elif check_board(bp, (x1 + (i + 1)), (y1 - (i + 1)), '0') and ((i + 1) == x_difference):
                        return False
                return True
            elif (x2 < x1) and (y2 < y1):
                for i in range(x_difference):
                    if not check_board(bp, (x1 - (i + 1)), (y1 - (i + 1)), '0'):
                        break
                    elif check_board(bp, (x1 - (i + 1)), (y1 - (i + 1)), '0') and ((i + 1) == x_difference):
                        return False
                return True


def target(x, y, color):
    if color == 'white':
        if check_board(bp, x, y, 'r'):
            return True
        elif check_board(bp, x, y, 'n'):
            return True
        elif check_board(bp, x, y, 'b'):
            return True
        elif check_board(bp, x, y, 'p'):
            return True
        elif check_board(bp, x, y, 'k'):
            return True
        elif check_board(bp, x, y, 'q'):
            return True
        elif check_board(bp, x, y, '0'):
            return True
        else:
            return False
    elif color == 'black':
        if check_board(bp, x, y, 'R'):
            return True
        elif check_board(bp, x, y, 'N'):
            return True
        elif check_board(bp, x, y, 'B'):
            return True
        elif check_board(bp, x, y, 'P'):
            return True
        elif check_board(bp, x, y, 'K'):
            return True
        elif check_board(bp, x, y, 'Q'):
            return True
        elif check_board(bp, x, y, '0'):
            return True
        else:
            return False


def pawn_target(x, y, color):
    if color == 'white':
        if check_board(bp, x, y, 'r'):
            return True
        elif check_board(bp, x, y, 'n'):
            return True
        elif check_board(bp, x, y, 'b'):
            return True
        elif check_board(bp, x, y, 'p'):
            return True
        elif check_board(bp, x, y, 'k'):
            return True
        elif check_board(bp, x, y, 'q'):
            return True
        else:
            return False
    elif color == 'black':
        if check_board(bp, x, y, 'R'):
            return True
        elif check_board(bp, x, y, 'N'):
            return True
        elif check_board(bp, x, y, 'B'):
            return True
        elif check_board(bp, x, y, 'P'):
            return True
        elif check_board(bp, x, y, 'K'):
            return True
        elif check_board(bp, x, y, 'Q'):
            return True
        else:
            return False


def pawn_move(x, y):
    if check_board(bp, x, y, '0'):
        return True
    else:
        return False


####################################################################################
# CHECK ATTACK FUNCTIONS
####################################################################################


def check_rook_attack(board, x, y, color):
    if color == 'white':
        for i in range(7):
            if 9 > (x + (i + 1)) > 0:
                if check_board(board, (x + (i + 1)), y, 'r'):
                    return True
                elif check_board(board, (x + (i + 1)), y, '0'):
                    continue
                else:
                    break
        for i in range(7):
            if 9 > (x - (i + 1)) > 0:
                if check_board(board, (x - (i + 1)), y, 'r'):
                    return True
                elif check_board(board, (x - (i + 1)), y, '0'):
                    continue
                else:
                    break
        for i in range(7):
            if 9 > (y + (i + 1)) > 0:
                if check_board(board, x, (y + (i + 1)), 'r'):
                    return True
                elif check_board(board, x, (y + (i + 1)), '0'):
                    continue
                else:
                    break
        for i in range(7):
            if 9 > (y - (i + 1)) > 0:
                if check_board(board, x, (y - (i + 1)), 'r'):
                    return True
                elif check_board(board, x, (y - (i + 1)), '0'):
                    continue
                else:
                    break
    elif color == 'black':
        for i in range(7):
            if 9 > (x + (i + 1)) > 0:
                if check_board(board, (x + (i + 1)), y, 'R'):
                    return True
                elif check_board(board, (x + (i + 1)), y, '0'):
                    continue
                else:
                    break
        for i in range(7):
            if 9 > (x - (i + 1)) > 0:
                if check_board(board, (x - (i + 1)), y, 'R'):
                    return True
                elif check_board(board, (x - (i + 1)), y, '0'):
                    continue
                else:
                    break
        for i in range(7):
            if 9 > (y + (i + 1)) > 0:
                if check_board(board, x, (y + (i + 1)), 'R'):
                    return True
                elif check_board(board, x, (y + (i + 1)), '0'):
                    continue
                else:
                    break
        for i in range(7):
            if 9 > (y - (i + 1)) > 0:
                if check_board(board, x, (y - (i + 1)), 'R'):
                    return True
                elif check_board(board, x, (y - (i + 1)), '0'):
                    continue
                else:
                    break


def check_knight_attack(board, x, y, color):
    if color == 'white':
        if (9 > (x + 1) > 0) and (9 > (y + 2) > 0):
            if check_board(board, (x + 1), (y + 2), 'n'):
                return True
        if (9 > (x + 1) > 0) and (9 > (y - 2) > 0):
            if check_board(board, (x + 1), (y - 2), 'n'):
                return True
        if (9 > (x - 1) > 0) and (9 > (y + 2) > 0):
            if check_board(board, (x - 1), (y + 2), 'n'):
                return True
        if (9 > (x - 1) > 0) and (9 > (y - 2) > 0):
            if check_board(board, (x - 1), (y - 2), 'n'):
                return True
        if (9 > (x + 2) > 0) and (9 > (y + 1) > 0):
            if check_board(board, (x + 2), (y + 1), 'n'):
                return True
        if (9 > (x + 2) > 0) and (9 > (y - 1) > 0):
            if check_board(board, (x + 2), (y - 1), 'n'):
                return True
        if (9 > (x - 2) > 0) and (9 > (y + 1) > 0):
            if check_board(board, (x - 2), (y + 1), 'n'):
                return True
        if (9 > (x - 2) > 0) and (9 > (y - 1) > 0):
            if check_board(board, (x - 2), (y - 1), 'n'):
                return True
    elif color == 'black':
        if (9 > (x + 1) > 0) and (9 > (y + 2) > 0):
            if check_board(board, (x + 1), (y + 2), 'N'):
                return True
        if (9 > (x + 1) > 0) and (9 > (y - 2) > 0):
            if check_board(board, (x + 1), (y - 2), 'N'):
                return True
        if (9 > (x - 1) > 0) and (9 > (y + 2) > 0):
            if check_board(board, (x - 1), (y + 2), 'N'):
                return True
        if (9 > (x - 1) > 0) and (9 > (y - 2) > 0):
            if check_board(board, (x - 1), (y - 2), 'N'):
                return True
        if (9 > (x + 2) > 0) and (9 > (y + 1) > 0):
            if check_board(board, (x + 2), (y + 1), 'N'):
                return True
        if (9 > (x + 2) > 0) and (9 > (y - 1) > 0):
            if check_board(board, (x + 2), (y - 1), 'N'):
                return True
        if (9 > (x - 2) > 0) and (9 > (y + 1) > 0):
            if check_board(board, (x - 2), (y + 1), 'N'):
                return True
        if (9 > (x - 2) > 0) and (9 > (y - 1) > 0):
            if check_board(board, (x - 2), (y - 1), 'N'):
                return True
    return False


def check_byshop_attack(board, x, y, color):
    if color == 'white':
        for i in range(7):
            if (9 > (x + (i + 1)) > 0) and (9 > (y + (i + 1)) > 0):
                if check_board(board, (x + (i + 1)), (y + (i + 1)), 'b'):
                    return True
                elif check_board(board, (x + (i + 1)), (y + (i + 1)), '0'):
                    continue
                else:
                    break
        for i in range(7):
            if (9 > (x + (i + 1)) > 0) and (9 > (y - (i + 1)) > 0):
                if check_board(board, (x + (i + 1)), (y - (i + 1)), 'b'):
                    return True
                elif check_board(board, (x + (i + 1)), (y - (i + 1)), '0'):
                    continue
                else:
                    break
        for i in range(7):
            if (9 > (x - (i + 1)) > 0) and (9 > (y + (i + 1)) > 0):
                if check_board(board, (x - (i + 1)), (y + (i + 1)), 'b'):
                    return True
                elif check_board(board, (x - (i + 1)), (y + (i + 1)), '0'):
                    continue
                else:
                    break
        for i in range(7):
            if (9 > (x - (i + 1)) > 0) and (9 > (y - (i + 1)) > 0):
                if check_board(board, (x - (i + 1)), (y - (i + 1)), 'b'):
                    return True
                elif check_board(board, (x - (i + 1)), (y - (i + 1)), '0'):
                    continue
                else:
                    break
    elif color == 'black':
        for i in range(7):
            if (9 > (x + (i + 1)) > 0) and (9 > (y + (i + 1)) > 0):
                if check_board(board, (x + (i + 1)), (y + (i + 1)), 'B'):
                    return True
                elif check_board(board, (x + (i + 1)), (y + (i + 1)), '0'):
                    continue
                else:
                    break
        for i in range(7):
            if (9 > (x + (i + 1)) > 0) and (9 > (y - (i + 1)) > 0):
                if check_board(board, (x + (i + 1)), (y - (i + 1)), 'B'):
                    return True
                elif check_board(board, (x + (i + 1)), (y - (i + 1)), '0'):
                    continue
                else:
                    break
        for i in range(7):
            if (9 > (x - (i + 1)) > 0) and (9 > (y + (i + 1)) > 0):
                if check_board(board, (x - (i + 1)), (y + (i + 1)), 'B'):
                    return True
                elif check_board(board, (x - (i + 1)), (y + (i + 1)), '0'):
                    continue
                else:
                    break
        for i in range(7):
            if (9 > (x - (i + 1)) > 0) and (9 > (y - (i + 1)) > 0):
                if check_board(board, (x - (i + 1)), (y - (i + 1)), 'B'):
                    return True
                elif check_board(board, (x - (i + 1)), (y - (i + 1)), '0'):
                    continue
                else:
                    break


def check_pawn_attack(board, x, y, color):
    if color == 'white':
        if (9 > (x + 1) > 0) and (9 > (y + 1) > 0):
            if check_board(board, (x + 1), (y + 1), 'p'):
                return True
        if (9 > (x - 1) > 0) and (9 > (y + 1) > 0):
            if check_board(board, (x - 1), (y + 1), 'p'):
                return True
    elif color == 'black':
        if (9 > (x + 1) > 0) and (9 > (y - 1) > 0):
            if check_board(board, (x + 1), (y - 1), 'P'):
                return True
        if (9 > (x - 1) > 0) and (9 > (y - 1) > 0):
            if check_board(board, (x - 1), (y - 1), 'P'):
                return True


def check_queen_attack(board, x, y, color):
    if color == 'white':
        for i in range(7):
            if 9 > (x + (i + 1)) > 0:
                if check_board(board, (x + (i + 1)), y, 'q'):
                    return True
                elif check_board(board, (x + (i + 1)), y, '0'):
                    continue
                else:
                    break
        for i in range(7):
            if 9 > (x - (i + 1)) > 0:
                if check_board(board, (x - (i + 1)), y, 'q'):
                    return True
                elif check_board(board, (x - (i + 1)), y, '0'):
                    continue
                else:
                    break
        for i in range(7):
            if 9 > (y + (i + 1)) > 0:
                if check_board(board, x, (y + (i + 1)), 'q'):
                    return True
                elif check_board(board, x, (y + (i + 1)), '0'):
                    continue
                else:
                    break
        for i in range(7):
            if 9 > (y - (i + 1)) > 0:
                if check_board(board, x, (y - (i + 1)), 'q'):
                    return True
                elif check_board(board, x, (y - (i + 1)), '0'):
                    continue
                else:
                    break
        for i in range(7):
            if (9 > (x + (i + 1)) > 0) and (9 > (y + (i + 1)) > 0):
                if check_board(board, (x + (i + 1)), (y + (i + 1)), 'q'):
                    return True
                elif check_board(board, (x + (i + 1)), (y + (i + 1)), '0'):
                    continue
                else:
                    break
        for i in range(7):
            if (9 > (x + (i + 1)) > 0) and (9 > (y - (i + 1)) > 0):
                if check_board(board, (x + (i + 1)), (y - (i + 1)), 'q'):
                    return True
                elif check_board(board, (x + (i + 1)), (y - (i + 1)), '0'):
                    continue
                else:
                    break
        for i in range(7):
            if (9 > (x - (i + 1)) > 0) and (9 > (y + (i + 1)) > 0):
                if check_board(board, (x - (i + 1)), (y + (i + 1)), 'q'):
                    return True
                elif check_board(board, (x - (i + 1)), (y + (i + 1)), '0'):
                    continue
                else:
                    break
        for i in range(7):
            if (9 > (x - (i + 1)) > 0) and (9 > (y - (i + 1)) > 0):
                if check_board(board, (x - (i + 1)), (y - (i + 1)), 'q'):
                    return True
                elif check_board(board, (x - (i + 1)), (y - (i + 1)), '0'):
                    continue
                else:
                    break
    elif color == 'black':
        for i in range(7):
            if 9 > (x + (i + 1)) > 0:
                if check_board(board, (x + (i + 1)), y, 'Q'):
                    return True
                elif check_board(board, (x + (i + 1)), y, '0'):
                    continue
                else:
                    break
        for i in range(7):
            if 9 > (x - (i + 1)) > 0:
                if check_board(board, (x - (i + 1)), y, 'Q'):
                    return True
                elif check_board(board, (x - (i + 1)), y, '0'):
                    continue
                else:
                    break
        for i in range(7):
            if 9 > (y + (i + 1)) > 0:
                if check_board(board, x, (y + (i + 1)), 'Q'):
                    return True
                elif check_board(board, x, (y + (i + 1)), '0'):
                    continue
                else:
                    break
        for i in range(7):
            if 9 > (y - (i + 1)) > 0:
                if check_board(board, x, (y - (i + 1)), 'Q'):
                    return True
                elif check_board(board, x, (y - (i + 1)), '0'):
                    continue
                else:
                    break
        for i in range(7):
            if (9 > (x + (i + 1)) > 0) and (9 > (y + (i + 1)) > 0):
                if check_board(board, (x + (i + 1)), (y + (i + 1)), 'Q'):
                    return True
                elif check_board(board, (x + (i + 1)), (y + (i + 1)), '0'):
                    continue
                else:
                    break
        for i in range(7):
            if (9 > (x + (i + 1)) > 0) and (9 > (y - (i + 1)) > 0):
                if check_board(board, (x + (i + 1)), (y - (i + 1)), 'Q'):
                    return True
                elif check_board(board, (x + (i + 1)), (y - (i + 1)), '0'):
                    continue
                else:
                    break
        for i in range(7):
            if (9 > (x - (i + 1)) > 0) and (9 > (y + (i + 1)) > 0):
                if check_board(board, (x - (i + 1)), (y + (i + 1)), 'Q'):
                    return True
                elif check_board(board, (x - (i + 1)), (y + (i + 1)), '0'):
                    continue
                else:
                    break
        for i in range(7):
            if (9 > (x - (i + 1)) > 0) and (9 > (y - (i + 1)) > 0):
                if check_board(board, (x - (i + 1)), (y - (i + 1)), 'Q'):
                    return True
                elif check_board(board, (x - (i + 1)), (y - (i + 1)), '0'):
                    continue
                else:
                    break


####################################################################################
# CHECK KING FUNCTIONS
####################################################################################


def check_king(board, color):
    if color == 'white':
        for i in range(64):
            x = ((i % 8) + 1)
            y = y_coordinate(i + 1)
            if check_board(board, x, y, 'K'):
                if check_rook_attack(board, x, y, color):
                    return True
                elif check_knight_attack(board, x, y, color):
                    return True
                elif check_byshop_attack(board, x, y, color):
                    return True
                elif check_pawn_attack(board, x, y, color):
                    return True
                elif check_queen_attack(board, x, y, color):
                    return True
                else:
                    return False
    elif color == 'black':
        for i in range(64):
            x = ((i % 8) + 1)
            y = y_coordinate(i + 1)
            if check_board(board, x, y, 'k'):
                if check_rook_attack(board, x, y, color):
                    return True
                elif check_knight_attack(board, x, y, color):
                    return True
                elif check_byshop_attack(board, x, y, color):
                    return True
                elif check_pawn_attack(board, x, y, color):
                    return True
                elif check_queen_attack(board, x, y, color):
                    return True
                else:
                    return False


def check_square(board, x, y, color):
    if color == 'white':
        if check_rook_attack(board, x, y, color):
            return True
        elif check_knight_attack(board, x, y, color):
            return True
        elif check_byshop_attack(board, x, y, color):
            return True
        elif check_pawn_attack(board, x, y, color):
            return True
        elif check_queen_attack(board, x, y, color):
            return True
        else:
            return False
    elif color == 'black':
        if check_rook_attack(board, x, y, color):
            return True
        elif check_knight_attack(board, x, y, color):
            return True
        elif check_byshop_attack(board, x, y, color):
            return True
        elif check_pawn_attack(board, x, y, color):
            return True
        elif check_queen_attack(board, x, y, color):
            return True
        else:
            return False


def check_mate(board, color):
    if (len(moves_on_board) == 0) and (check_king(board, color)):
        return True
    else:
        return False


def check_stale(board, color):
    if (len(moves_on_board) == 0) and (check_king(board, color) is False):
        return True
    else:
        return False


####################################################################################
# MICRO FUNCTIONS
####################################################################################


def never_moved(num):
    global game_positions, bp
    if num == 0:
        for i in range(len(game_positions)):
            if game_positions[i] != '':
                if check_board(game_positions[i], 1, 1, 'R') and check_board(game_positions[i], 5, 1, 'K'):
                    if i == int(len(game_positions) - 1):
                        return True
                    continue
                else:
                    break
        return False
    elif num == 7:
        for i in range(len(game_positions)):
            if game_positions[i] != '':
                if check_board(game_positions[i], 8, 1, 'R') and check_board(game_positions[i], 5, 1, 'K'):
                    if i == int(len(game_positions) - 1):
                        return True
                    continue
                else:
                    break
        return False
    elif num == 56:
        for i in range(len(game_positions)):
            if game_positions[i] != '':
                if check_board(game_positions[i], 1, 8, 'r') and check_board(game_positions[i], 5, 8, 'k'):
                    if i == int(len(game_positions) - 1):
                        return True
                    continue
                else:
                    break
        return False
    elif num == 63:
        for i in range(len(game_positions)):
            if game_positions[i] != '':
                if check_board(game_positions[i], 8, 8, 'r') and check_board(game_positions[i], 5, 8, 'k'):
                    if i == int(len(game_positions) - 1):
                        return True
                    continue
                else:
                    break
        return False


def check_board(board, x, y, piece):
    num = x - 1
    num = num + ((y - 1) * 8)
    if board[num] == piece:
        return True
    else:
        return False


def get_moves_on_board(board, color):
    global moves_on_board
    global new_bp
    global bp
    bp = board
    moves_on_board = ['']
    moves_on_board.clear()
    # print('get moves on board color: ' + color)
    if color == 'black':
        for i in range(64):
            j = i + 1
            if board[i:j] == 'r':
                add_dark_rooks(i)
            elif board[i:j] == 'n':
                add_dark_knights(i)
            elif board[i:j] == 'b':
                add_dark_byshops(i)
            elif board[i:j] == 'p':
                add_dark_pawns(i)
            elif board[i:j] == 'k':
                add_dark_kings(i)
            elif board[i:j] == 'q':
                add_dark_queens(i)
    elif color == 'white':
        for i in range(64):
            j = i + 1
            if board[i:j] == 'R':
                add_light_rooks(i)
            elif board[i:j] == 'N':
                add_light_knights(i)
            elif board[i:j] == 'B':
                add_light_byshops(i)
            elif board[i:j] == 'P':
                add_light_pawns(i)
            elif board[i:j] == 'K':
                add_light_kings(i)
            elif board[i:j] == 'Q':
                add_light_queens(i)


def validate_moves_on_board(color):
    global moves_on_board
    len_of_moves = len(moves_on_board)
    i = 0
    while i < len_of_moves:
        if check_king(str(moves_on_board[i]), color):
            moves_on_board.remove(moves_on_board[i])
            len_of_moves -= 1
            continue
        i += 1


####################################################################################
# SUB FUNCTIONS
####################################################################################


def get_moves(color):
    global bp
    get_moves_on_board(bp, color)
    validate_moves_on_board(color)


def choose_move(color):
    global game_over, white_win, black_win, checkmate, stalemate, bp
    global best_white_wins, best_black_wins, moves_on_board
    best_move = ''
    for i in range(len(moves_on_board)):
        # print('loop is', i)
        # print('checkpoint 4', moves_on_board[i])
        file = bp_library + convert_name(moves_on_board[i])
        if not os.path.exists(file):
            p = open(bp_library + convert_name(moves_on_board[i]), "w")
            p.write('5\n5')
            p.close()
        p = open(bp_library + convert_name(moves_on_board[i]), "r")
        white_wins = p.readline()
        black_wins = p.readline()
        p.close()
        white_wins = white_wins[:-1]
        white_wins = int(white_wins)
        black_wins = int(black_wins)
        if best_move == '':
            best_move = moves_on_board[i]
            best_white_wins = white_wins
            best_black_wins = black_wins
        else:
            if color == 'white':
                if int(white_wins) > int(best_white_wins):
                    best_move = moves_on_board[i]
                    best_white_wins = white_wins
                    best_black_wins = black_wins
                elif (int(white_wins) >= int(best_white_wins)) and int(black_wins) < int(best_black_wins):
                    best_move = moves_on_board[i]
                    best_white_wins = white_wins
                    best_black_wins = black_wins
            elif color == 'black':
                if black_wins > best_black_wins:
                    best_move = moves_on_board[i]
                    best_white_wins = white_wins
                    best_black_wins = black_wins
                elif (int(black_wins) >= int(best_black_wins)) and (int(white_wins) < int(best_white_wins)):
                    best_move = moves_on_board[i]
                    best_white_wins = white_wins
                    best_black_wins = black_wins
    if (best_move == '') and check_king(bp, color) and (color == 'white'):
        # print('checkpoint #1')
        game_over = True
        white_win = False
        black_win = True
        checkmate = True
        stalemate = False
    elif (best_move == '') and check_king(bp, color) and (color == 'black'):
        # print('checkpoint #2')
        game_over = True
        white_win = True
        black_win = False
        checkmate = True
        stalemate = False
    elif best_move == '':
        # print('checkpoint #3')
        game_over = True
        white_win = False
        black_win = False
        checkmate = False
        stalemate = True
    return best_move


def move_piece(new_board, old_board):
    # print('moving piece')
    update_board(new_board, old_board)
    # time.sleep(3)


def get_input_bp(user_input):
    global bp
    if len(user_input) == 5:
        user_input = str(user_input)
        x1 = int(user_input[0])
        y1 = int(user_input[1])
        x2 = int(user_input[2])
        y2 = int(user_input[3])
        num1 = x1 - 1
        num1 = num1 + ((y1 - 1) * 8)
        num2 = x2 - 1
        num2 = num2 + ((y2 - 1) * 8)
        input_bp = list(bp)
        input_bp[num2] = str(user_input[4:5])
        input_bp[num1] = '0'
        input_bp = str(input_bp)
        input_bp = input_bp.replace(' ', '')
        input_bp = input_bp.replace('[', '')
        input_bp = input_bp.replace(']', '')
        input_bp = input_bp.replace(',', '')
        input_bp = input_bp.replace("'", '')
        print(str(len(input_bp)))
        print(str(input_bp))
        return input_bp
    else:
        user_input = str(user_input)
        x1 = int(user_input[0])
        y1 = int(user_input[1])
        x2 = int(user_input[2])
        y2 = int(user_input[3])
        if (x1 == 5) and (y1 == 1) and (x2 == 3) and (y2 == 1) and check_board(bp, x1, y1, 'K'):
            input_bp = list(bp)
            input_bp[0] = '0'
            input_bp[4] = '0'
            input_bp[2] = 'K'
            input_bp[3] = 'R'
            input_bp = str(input_bp)
            input_bp = input_bp.replace(' ', '')
            input_bp = input_bp.replace('[', '')
            input_bp = input_bp.replace(']', '')
            input_bp = input_bp.replace(',', '')
            input_bp = input_bp.replace("'", '')
            return input_bp
        elif (x1 == 5) and (y1 == 1) and (x2 == 7) and (y2 == 1) and check_board(bp, x1, y1, 'K'):
            input_bp = list(bp)
            input_bp[4] = '0'
            input_bp[7] = '0'
            input_bp[6] = 'K'
            input_bp[5] = 'R'
            input_bp = str(input_bp)
            input_bp = input_bp.replace(' ', '')
            input_bp = input_bp.replace('[', '')
            input_bp = input_bp.replace(']', '')
            input_bp = input_bp.replace(',', '')
            input_bp = input_bp.replace("'", '')
            return input_bp
        elif (x1 == 5) and (y1 == 8) and (x2 == 3) and (y2 == 8) and check_board(bp, x1, y1, 'k'):
            input_bp = list(bp)
            input_bp[56] = '0'
            input_bp[60] = '0'
            input_bp[58] = 'k'
            input_bp[59] = 'r'
            input_bp = str(input_bp)
            input_bp = input_bp.replace(' ', '')
            input_bp = input_bp.replace('[', '')
            input_bp = input_bp.replace(']', '')
            input_bp = input_bp.replace(',', '')
            input_bp = input_bp.replace("'", '')
            return input_bp
        elif (x1 == 5) and (y1 == 8) and (x2 == 7) and (y2 == 8) and check_board(bp, x1, y1, 'k'):
            input_bp = list(bp)
            input_bp[60] = '0'
            input_bp[63] = '0'
            input_bp[62] = 'k'
            input_bp[61] = 'r'
            input_bp = str(input_bp)
            input_bp = input_bp.replace(' ', '')
            input_bp = input_bp.replace('[', '')
            input_bp = input_bp.replace(']', '')
            input_bp = input_bp.replace(',', '')
            input_bp = input_bp.replace("'", '')
            return input_bp
        else:
            num1 = x1 - 1
            num1 = num1 + ((y1 - 1) * 8)
            num2 = x2 - 1
            num2 = num2 + ((y2 - 1) * 8)
            input_bp = list(bp)
            input_bp[num1] = '0'
            input_bp[num2] = str(bp[num1])
            input_bp = str(input_bp)
            input_bp = input_bp.replace(' ', '')
            input_bp = input_bp.replace('[', '')
            input_bp = input_bp.replace(']', '')
            input_bp = input_bp.replace(',', '')
            input_bp = input_bp.replace("'", '')
            return input_bp


def validate_move(user_input, color):
    get_moves(color)
    requested_bp = get_input_bp(user_input)
    for i in range(len(moves_on_board)):
        if requested_bp == moves_on_board[i]:
            return True
        elif (i + 1) == len(moves_on_board):
            return False


####################################################################################
# BASIC FUNCTIONS
####################################################################################


def end_no_save():
    if keyboard.is_pressed('esc'):
        # close application
        exit(00)


def end_save():
    global games_played, draw_games, white_games, black_games
    if keyboard.is_pressed('esc'):
        print('0 was pressed')
        print('saving progress')
        p = open(directory + 'training_records.txt', "r")
        line1 = p.readline()
        line2 = p.readline()
        line3 = p.readline()
        line4 = p.readline()
        p.close()
        line1 = int(line1[:-1])
        line2 = int(line2[:-1])
        line3 = int(line3[:-1])
        line4 = int(line4)
        line1 += games_played
        line2 += draw_games
        line3 += white_games
        line4 += black_games
        p = open(directory + 'training_records.txt', "w")
        p.write(str(line1) + '\n' + str(line2) + '\n' + str(line3) + '\n' + str(line4))
        p.close()
        p = open(directory + 'latest_records.txt', "w")
        p.write(str(games_played) + '\n' + str(draw_games) + '\n' + str(white_games) + '\n' + str(black_games))
        p.close()
        # close application
        exit(00)


def show_stats(moves):
    global white_win
    global black_win
    global checkmate
    global stalemate
    print('########################')
    print('GAME OVER')
    print('########################')
    print('Results:')
    if white_win:
        print('Winner: White')
        print('Loser : Black')
    elif black_win:
        print('Winner: Black')
        print('Loser : White')
    else:
        print('Draw :: Draw')
    if checkmate:
        print('Cause : Checkmate')
    elif stalemate:
        print('Cause : Stalemate')
    else:
        print('Cause : Move_Limit')
    print('Moves : ' + str(moves))
    print('########################')
    # time.sleep(15)


def convert_name(code):
    name = str(code)
    name = name.replace('0', '00')
    name = name.replace('R', '10')
    name = name.replace('r', '01')
    name = name.replace('N', '20')
    name = name.replace('n', '02')
    name = name.replace('B', '30')
    name = name.replace('b', '03')
    name = name.replace('P', '40')
    name = name.replace('p', '04')
    name = name.replace('K', '50')
    name = name.replace('k', '05')
    name = name.replace('Q', '60')
    name = name.replace('q', '06')
    name = str(name) + '.txt'
    return name


def reverse_positions():
    global game_positions, reversed_positions
    reversed_positions = game_positions.copy()
    for i in range(len(reversed_positions)):
        if game_positions[i] != '':
            temp = list(game_positions[i])
            for j in range(64):
                if temp[j] != '0':
                    if temp[j].islower():
                        temp[j] = temp[j].upper()
                    elif temp[j].isupper():
                        temp[j] = temp[j].lower()
            temp = str(temp)
            temp = temp.replace(' ', '')
            temp = temp.replace('[', '')
            temp = temp.replace(']', '')
            temp = temp.replace(',', '')
            temp = temp.replace("'", '')
            reversed_positions[i] = temp


def reverse_train_past():
    global bp, moves_on_board, reversed_positions, game_positions
    # print('in train_past')
    for i in range(len(game_positions)):
        print(len(game_positions))
        if game_positions[i] != '':
            file = bp_library + convert_name(game_positions[i])
            print(file)
            p = open(file, "r")
            white_wins = p.readline()
            black_wins = p.readline()
            p.close()
            white_wins = white_wins[:-1]
            print(white_wins)
            print(black_wins)
            file = bp_library + convert_name(reversed_positions[i])
            print(file)
            p = open(file, "w")
            p.write(str(black_wins) + '\n' + str(white_wins))
            p.close()


def train_last():
    global game_positions, white_win, black_win
    # print('in train_last')
    for i in range(len(game_positions)):
        j = len(game_positions) - 1 - i
        # print('j game positions: ', game_positions[j], str(j))
    file = bp_library + convert_name(game_positions[len(game_positions) - 1])
    p = open(file, "r")
    white_wins = p.readline()
    black_wins = p.readline()
    p.close()
    white_wins = white_wins[:-1]
    # print('white_wins: ', str(white_wins))
    # print('black_wins: ', str(black_wins))
    if white_win:
        # print('detected white won')
        p = open(file, "w")
        # print(str(int(white_wins) + 1) + '\n' + str(int(black_wins) - 1))
        p.write(str(int(white_wins) + 2) + '\n' + str(int(black_wins) - 2))
        p.close()
    elif black_win:
        # print('detected black won')
        p = open(file, "w")
        # print(str(int(white_wins) - 1) + str(int(black_wins) + 1))
        p.write(str(int(white_wins) - 2) + str(int(black_wins) + 2))
        p.close()
    else:
        # print('detected draw')
        p = open(file, "w")
        # print(str(file))
        # print(str(int(white_wins) - 1) + '\n' + str(int(black_wins) - 1))
        p.write(str(int(white_wins) - 1) + '\n' + str(int(black_wins) - 1))
        p.close()
    # print('end train_past')


def train_past():
    global bp, moves_on_board
    # print('in train_past')
    for i in range(len(game_positions) - 2):
        j = len(game_positions) - 2 - i
        if game_positions[len(game_positions) - 1] == game_positions[j]:
            continue
        elif i % 2 != 0:
            # print('j check#1: ', str(j), ' white')
            get_moves_on_board(game_positions[j], 'white')
            validate_moves_on_board('white')
            best_white_success = ''
            best_black_success = ''
            # print('len of white moves on board: ', len(moves_on_board), ' : ', str(j))
            # print(game_positions[j])
            for k in range(len(moves_on_board)):
                file = bp_library + convert_name(moves_on_board[k])
                if not os.path.exists(file):
                    p = open(file, "w")
                    p.write('5\n5')
                    p.close()
                p = open(file, 'r')
                white_wins = p.readline()
                black_wins = p.readline()
                p.close()
                white_wins = white_wins[:-1]
                # print('white and black wins: ', str(white_wins), ' : ', str(black_wins), ' : ', file)
                if best_white_success == '':
                    best_white_success = int(white_wins)
                elif int(best_white_success) < int(white_wins):
                    best_white_success = int(white_wins)
                if best_black_success == '':
                    best_black_success = int(black_wins)
                elif int(best_black_success) < int(black_wins):
                    best_black_success = int(black_wins)
            file = bp_library + convert_name(game_positions[j])
            if (best_white_success == '') and (best_black_success == ''):
                p = open(file, 'w')
                p.write(str(-1000) + '\n' + str(-1000))
                p.close()
            elif best_white_success == '':
                p = open(file, 'w')
                p.write(str(-1000) + '\n' + str(best_black_success))
                p.close()
            elif best_black_success == '':
                p = open(file, 'w')
                p.write(str(best_white_success) + '\n' + str(-1000))
                p.close()
            else:
                p = open(file, 'w')
                # print('checkpoint #2: ', str(best_white_success) + ' : ' + str(best_black_success))
                p.write(str(best_white_success) + '\n' + str(best_black_success))
                p.close()
        elif i % 2 == 0:
            # print('j check#1: ', str(j), ' black')
            get_moves_on_board(game_positions[j], 'black')
            validate_moves_on_board('black')
            best_white_success = ''
            best_black_success = ''
            # print('len of black moves on board: ', len(moves_on_board), ' : ', str(j))
            # print(game_positions[j])
            for k in range(len(moves_on_board)):
                file = bp_library + convert_name(moves_on_board[k])
                if not os.path.exists(file):
                    p = open(file, "w")
                    p.write('5\n5')
                    p.close()
                p = open(file, 'r')
                white_wins = p.readline()
                black_wins = p.readline()
                p.close()
                white_wins = white_wins[:-1]
                # print('white and black wins: ', str(white_wins), ' : ', str(black_wins), ' : ', file)
                if best_white_success == '':
                    best_white_success = int(white_wins)
                elif int(best_white_success) < int(white_wins):
                    best_white_success = int(white_wins)
                if best_black_success == '':
                    best_black_success = int(black_wins)
                elif int(best_black_success) < int(black_wins):
                    best_black_success = int(black_wins)
            file = bp_library + convert_name(game_positions[j])
            # print(file, ' ', str(j))
            if (best_white_success == '') and (best_black_success == ''):
                p = open(file, 'w')
                p.write(str(-1000) + '\n' + str(-1000))
                p.close()
            elif best_white_success == '':
                p = open(file, 'w')
                p.write(str(-1000) + '\n' + str(best_black_success))
                p.close()
            elif best_black_success == '':
                p = open(file, 'w')
                p.write(str(best_white_success) + '\n' + str(-1000))
                p.close()
            else:
                # print('checkpoint #4: ', str(best_white_success) + ' : ' + str(best_black_success))
                p = open(file, 'w')
                p.write(str(best_white_success) + '\n' + str(best_black_success))
                p.close()
    # print('end train past')
    # print(str(file))


def learn():
    # print('learning')
    train_last()
    train_past()
    # reverse_positions()
    # reverse_train_past()


def move(color):
    global bp
    # print('starting move')
    get_moves(color)
    chosen_move = choose_move(color)
    move_piece(chosen_move, bp)
    bp = chosen_move


def wait(color):
    global bp
    while True:
        # print('waiting for move')
        user_input = input('move code:')
        # print('in wait bp is: ' + bp)
        if user_input == '0':
            exit(0)
        elif (len(user_input) == 4) and (user_input.isnumeric()) and (validate_move(user_input, color)):
            # print('Found match: ' + bp)
            move_piece(get_input_bp(user_input), bp)
            bp = get_input_bp(user_input)
            # print('done waiting for move')
            break
        elif (len(user_input) == 5) and (user_input[0:4].isnumeric()) and (validate_move(user_input, color)):
            # print('Found match: ' + bp)
            move_piece(get_input_bp(user_input), bp)
            bp = get_input_bp(user_input)
            # print('done waiting for move')
            break
        else:
            print('invalid move: ' + user_input)


def play(color):
    global bp
    # print('moving in background')
    get_moves(color)
    bp = choose_move(color)


####################################################################################
# MAJOR FUNCTIONS
####################################################################################


def play_white():
    while True:
        global game_over, game_positions, moves_on_board
        global white_win, black_win, checkmate, stalemate, bp
        moves_on_board = ['']
        game_positions = ['']
        game_over = False
        print('playing against white')
        draw_board()
        set_board()
        for i in range(40):
            end_no_save()
            print('move #', (i * 2) + 1)
            wait('white')
            if bp != '':
                game_positions.append(bp)
            else:
                show_stats(2 * i)
                learn()
                bp = 'RNBQKBNRPPPPPPPP00000000000000000000000000000000pppppppprnbqkbnr'
                break
            end_no_save()
            print('move #', (i * 2) + 2)
            print('moving black')
            move('black')
            if bp != '':
                game_positions.append(bp)
            else:
                show_stats((2 * i) + 1)
                learn()
                bp = 'RNBQKBNRPPPPPPPP00000000000000000000000000000000pppppppprnbqkbnr'
                break
            if (i + 1) >= 40:
                game_over = True
                white_win = False
                black_win = False
                checkmate = False
                stalemate = False
                show_stats((2 * i) + 2)
                learn()


def ai_vs():
    global games_played, draw_games, white_games, black_games
    games_played = 0
    white_games = 0
    black_games = 0
    draw_games = 0
    while True:
        global game_over, game_positions, moves_on_board
        global white_win, black_win, checkmate, stalemate, bp
        moves_on_board = ['']
        game_positions = ['']
        game_over = False
        print('playing against myself')
        draw_board()
        set_board()
        for i in range(40):
            if i == 0:
                bp = 'RNBQKBNRPPPPPPPP00000000000000000000000000000000pppppppprnbqkbnr'
            end_save()
            print('move #', (i * 2) + 1)
            print('moving white')
            move('white')
            end_save()
            if bp != '':
                game_positions.append(bp)
            else:
                show_stats(2 * i)
                learn()
                bp = 'RNBQKBNRPPPPPPPP00000000000000000000000000000000pppppppprnbqkbnr'
                break
            print('move #', (i * 2) + 2)
            print('moving black')
            move('black')
            if bp != '':
                game_positions.append(bp)
            else:
                show_stats((2 * i) + 1)
                learn()
                bp = 'RNBQKBNRPPPPPPPP00000000000000000000000000000000pppppppprnbqkbnr'
                break
            if (i + 1) >= 40:
                game_over = True
                white_win = False
                black_win = False
                checkmate = False
                stalemate = False
                show_stats((2 * i) + 2)
                learn()
        if white_win:
            white_games += 1
        elif black_win:
            black_games += 1
        else:
            draw_games += 1
        games_played += 1


def train():
    global games_played, draw_games, white_games, black_games
    games_played = 0
    white_games = 0
    black_games = 0
    draw_games = 0
    while True:
        print('number of games played', games_played)
        global game_over, game_positions, moves_on_board
        global white_win, black_win, checkmate, stalemate, bp
        moves_on_board = ['']
        game_positions = ['']
        game_over = False
        for i in range(40):
            if i == 0:
                bp = 'RNBQKBNRPPPPPPPP00000000000000000000000000000000pppppppprnbqkbnr'
            end_save()
            # print(bp, 'move #', (i * 2) + 1)
            # print('move #', (i * 2) + 1)
            # print('moving white')
            play('white')
            if bp != '':
                game_positions.append(bp)
            else:
                show_stats(2 * i)
                learn()
                bp = 'RNBQKBNRPPPPPPPP00000000000000000000000000000000pppppppprnbqkbnr'
                break
            # print(bp, 'move #', (i * 2) + 2)
            # print('move #', (i * 2) + 2)
            # print('moving black')
            play('black')
            if bp != '':
                game_positions.append(bp)
            else:
                show_stats((2 * i) + 1)
                learn()
                bp = 'RNBQKBNRPPPPPPPP00000000000000000000000000000000pppppppprnbqkbnr'
                break
            if (i + 1) >= 40:
                game_over = True
                white_win = False
                black_win = False
                checkmate = False
                stalemate = False
                show_stats((2 * i) + 2)
                learn()
        if white_win:
            white_games += 1
        elif black_win:
            black_games += 1
        else:
            draw_games += 1
        games_played += 1


def play_black():
    while True:
        global game_over, game_positions, moves_on_board
        global white_win, black_win, checkmate, stalemate, bp
        moves_on_board = ['']
        game_positions = ['']
        game_over = False
        print('playing against black')
        draw_board()
        set_board()
        for i in range(40):
            end_no_save()
            print('move #', (i * 2) + 1)
            print('moving white')
            move('white')
            end_no_save()
            if bp != '':
                game_positions.append(bp)
            else:
                show_stats(2 * i)
                learn()
                bp = 'RNBQKBNRPPPPPPPP00000000000000000000000000000000pppppppprnbqkbnr'
                break
            print('move #', (i * 2) + 2)
            wait('black')
            if bp != '':
                game_positions.append(bp)
            else:
                show_stats((2 * i) + 1)
                learn()
                bp = 'RNBQKBNRPPPPPPPP00000000000000000000000000000000pppppppprnbqkbnr'
                break
            if (i + 1) >= 40:
                game_over = True
                white_win = False
                black_win = False
                checkmate = False
                stalemate = False
                show_stats((2 * i) + 2)
                learn()


def custom():
    again = True
    while again:
        global game_over, game_positions, moves_on_board
        global white_win, black_win, checkmate, stalemate, bp
        print('white or black?')
        while True:
            color = input('input your color: ')
            if (color == 'white') or (color == 'black'):
                break
            else:
                print('invalid color')
        while True:
            bp = input('input your board code: ')
            if len(bp) == 64:
                break
            else:
                print('invalid bp code')
        moves_on_board = ['']
        game_positions = ['']
        game_over = False
        print('playing custom board')
        draw_board()
        update_board(bp, '0000000000000000000000000000000000000000000000000000000000000000')
        if color == 'white':
            print('moving black')
            time.sleep(3)
            move('black')
        elif color == 'black':
            print('moving white')
            time.sleep(3)
            move('white')
        while True:
            user_input = input('again? y/n: ')
            if user_input == 'y':
                again = True
                break
            elif user_input == 'n':
                again = False
                home()
                break
            else:
                print('please choose y/n')


def home():
    print('########################')
    print('## displaying options ##')
    print('########################')
    print(' esc: stop program')
    print(' input 0 to exit')
    print(' 1: play a white player')
    print(' 2: AI vs AI')
    print(' 3: Train AI')
    print(' 4: play a black player')
    print(' 5: display options')
    print(' 6: choose move')
    print('########################')


home()

####################################################################################
# MAIN
####################################################################################


while True:
    time.sleep(0.05)
    if keyboard.is_pressed('0'):
        print('0 was pressed')
        # close application
        exit(00)
    elif keyboard.is_pressed('1'):
        print('1 was pressed')
        # white vs AI
        play_white()
    elif keyboard.is_pressed('2'):
        print('2 was pressed')
        # AI vs AI
        ai_vs()
    elif keyboard.is_pressed('3'):
        print('3 was pressed')
        # AI vs AI no graphics
        train()
    elif keyboard.is_pressed('4'):
        print('4 was pressed')
        # black vs AI
        play_black()
    elif keyboard.is_pressed('5'):
        print('5 was pressed')
        # display options
        home()
    elif keyboard.is_pressed('6'):
        # custom board
        custom()
