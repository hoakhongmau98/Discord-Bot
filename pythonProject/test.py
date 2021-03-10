import numpy as np
lst_a = [[], [], [], [], [], [], [], [], []]
for row in range(9):
    lst_a[row] = list(map(int, (input(f'nhập dãy số {row} (viết liền không khoảng trắng:)'))))

lst_a = np.array(lst_a)
print(lst_a)