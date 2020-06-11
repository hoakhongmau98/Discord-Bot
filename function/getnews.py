from bs4 import BeautifulSoup
import requests


def get_news():
    url = "https://news.zing.vn/"
    html_content = requests.get(url).text

    soup = BeautifulSoup(html_content, features="html.parser")

    # print(soup.title.text)
    a = 0
    lst_link = []
    for link in soup.find("div", attrs={"data-content": "newsfeatured"}).select('a[href]'):
        # print("Inner Text: {}".format(link.text))
        # print("Title: {}".format(link.get("title")))
        # print("href: {}".format(link.get("href")))
        # print(type(link))
        # print(type(soup))
        for href in link:
            str_out = 'https://zing.vn'+''.join(link.get('href'))
            lst_link.append(str_out)
    for link in soup.find("div", attrs={"data-content": "newstrending"}).select('a[href]'):
        # print("Inner Text: {}".format(link.text))
        # print("Title: {}".format(link.get("title")))
        # print("href: {}".format(link.get("href")))
        # print(type(link))
        # print(type(soup))
        for href in link:
            str_out = 'https://zing.vn'+''.join(link.get('href'))
            lst_link.append(str_out)
    return set(lst_link)


def get_tech():
    url = 'https://genk.vn'
    html_content = requests.get(url).text
    file_object = open('/home/huyenchi/discord_bot/filetxt/tech_news.txt', 'r')
    file_object.seek(0)
    lines = file_object.readlines()
    lines = lines[0].split(' ')
    lines = lines[1:]
    file_object.close()
    soup = BeautifulSoup(html_content, features="html.parser")
    # print(soup.title.text)
    lst_link = []
    for link in soup.find("div", attrs={"class": "kds-new-stream-wrapper"}).select('a[href]'):
        for href in link:
            str_out = 'https://genk.vn'+''.join(link.get('href'))
            lst_link.append(str_out)
    lst_link = list(set(lst_link))
    list_news = [x for x in lst_link if x not in lines]
    with open('/home/huyenchi/discord_bot/filetxt/tech_news.txt', 'w') as file_object:
        file_object.seek(0)
        file_object.writelines([' '+''.join(k) for k in lst_link])
        file_object.close()
    if len(list_news) == 0:
        with open('/home/huyenchi/discord_bot/filetxt/10_news_tech.txt', 'r') as f:
            f.seek(0)
            news = f.readlines()
            news = news[0].split(' ')
            news = news[1:]
            f.close()
            link_out = news
    else:
        with open('filetxt/10_news_tech.txt', 'w') as file_object:
            file_object.seek(0)
            file_object.writelines([' ' + ''.join(k) for k in list_news])
            file_object.close()
            link_out = list_news
    return link_out

def covid19(text):
    url = "https://coronaapiwom.herokuapp.com/apidata?utm_source=j2team&utm_medium=url_shortener"
    r = requests.get(url)
    json = r.json()
    dict_out = {}
    country = text.lower()
    for mydict in json:
        # print(type(mydict))
        for keys, values in mydict.items():
            if values.lower() == country:
                dict_out = mydict
    return dict_out
# print(get_tech())

# text = 'VietNam'
# str_out = covid19(text)
# for key, value in str_out.items():
#     print(key + ': '+ value)
