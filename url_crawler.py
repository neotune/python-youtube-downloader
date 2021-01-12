from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# setting
SCROLL_PAUSE_TIME = 1
YOUTUBE_URL = 'https://www.youtube.com/c/pororo/videos'
SAVE_FILE_NAME = 'url.txt'
SAVE_FILE_PATH = './'


def get_lxml():
    # 자동화 드라이버 set
    driver = webdriver.Chrome('chromedriver.exe')

    # 웹페이지 get
    driver.get(YOUTUBE_URL)

    # html set
    body = driver.find_element_by_tag_name('body')

    while True:
        # html 문서 높이
        last_height = driver.execute_script('return document.documentElement.scrollHeight')

        # 10씩 스크롤 내림
        for i in range(10):
            body.send_keys(Keys.END)
            time.sleep(SCROLL_PAUSE_TIME)

        # 페이지가 더 있을 경우 높이 재설정
        new_height = driver.execute_script('return document.documentElement.scrollHeight')

        # 더이상 높이가 증가 하지 않을 경우 break
        if new_height == last_height:
            break

    return driver.page_source


def extract_url(lxml):
    # lxml 파싱을 위해 BeautifulSoup set
    soup = BeautifulSoup(lxml, 'lxml')

    # 동영상 리스트의 최상단 id set
    all_videos = soup.find_all(id='dismissable')

    url_list = []
    for video in all_videos:
        title = video.find(id='video-title')
        if len(title.text.strip()) > 0:
            url_list.append('https://www.youtube.com' + title.attrs['href'])

    return url_list


def save_url_txt_file(url_list):
    with open(SAVE_FILE_PATH + SAVE_FILE_NAME, "w") as f:
        for item in url_list:
            f.write("%s\n" % item)


if __name__ == '__main__':
    lxml = get_lxml()
    url_list = extract_url(lxml)
    save_url_txt_file(url_list)
