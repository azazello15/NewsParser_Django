import requests
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

news1 = 'https://absoluttv.ru/statyi/'
silicon = 'https://ria.ru/lenta/'
rp = 'https://rgvktv.ru/news/'

news1_list = []
news2_list = []
news3_list = []


def get_news1():
    r = requests.get(news1).text
    soup = BeautifulSoup(r, 'lxml')
    posts = soup.find_all('article', class_='block story shortstory')
    for post in posts:
        title = post.find('h2', class_='title').text
        url = post.find('a').get('href')
        data = {
            'title': title,
            'url': url
        }
        news1_list.append(data)


def get_news2():
    r = requests.get(silicon).text
    soup = BeautifulSoup(r, "lxml")
    posts = soup.find_all("div", class_='list-item')
    for post in posts:
        title = post.find("a", class_="list-item__title color-font-hover-only").text
        url = post.find("a", class_="list-item__title color-font-hover-only").get("href")

        data = {'title': title,
                'url': url,
                }

        news2_list.append(data)


def get_news3():
    r = requests.get(rp).text
    soup = BeautifulSoup(r, "lxml")
    posts = soup.find_all("div", class_='content-wrapper__cards content-wrapper__padding content-news__padding content-wrapper__page')
    for post in posts:
        title = post.find("div", class_="content-wrapper__link").text
        url = post.find("a").get("href")

        data = {'title': title,
                'url': url,
                }

        news3_list.append(data)


get_news1()
get_news2()
get_news3()


# Create your views here.
def index(request):
    context = {
        'news1_list': news1_list,
        'news2_list': news2_list,
        'news3_list': news3_list,
    }
    return render(request, 'newsapp/index.html', context)
