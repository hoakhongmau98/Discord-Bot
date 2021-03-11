"""
B1: cắt chuỗi thành các thành phần
B2: Tiền hành chuyển đổi từng phần
	- text to text
	- super_chr to numb
	- numb to numb
B3: Chuyển đổi numb thành chữ cái
B4: Ghép tất cả thành 1 chuỗi non 
B5: Cắt chuỗi thành từng ký tự nhỏ
B6: Quét chuỗi, nếu là ký tự dạng phụ âm
B7: Dựa vào code chuyển phụ âm thành phụ âm có dấu
B8: Ghép chuỗi và hoàn thành chuỗi
"""
import Password.class_decode_chr as decode
import Password.class_deconvert_chr as deconvert
# str_pw = 'Nguyen*$#*286640332132321htGPDnd715'
# 15 là độ dài chuỗi pw
# 7 là độ dài chuỗi đánh giá ký tự đặc biệt
# str_pw = input('Enter your password want to deconvert to string: ')
# Module 1
# Các thành phần của chuỗi


def analysis_passwords(str_pw):
	password = ''
	key_space = ''
	chr_log = ''
	chr_decode = ''
	len_chr_decode = ''
	pw_len = ''
	# Phân tích thông tin các thành phần
	pw_len = str_pw[-2:]
	password = str_pw[:int(pw_len)]
	key_space = str_pw[int(pw_len)]
	len_chr_decode = str_pw[-3]
	chr_decode = str_pw[(-3-int(len_chr_decode)):-3]
	chr_log = str_pw[(int(pw_len)+1):(-3-int(len_chr_decode))]
	return pw_len, password, key_space, len_chr_decode, chr_decode, chr_log


# Hàm xử lý chính để chuyển đổi chuỗi
# pw[text,sp_chr,numb,text,..] => pw[text,numb,numb,text,...]
def cut_str_pw(pw):
	# point_start: đánh dấu điểm bắt đầu của chuỗi
	# point_start = numb_point:
	point_start = 0
	lst_pw = []
	while point_start < len(pw):
		for i in pw[point_start:]:
			if i.isalpha():
				str_1 = deconvert.str_cvt_pw(pw,point_start)
				tuple_1 = str_1.decode_alpha()
				point_start = tuple_1[1]
				lst_pw.append(tuple_1[0])
				break
			elif i.isdigit():
				str_2 = deconvert.str_cvt_pw(pw,point_start)
				tuple_2 = str_2.decode_digit()
				point_start = tuple_2[1]
				lst_pw.append(tuple_2[0])
				break
			else:
				str_3 = deconvert.str_cvt_pw(pw,point_start)
				tuple_3 = str_3.decode_super_str()
				point_start = tuple_3[1]
				lst_pw.append(tuple_3[0])
				break
	return lst_pw


# lst_pw = cut_str_pw(password)
# print(lst_pw)
# Module 2: Tạo chuỗi gần hoàn chỉnh, không dấu
# Tách ký tự số và ký tự text
def cut_lst(lst_a):
	x = 1
	# lst chúa ký tự là số
	lst_new = []
	while x < len(lst_a):
		if x +2 == len(lst_a):
			lst_new.append(lst_a[x])
			lst_new.append(lst_a[x+1])
			break
		elif x + 1 == len(lst_a):
			lst_new.append(lst_a[x])
			break
		else:
			lst_new.append(lst_a[x])
			lst_new.append(lst_a[x+1])
			x = x+3
	return lst_new


# chr_pw_numb = cut_lst(lst_pw)
# In ra lst chứa list con là số
# print(chr_pw_numb)

def decode_number_to_text(chr_pw_numb, chr_log):
	# Tính số phần tử chuỗi từng chuỗi con
	len_pw_numb = [len(x) for x in chr_pw_numb]
	# Nối chuỗi thành 1 chuỗi dài để decode hàng loạt vì đều là số => chữ
	str_pw_numb = ''.join(chr_pw_numb)
	# Tạo list chứa tất cả các ký tự của chuỗi str_pw_nummb
	lst_chr_numb = [[] for i in range(len(str_pw_numb))]
	# Cắt ra các ký tự mang cùng số
	for i in range(len(str_pw_numb)):
		for key, value in decode.chr_numb.items():
			if value == str_pw_numb[i]:
				lst_chr_numb[i].append(key)
	# print(lst_chr_numb)
	# list chứa các ký tự sau khi đã được decode thành text
	lst_str_numb = []
	for i in range(len(chr_log)):
		lst_str_numb.append(lst_chr_numb[i][int(chr_log[i])-1])
	# print(lst_str_numb)
	# Trả về đúng thứ tự của chuỗi password chính
	return len_pw_numb, lst_str_numb


def rebuild_chr_numb(len_lst,lst_str):
	zxc = 0
	lst_str_pw = []
	for i in len_lst:
		lst_str_pw.append(''.join(lst_str[zxc:zxc+int(i)]))
		zxc += i
	return lst_str_pw


# lst_new = rebuild_chr_numb(len_pw_numb,lst_str_numb)
# print(lst_new)


def rebuild_password(str_in,lst_chr):
	xa = 0
	xy = 1
	while xy < len(str_in):
		if (xy + 2) == len(str_in):
			str_in[xy] = lst_chr[xa]
			str_in[xy+1] = lst_chr[xa+1]
			xy += 3 
			xa += 2
		elif (xy + 1) == len(str_in):
			str_in[xy] = lst_chr[xa]
			xy += 3 
			xa += 2
		else:
			str_in[xy] = lst_chr[xa]
			str_in[xy+1] =lst_chr[xa+1]
			xy += 3 
			xa += 2
	return str_in


# lst_pw = rebuild_password(lst_pw, lst_new)


def make_string(text):
	pw_len, password, key_space, len_chr_decode, chr_decode, chr_log = analysis_passwords(text)
	lst_pw = cut_str_pw(password)
	chr_pw_numb = cut_lst(lst_pw)
	len_pw_numb, lst_str_numb = decode_number_to_text(chr_pw_numb, chr_log)
	lst_str_pw = rebuild_chr_numb(len_pw_numb, lst_str_numb)
	str_out = rebuild_password(lst_pw, lst_str_pw)
	# Tạo ra chuỗi pw gần hoàn chỉnh chưa có dấu
	if key_space == '0':
		lst_pw = ' '.join(lst_pw).title()
	else:
		lst_pw = '.'.join(lst_pw).title()
	# Module 3 decode T9
	# CHuyển từng ký tự vào mảng để quét ký tự T9
	lst_pw = [x for x in lst_pw]
	# Giải mã Chr_decode để chuyển đổi ký tự
	# list chứa các ký tự có nằm trong bảng chr_t9_non
	# Các ký tự có thể mang dấu
	str_t9_non = []
	for i in lst_pw:
		if i in decode.chr_t9_non:
			str_t9_non.append(i)
	# Lặp từng ký tự từ chr_decode so sánh với dictionary chr_decode_t9
	# Nếu có value nào trùng với str(ord(i)) thì cout >> key
	# str(ord(i)): ord(i) chuyển ký tự từ bảng acii sang dạng số
	str_t9 = []
	for i in chr_decode:
		for key,value in decode.chr_decode_t9.items():
			if str(ord(i)) == value:
				str_t9.append(key)
	stt_str_t9 = 0
	for i in range(len(lst_pw)):
		if lst_pw[i] in decode.chr_t9_non:
			lst_pw[i] = str_t9[stt_str_t9]
			stt_str_t9 += 1
	return ''.join(lst_pw)


# b = ['deconvert_password', 'Duong$*(#^8726402232213121nbhtE1615']
# a = make_string(b[1])
# print(a)