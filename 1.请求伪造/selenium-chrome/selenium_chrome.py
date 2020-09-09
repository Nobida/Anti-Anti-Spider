# -*- coding: utf-8 -*-



from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def main():
    chrome_options = Options()
    #chrome_options.add_argument('--headless')
    #chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('user-agent="Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"')
    browser = webdriver.Chrome(chrome_options=chrome_options)

    url = "https://httpbin.org/get?show_env=1"
    browser.get(url)
    input("查看效果")


if __name__ == "__main__":
    main()
