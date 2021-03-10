import numpy as np
import random
import time

# main_board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
#               [0, 3, 0, 0, 0, 9, 0, 5, 0],
#               [0, 0, 9, 8, 2, 0, 0, 1, 3],
#               [1, 0, 7, 0, 9, 0, 0, 0, 0],
#               [3, 0, 0, 0, 0, 0, 0, 4, 5],
#               [0, 0, 0, 0, 0, 0, 0, 0, 6],
#               [0, 2, 0, 0, 7, 4, 0, 0, 0],
#               [0, 0, 0, 9, 0, 0, 0, 0, 0],
#               [0, 6, 0, 1, 0, 5, 4, 0, 0]]

# main_board = [[0, 9, 3],
#               [0, 0, 7],
#               [0, 2, 4]]

main_board = [[], [], [], [], [], [], [], [], []]
i = 0
while i < 9:
    lst_row = list(map(int, (input(f'nhập dãy số {i} (viết liền không khoảng trắng:)'))))
    if len(lst_row) == 9:
        main_board[i] = lst_row
        i += 1

# main_board = np.array(main_board)


def sudoku_sovel(m):
    place = find_blank_place(m)
    if not place:
        return True
    else:
        row, col = place
    for number in range(1, 10):
        # Nếu check_board trả về True gán giá trị number cho m
        if check_board(m, number, row, col):
            m[row][col] = number
            # time.sleep(0.5)
            print("------------Preview------------")
            print_board(m)
            # tiếp tục thực hiện nếu trả True thì tiếp tục vòng lặp
            if sudoku_sovel(m):
                return True
            # Nếu lỗi hoặc trả về False ở 1 bước sẽ gán lại giá trị 0 cho m, lặp lại vòng lặp
            else:
                m[row][col] = 0
    return print("Can't solver")


def check_board(m, number, row, col):
    # Kiểm tra giá trị từng dòng với cột cho trước
    for m_col in range(len(m[0])):
        # print('Here', m[row][m_col], number)
        if m[row][m_col] == number and col != m_col:
            # Nếu giá phần tử mang giá trị hàng cố định với hàng chạy từ 0 tới 9
            # mang giá trị trùng với giá trị đưa ra và phần tử đó k`hông phải là phần tử trống đang xét
            # Thì sẽ trả về sẽ trả về false tương ứng đã có giá trị trùng với giá trị đang được xét.
            # ----------
            # Trường hợp phụ: Nếu giá trị hiện tại trùng với giá trị xét và trùng với nhau và trùng ô cũng được tính là
            # False vì nó không ảnh hưởng tới tính sai.
            return False
    # kiểm tra giá trị từng cột với hàng cho trước
    # print('here')
    for m_row in range(len(m)):
        if m[m_row][col] == number and row != m_row:
            return False
    # Kiểm tra trong ô 3x3
    x = col // 3
    y = row // 3
    # kết hợp kiểm tra hàng và cột với giá trị cho trước
    for i in range(y * 3, y * 3 + 3):
        for j in range(x * 3, x * 3 + 3):
            if m[i][j] == number and i != row and j != col:
                return False
    return True


def print_board(m):
    if m is None:
        print('No Solution')
        return
    line = '-' * 25
    if len(m) == 0:
        print('board is empty')
        return

    # cắt board
    __number_of_columns = len(m[0])
    __number_of_rows = len(m)
    # print(__number_of_rows)
    # print(__number_of_columns)
    # board check
    if __number_of_columns == 3:
        print('-' * 13)
        for row in m:
            print('|', end='')
            for s_char in row:
                if s_char == 0:
                    s_char = ' '
                print(' ' + str(s_char) + ' |', end='')
            print('\n' + '-' * 13)
    elif __number_of_rows == 9:
        print('-' * 31)
        for row in m:
            print('|', end='')
            for i in range(9):
                s_char = row[i]
                if s_char == 0:
                    s_char = ' '
                if i in [2, 5, 8]:
                    print(' ' + str(s_char) + ' |', end='')
                else:
                    print(' ' + str(s_char) + ' ', end='')

            if m.index(row) in [2, 5, 8]:
                print('\n' + '-' * 31)
            else:
                print('')
    else:
        print('ERROR board')
        return


# print(main_board)
print_board(main_board)


def find_blank_place(m):
    # tìm 1 phần tử trống trong board
    for row in range(len(m)):
        for col in range(len(m[0])):
            if m[row][col] == 0:
                return row, col
    return None


# find_blank_place(main_board)

# # fill box 3x3
# def fill_3x3(m):
#     lst_nb = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     lst_nb = random.sample(lst_nb, len(lst_nb))
#     for row, col in find_blank_place(m):
#         print(row, col)
#         print(lst_nb)
#         for number in lst_nb:
#             if number not in np.array(m):
#                 m[row][col] = number
#                 break
#
#     return print_board(m)
#
#
# fill_3x3(main_board)
# # print(7 in main_board)

# check rule board


print("------------solver-------------")
sudoku_sovel(main_board)
print_board(main_board)
