please input your token in filetxt/token.txt
11:40 18-12-2020: Error 
""
Ignoring exception in on_message
Traceback (most recent call last):
  File "/home/huyenchi/miniconda3/envs/.discord/lib/python3.6/site-packages/discord/client.py", line 333, in _run_event
    await coro(*args, **kwargs)
  File "index.py", line 112, in on_message
    str_out = getnews.get_tech()
  File "/home/huyenchi/Discord-Bot/function/getnews.py", line 45, in get_tech
    file_object = open('/home/huyenchi/discord_bot/filetxt/tech_news.txt', 'r')
FileNotFoundError: [Errno 2] No such file or directory: '/home/huyenchi/discord_bot/filetxt/tech_news.txt'
Ignoring exception in on_message
Traceback (most recent call last):
  File "/home/huyenchi/miniconda3/envs/.discord/lib/python3.6/site-packages/discord/client.py", line 333, in _run_event
    await coro(*args, **kwargs)
  File "index.py", line 104, in on_message
    str_out = get_tkb.tkb_today(str_in[1])
IndexError: list index out of range
Ignoring exception in on_message
Traceback (most recent call last):
  File "/home/huyenchi/miniconda3/envs/.discord/lib/python3.6/site-packages/discord/client.py", line 333, in _run_event
    await coro(*args, **kwargs)
  File "index.py", line 97, in on_message
    str_weather = weather.weather(str_in[1])
IndexError: list index out of range
Ignoring exception in on_message
Traceback (most recent call last):
  File "/home/huyenchi/miniconda3/envs/.discord/lib/python3.6/site-packages/discord/client.py", line 333, in _run_event
    await coro(*args, **kwargs)
  File "index.py", line 66, in on_message
    passwords = make_password.converter(str_in[1])
  File "/home/huyenchi/Discord-Bot/Password/make_password.py", line 57, in converter
    pw = str_2.numb_chr()
  File "/home/huyenchi/Discord-Bot/Password/class_convert_chr.py", line 34, in numb_chr
    self.str_cvt.append(decode.chr_numb[i.lower()])
KeyError: 'đ'
Ignoring exception in on_message
Traceback (most recent call last):
  File "/home/huyenchi/miniconda3/envs/.discord/lib/python3.6/site-packages/discord/client.py", line 333, in _run_event
    await coro(*args, **kwargs)
  File "index.py", line 73, in on_message
    str_out = deconvert_password.make_string(str_in[1])
  File "/home/huyenchi/Discord-Bot/Password/deconvert_password.py", line 158, in make_string
    pw_len, password, key_space, len_chr_decode, chr_decode, chr_log = analysis_passwords(text)
  File "/home/huyenchi/Discord-Bot/Password/deconvert_password.py", line 34, in analysis_passwords
    key_space = str_pw[int(pw_len)]
IndexError: string index out of range
Ignoring exception in on_message
Traceback (most recent call last):
  File "/home/huyenchi/miniconda3/envs/.discord/lib/python3.6/site-packages/discord/client.py", line 333, in _run_event
    await coro(*args, **kwargs)
  File "index.py", line 73, in on_message
    str_out = deconvert_password.make_string(str_in[1])
  File "/home/huyenchi/Discord-Bot/Password/deconvert_password.py", line 158, in make_string
    pw_len, password, key_space, len_chr_decode, chr_decode, chr_log = analysis_passwords(text)
  File "/home/huyenchi/Discord-Bot/Password/deconvert_password.py", line 34, in analysis_passwords
    key_space = str_pw[int(pw_len)]
IndexError: string index out of range
Ignoring exception in on_message
Traceback (most recent call last):
  File "/home/huyenchi/miniconda3/envs/.discord/lib/python3.6/site-packages/discord/client.py", line 333, in _run_event
    await coro(*args, **kwargs)
  File "index.py", line 73, in on_message
    str_out = deconvert_password.make_string(str_in[1])
  File "/home/huyenchi/Discord-Bot/Password/deconvert_password.py", line 158, in make_string
    pw_len, password, key_space, len_chr_decode, chr_decode, chr_log = analysis_passwords(text)
  File "/home/huyenchi/Discord-Bot/Password/deconvert_password.py", line 34, in analysis_passwords
    key_space = str_pw[int(pw_len)]
IndexError: string index out of range
""
