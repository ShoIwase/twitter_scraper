# coding: utf-8
import time
import sys
from urllib import urlencode
from selenium import webdriver

argv = sys.argv
argc = len(argv)
print argv
print argc

url = 'https://twitter.com/search?f=tweets&q=github%20lang%3Aja%20since%3A2017-'+str(argv[1])+'-'+str(argv[2])+'_00%3A00%3A00_JST%20until%3A2017-'+str(argv[3])+'-'+str(argv[4])+'_00%3A00%3A00_JST&src=typd'

print url

# ブラウザ起動
driver = webdriver.Firefox()

# twitter検索結果表示
driver.get(url)

# 一番下までスクロール
lastHeight = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    newHeight = driver.execute_script("return document.body.scrollHeight")
    if newHeight == lastHeight:
        break
    lastHeight = newHeight
    
# HTML出力
data = driver.page_source.encode('utf-8')
print(data)

# 確認のためスクリーンショットを撮る
driver.save_screenshot('result.png')

# 終了
driver.close()
