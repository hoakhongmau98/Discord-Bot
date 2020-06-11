from bs4 import BeautifulSoup
import requests

url = 'https://genk.vn'
html_content = requests.get(url).text
file_object = open('/home/huyenchi/discord_bot/filetxt/tech_news.txt', 'r')
file_object.seek(0)
lines = file_object.readlines()
lines = lines[0].split(' ')
lines = lines[1:]
file_object.close()
#
file_object = open('/home/huyenchi/discord_bot/filetxt/10_news_tech.txt', 'r')
file_object.seek(0)
lines_news = file_object.readlines()
lines_news = lines[0].split(' ')
lines_news = lines[1:]
file_object.close()
soup = BeautifulSoup(html_content, features="html.parser")
lst_link = []
for link in soup.find("div", attrs={"class": "kds-new-stream-wrapper"}).select('a[href]'):
    for href in link:
        str_out = 'https://genk.vn' + ''.join(link.get('href'))
        lst_link.append(str_out)

lst_link = list(set(lst_link))
print([x for x in lst_link if x not in lines ])
# print([x for x in lines if x not in lines_news])
# def get_tech():
#     url = 'https://genk.vn'
#     html_content = requests.get(url).text
#     file_object = open('filetxt/tech_news.txt', 'r')
#     file_object.seek(0)
#     lines = file_object.read()
#     lines = lines[0].split(' ')
#     file_object.close()
#     soup = BeautifulSoup(html_content, features="html.parser")
#     # print(soup.title.text)
#     a = 0
#     lst_link = []
#     for link in soup.find("div", attrs={"class": "kds-new-stream-wrapper"}).select('a[href]'):
#         for href in link:
#             str_out = 'https://genk.vn'+''.join(link.get('href'))
#             lst_link.append(str_out)
#     lst_link = list(set(lst_link))
#     list_news = [x for x in lst_link if x not in lines]
#     with open('filetxt/tech_news.txt', 'w') as file_object:
#         file_object.seek(0)
#         file_object.writelines([' '+''.join(k) for k in lst_link])
#     file_object.close()
#     if len(list_news) == 0:
#         with open('filetxt/10_news_tech.txt', 'r') as f:
#             f.seek(0)
#             news = f.read()
#             news = news[0].split(' ')
#         return news
#     else:
#         with open('filetxt/10_news_tech.txt', 'w+') as file_object:
#             file_object.seek(0)
#             file_object.writelines([' ' + ''.join(k) for k in lst_link])
#         return list_news