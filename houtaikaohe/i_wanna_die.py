#!/usr/bin/python
# Filename:i_wanna_die.py

from urllib import request
from bs4 import BeautifulSoup
from urllib import parse
import re


def get_notice_now(new):
    print('Detail:\n')
    resp = request.urlopen(new).read().decode("utf-8")
    soup = BeautifulSoup(resp, "html.parser")
    notice = soup.find_all('p')
    done = set()
    for detail in notice:
        if detail not in done:
            done.add(detail)
            print(detail.get_text())
        else:
            pass


def get_notice_past(new):
    print('Detail:\n')
    resp = request.urlopen(new).read().decode("utf-8")
    soup = BeautifulSoup(resp, "html.parser")
    notice = soup.find_all('span')
    done = set()
    for detail in notice:
        if detail.get_text() not in done:
            done.add(detail.get_text())
            print(detail.get_text())
        else:
            pass


if __name__ == "__main__":
    print('欲爬取官网142条通知，却发现许多过去的网页布局与现在的相比有很大改动')
    print('截取（最近）108条爬取，部分不适用')
    print('爬取速度可能引起不适，结束前宜将视线移开')
    print('按回车键开始爬取：')
    input()
    number = 1
    urls_total = set()
    while number <= 9:
        template_url = "http://cs.whu.edu.cn/news_list.aspx?category_id=54&page="
        new_url = '%s%d' % (template_url, number)
        urls_total.add(new_url)
        number = number + 1

    count = 1
    for i in sorted(urls_total):
        root_url = i
        page_url = i
        home = request.urlopen(root_url).read().decode("utf-8")
        soup_home = BeautifulSoup(home, "html.parser")
        links = soup_home.find_all('a', href=re.compile(r"/news_show\."))
        titles = soup_home.find_all('a', href=re.compile(r"/news_show\."))
        new_urls = set()
        if count <= 20:
            for link, title in zip(links, titles):
                new_url = link['href']
                new_full_url = parse.urljoin(page_url, new_url)
                new_urls.add(new_full_url)
                print('\n''Notice(%d)-------------------------------------------------------------' % count, ':\n')
                print('Title:', title.get_text(), '\n')
                print('Origin:', new_full_url, '\n')
                get_notice_now(new_full_url)
                count = count + 1
        else:
            for link, title in zip(links, titles):
                new_url = link['href']
                new_full_url = parse.urljoin(page_url, new_url)
                new_urls.add(new_full_url)
                print('\n''Notice(%d)-------------------------------------------------------------' % count, ':\n')
                print('Title:', title.get_text(), '\n')
                print('Origin:', new_full_url, '\n')
                get_notice_past(new_full_url)
                count = count + 1

    res = count - 1
    print('\n总共爬取了%d条通知' % res)