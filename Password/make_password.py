import Password.class_convert_chr as cvt_chr


# Nhập chuỗi để convert
# str_in = 'Nguyễn Thanh Thảo'
# Cắt chuỗi
# str_in = input('Enter your string u want convert to password: ')

'''
	str_in = list chứa các thành phần sau khi cắt dấu cách or dấu chấm
'''


def prepare(str_in):
	key_space = ''
	if '.' in str_in:
		str_in = str_in.split('.')
		key_space = '1'
	else:
		str_in = str_in.split(' ')
		key_space = '0'
	# str_in out same like str_in = ['Nguyễn', 'Thanh', 'Thảo']
	return str_in, key_space


def converter(str_in):
	str_in, key_space = prepare(str_in)
	# Tạo list password trống
	password = [x for x in range(len(str_in))]
	# Kiểm tra và thực hiện công việc với chuỗi dài hơn 3 đối tượng
	key_decode = []
	key_log = []
	chr_decode = []
	chr_log = []
	lst_0 = 0
	lst_1 = 1
	lst_2 = 2
	# Vòng lặp for chạy theo số thứ tự đã được ấn định theo quy ước sẵn
	# text - super_chr - numb
	# mỗi lần chạy sẽ tương ứng với 1 đơn vị cố định, 1 chuỗi trong list str_in
	for i in range(len(str_in)):
		if i == (lst_0):
			str_0 = cvt_chr.pw_cvt_str(str_in[i])
			pw = str_0.T9_to_chr()
			password[i] = pw[0]
			key_decode.append(pw[1])
			lst_0 = lst_0 + 3
		elif i == (lst_1):
			str_1 = cvt_chr.pw_cvt_str(str_in[i])
			pw = str_1.super_chr()
			password[i] = pw[0]
			key_decode.append(pw[1])
			key_log.append(pw[2])
			lst_1 += 3
		elif i == (lst_2):
			str_2 = cvt_chr.pw_cvt_str(str_in[i])
			pw = str_2.numb_chr()
			password[i] = pw[0]
			key_decode.append(pw[1])
			key_log.append(pw[2])
			lst_2 += 3
	# print(key_log)
	for i in key_decode:
		chr_decode = chr_decode + i
	# print(chr_decode)
	# print(key_log)
	for i in key_log:
		chr_log = chr_log + i
	# print(chr_log)
	# Tạo pw_len - đếm số ký tự của passwords
	# print(password)
	pw_len = len(''.join(password))
	if pw_len > 10:
		pw_len = str(pw_len)
	else:
		pw_len = '0' + str(pw_len)
	full_password = ''.join(password) + key_space + ''.join(chr_log) + ''.join(chr_decode)\
														+ str(len(chr_decode)) + pw_len
	key_password = key_space+''.join(chr_log)+''.join(chr_decode)+str(len(chr_decode))+pw_len
	your_password = ''.join(password)
	return full_password, key_password, your_password

# print(len('Tran*$$48936Trang012322323?1ShtE617'))
# print(key_space)
# print(key_log)
# print(chr_log)
# print(chr_decode)


# a = converter("Dương Huyền Trang")
# print(a)

'''
return [full_password, Key_password, your_password ]
'''
'''
Chương trình hỗ trợ cho chuỗi pw dưới 24 ký tự
Vì Nếu trên 24 ký tự chuỗi sau khi xử lý sẽ dài ra và làm hỏng tính chất của chuỗi
'''
