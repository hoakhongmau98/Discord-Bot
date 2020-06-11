import Password.class_decode_chr as decode


class pw_cvt_str():
    # key_log_numb thứ tự của char trong key log
    # key_stt thứ tự của char trong bảng key_log
    # Dùng chr(number) để chuyển từ số sang ký tự trong bảng ascii
    def __init__(self, str_in):
        self.chr_in = str_in
        self.str_cvt = []
        self.key_log_numb = []
        self.key_decode_t9 = []

    # Kiểm tra chuỗi đầu tiên 1,4,7,10,...
    def T9_to_chr(self):
        for i in self.chr_in:
            if i in decode.chr_t9:
                self.str_cvt.append(decode.chr_t9[i])

                self.key_decode_t9.append(chr(int(decode.chr_decode_t9[i])))
            else:
                self.str_cvt.append(i)
        return ''.join(self.str_cvt), self.key_decode_t9

    # Kiểm tra chuỗi thứ 2
    def numb_chr(self):
        for i in self.chr_in:
            if not i.isdigit():
                if i in decode.chr_t9:
                    self.str_cvt.append(decode.chr_numb[decode.chr_t9[i].lower()])
                    self.key_decode_t9.append(chr(int(decode.chr_decode_t9[i])))
                    self.key_log_numb.append(decode.chr_numb_log[decode.chr_t9[i].lower()])
                else:
                    self.str_cvt.append(decode.chr_numb[i.lower()])
                    self.key_log_numb.append(decode.chr_numb_log[i.lower()])
            else:
                self.str_cvt.append(i)
        return ''.join(self.str_cvt), self.key_decode_t9, self.key_log_numb

    # KIểm tra chuỗi thứ 3
    def super_chr(self):
        for i in self.chr_in:
            if not i.isdigit():
                if i in decode.chr_t9:
                    numb_i = decode.chr_numb[decode.chr_t9[i].lower()]
                    self.str_cvt.append(decode.chr_power_str[numb_i])
                    self.key_decode_t9.append(chr(int(decode.chr_decode_t9[i])))
                    self.key_log_numb.append(decode.chr_numb_log[decode.chr_t9[i].lower()])
                else:
                    numb_i = decode.chr_numb[i.lower()]
                    self.str_cvt.append(decode.chr_power_str[numb_i])
                    self.key_log_numb.append(decode.chr_numb_log[i.lower()])
            else:
                self.str_cvt.append(decode.chr_power_str[i])
        return ''.join(self.str_cvt), self.key_decode_t9, self.key_log_numb


'''
Vấn đề:
Chuỗi đầu tiên nếu có chữ T9 thì phải chuyển về bthg, rồi phải chuyển sang
- Có thể dùng nhận dạng chữ cái và soi chiếu tới keynumb ở cuối dãy để định dạng lại ký tự
Chuỗi thứ 2 và thứ 3, sau khi được định dạng sang số, cần 1 bước định dạng nữa để xác định 
Ký tự đó có số thứ tự trên 1 số 1-9 là stt nào 1-4
Sau khi biết được cũng sẽ dùng soi chiếu như với chuỗi đầu tiên
Cái khó ở đây là làm saao để chuỗi đầu tiên có thể thực hiện chung bước với xử lý chuỗi 2-3

'''
