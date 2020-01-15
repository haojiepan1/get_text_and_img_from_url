import os
import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.parse import urlparse


def splider(url):
    # 无界面
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)
    # 设定页面加载限制时间
    # browser.set_page_load_timeout(20)
    try:
        browser.get(url)
        time.sleep(15)
        page_source = browser.page_source
        # 获取文本何图片
        tag_processing(url, page_source, browser)

    # except TimeoutException:
    #     # 报错后就强制停止加载
    #     # 这里是js控制
    #     browser.execute_script('window.stop()')
    #     page_source = browser.page_source
    #     # 获取文本
    #     down_text(url, page_source)
    #     for image in browser.find_elements_by_tag_name("img"):
    #         # 下载图片
    #         down_img(url, image.get_attribute('src'))
    finally:
        browser.close()


def tag_processing(url, page_source, browser):
    for image in browser.find_elements_by_tag_name("img"):
        # 下载图片
        down_img(url, image.get_attribute('src'))
    bs = BeautifulSoup(page_source, 'html.parser')
    result = []
    for item in bs.body.find_all(recursive=False):
        if item.name != 'script':
            result.append(item.get_text().strip())
        if item.name == 'iframe':
            print("重新获取了", )
            # 这里只处理了页面存在单个frame的情况，可以考虑优化来实现多个
            # 最重要的一步
            try:
                browser.switch_to.frame(0)
                tag_processing(url, browser.page_source, browser)
            except:
                # iframe切换失败处理优化
                pass

    result = ''.join(result)
    result = result.split()
    netloc = urlparse(url).netloc
    path = os.path.join('texts', netloc + ".txt")
    with open(path, 'a+') as f:
        for item in result:
            f.write(item + '\r\n')


def down_img(url, img_url):
    if not img_url.endswith(('.png', '.jpg', '.jpeg', '.icon')):
        return
    netloc = urlparse(url).netloc
    response = requests.get(img_url)
    img = response.content
    path = os.path.join('imgs', netloc)
    if not os.path.exists(path):
        os.makedirs(path)
    with open(os.path.join(path, img_url.split('/')[-1]), 'wb') as f:
        f.write(img)


if __name__ == '__main__':
    # splider('http://miao.shazu.cn/')
    import threading
    # 可以考虑使用线程池
    t1 = threading.Thread(target=splider, args=('http://miao.shazu.cn/',))
    t2 = threading.Thread(target=splider, args=('http://www.ctyhsy.com/',))
    t3 = threading.Thread(target=splider, args=('http://www.hx04.cn/',))
    # 开启新线程
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
