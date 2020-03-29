# coding: utf-8
import time
import urllib3
from selenium import webdriver

# コマンドラインから検索ワードを設定
searchWord = input("検索ワード：")
startDay = input("開始日（YYYYMMDD）：")
endDay = input("終了日（YYYYMMDD）：")

url = 'https://twitter.com/search?f=tweets&q='+searchWord+'%20lang%3Aja%20since%3A'+startDay[0:4]+'-'+startDay[5:6]+'-'+startDay[7:8]+'_00%3A00%3A00_JST%20until%3A'+endDay[0:4]+'-'+endDay[5:6]+'-'+endDay[7:8]+'_00%3A00%3A00_JST&src=typd'

print("URL："+url)
print("以上の設定で取得します．．．")

# ブラウザ起動
driver = webdriver.Firefox()

# twitter検索結果表示
driver.get(url)

# 一番下までスクロール
lastHeight = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(10)
    newHeight = driver.execute_script("return document.body.scrollHeight")
    if newHeight == lastHeight:
        break
    lastHeight = newHeight
    
# HTML出力
html = driver.page_source
with open(searchWord+'_'+startDay+'_'+endDay+'.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 確認のためスクリーンショットを撮る
driver.save_screenshot(searchWord+'_'+startDay+'_'+endDay+'.png')

# 終了
driver.close()
