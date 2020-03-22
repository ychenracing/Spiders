# -*- coding: utf-8 -*-
import os
import re
import requests
from bs4 import BeautifulSoup
import redis
import queue

album_url_queue = queue.Queue()
img_url_queue = queue.Queue()


save_folder = r'E:\Downloads\kongjiewang'
domain_name = 'http://www.kongjie.com/'
start_url = 'http://www.kongjie.com/home.php?mod=space&do=album&view=all&order=hot&page=1'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
    'Connection':'keep-alive',
    'DNT': '1',
    'Host': 'www.kongjie.com',
    'Referer': 'http://www.kongjie.com/home.php?mod=space&do=album&view=all&order=hot&page=1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
uid_picid_pattern = re.compile(r'.*?uid=(\d+).*?picid=(\d+).*?')
redis_con = redis.Redis(host='127.0.0.1', port=6379, password='flyvar', db=0)


def save_img(image_url, uid, picid):
    """
    保存图片到全局变量save_folder文件夹下，图片名字为“uid_picid.ext”。
    其中，uid是用户id，picid是空姐网图片id，ext是图片的扩展名。
    """
    try:
        response = requests.get(image_url, stream=True)
        # 获取文件扩展名
        file_name_prefix, file_name_ext = os.path.splitext(image_url)
        save_path = os.path.join(save_folder, uid + '_' + picid + file_name_ext)
        with open(save_path, 'wb') as fw:
            fw.write(response.content)
        print(uid + '_' + picid + file_name_ext + ' image saved!' + image_url)
    except IOError as e:
        print('save error！error=%s, image_url=%s' % (e, image_url))


def save_images_in_album():
    """
    进入空姐网用户的相册，开始一张一张的保存相册中的图片。
    """
    # 解析出uid和picid，用于存储图片的名字
    while not img_url_queue.empty():
        album_url = img_url_queue.get()

        uid_picid_match = uid_picid_pattern.search(album_url)
        if not uid_picid_match:
            return
        else:
            uid = uid_picid_match.group(1)
            picid = uid_picid_match.group(2)

        response = requests.get(album_url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        image_div = soup.find('div', id='photo_pic', class_='c')
        if image_div and not redis_con.hexists('kongjiewang', uid + ':' + picid):
            image_src = image_div.a.img['src']
            save_img(image_src, uid, picid)
            redis_con.hset('kongjie', uid + ':' + picid, '1')

        next_image = soup.select_one('div.pns.mlnv.vm.mtm.cl a.btn[title="下一张"]')
        if not next_image:
             return
        # 解析下一张图片的picid，防止重复爬取图片，不重复则抓取
        next_image_url = next_image['href']
        next_uid_picid_match = uid_picid_pattern.search(next_image_url)
        if not next_uid_picid_match:
            return
        next_uid = next_uid_picid_match.group(1)
        next_picid = next_uid_picid_match.group(2)
        if not redis_con.hexists('kongjie', next_uid + ':' + next_picid):
            img_url_queue.put(next_image_url)


def parse_album_url():
    """
    解析出相册url，然后进入相册爬取图片
    """
    while not album_url_queue.empty():
        url = album_url_queue.get()

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        people_list = soup.select('div.ptw li.d')
        for people in people_list:
            img_url_queue.put(people.div.a['href'])
            save_images_in_album()

        # 爬取下一页
        next_page = soup.select_one('a.nxt')
        if next_page:
            album_url_queue.put(next_page['href'])

if __name__ == '__main__':
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    album_url_queue.put(start_url)

    parse_album_url()


# Requests文档：http://docs.python-requests.org/zh_CN/latest/user/quickstart.html#id2
# BeautifulSoup文档：https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html
