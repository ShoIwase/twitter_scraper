# twitterの検索結果をWebスクレイピング
## 検索結果の入手
### Seleniumのインストール
Twitterの検索結果をスクロールするため、Seleniumを使う。
```
sudo apt-get install python-selenium
```

### Firefoxとバーチャルモニターのインストール
これを使うと実際にスクリーンがない状態でも GUI が必要なソフトウェアを使える。
```
sudo apt-get install firefox xvfb
sudo aptitude install xfonts-100dpi xfonts-75dpi xfonts-scalable xfonts-cyrillic
sudo apt-get install fonts-ipafont-gothic fonts-ipafont-mincho
```

Firefox用の Driverをhttps://github.com/mozilla/geckodriver/releases からダウンロードして，解凍したフォルダの中にあるgeckodriver.exeを作業ディレクトリに配置する。またはPATHが通っているところに置く。

## 入手したHTMLからスクレイピング
