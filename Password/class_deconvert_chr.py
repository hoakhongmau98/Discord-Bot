import Password.class_decode_chr as decode


class str_cvt_pw():
	def __init__(self,str_in,numb_start):
		self.str_in = str_in
		self.numb_start = numb_start	
	# Chuyển đổi ký tự text thành text
	numb_point = 0
	
	def decode_alpha(self):
		str_alpha = ''
		numb_point = self.numb_start
		for i in self.str_in[self.numb_start:]:
			if numb_point == (len(self.str_in)-1) and i.isalpha():
				str_alpha = str_alpha + i
				numb_point += 1
				return str_alpha, numb_point
			elif i.isalpha():
				str_alpha = str_alpha + i
				numb_point += 1
			else:
				return str_alpha, numb_point
				break
	# Chuyển đổi ký tự dạng số dang số
	
	def decode_digit(self):
		str_digit = ''
		numb_point = self.numb_start
		for i in self.str_in[self.numb_start:]:
			if numb_point == (len(self.str_in)-1) and i.isdigit():
				str_digit = str_digit + i
				numb_point += 1
				return str_digit, numb_point
			elif i.isdigit():
				str_digit = str_digit + i
				numb_point += 1
				#return str_digit, numb_point
			else:
				return str_digit, numb_point
				break
	# CHuyển đổi ký tự đặc biệt sang số
	
	def decode_super_str(self):
		str_super = ''
		numb_point = self.numb_start
		for i in self.str_in[self.numb_start:]:
			if numb_point == (len(self.str_in)-1) and (not i.isdigit() and not i.isalpha()):
				for key,value in decode.chr_power_str.items():
					if i is value:
						str_super = str_super + key
						numb_point += 1
						return str_super, numb_point
			elif not i.isdigit() and not i.isalpha():
				for key,value in decode.chr_power_str.items():
					if i is value:
						str_super = str_super + key
						numb_point += 1
			else:
				return str_super, numb_point
# class rebuild_case_password():
# 	def __init__(self,lst_chr,str_in):
# 		self.lst_chr = lst_chr
# 		self.str_in = str_in

# 	def rebuild_password(self):
# 		xa = 0
# 		xy = 1
# 		while xy < len(self.str_in):
# 			if (xy + 2) == len(self.str_in):
# 				self.str_in[xy] = self.lst_chr[xa]
# 				self.str_in[xy+1] = self.lst_chr[xa+1]
# 			elif (xy + 1) == len(self.str_in):
# 				self.str_in[xy] = self.lst_chr[xa]
# 			else:
# 				self.str_in[xy] = self.lst_chr[xa]
# 				self.str_in[xy+1] =self.lst_chr[xa+1]
# 				xy += 3 
# 				xa += 2
# 		return self.str_in

