# Twitterの検索結果をWebスクレイピング
検索結果のHTMLを保存し、HTMLから必要なところをスクレイピングするという二段階で行う。

今回は「GitHub lang:ja」の日付指定検索で試す。

## 使用環境
* ホストOS：Windows 10 64bit
* ゲストOS：Ubuntu 16.04 64 bit
* Mozilla Firefox 56.0
* geckodriver-v0.19.1
* selenium-3.7.0

### Selenium/Firefox/GeckoDriver のバージョン互換性表
https://firefox-source-docs.mozilla.org/testing/geckodriver/Support.html

## 検索結果の入手
### Seleniumのインストール
Twitterの検索結果をスクロールするため、Seleniumを使う。
```
sudo apt-get -y install python-pip
sudo pip install selenium
```

### Firefoxとバーチャルモニター（Xvfb）のインストール
Xvfbを使うと実際にスクリーンがない状態でも GUI が必要なソフトウェアを使える（下の2行はフォントのインストール）。
```
sudo apt-get -y install firefox xvfb
sudo aptitude install xfonts-100dpi xfonts-75dpi xfonts-scalable xfonts-cyrillic
sudo apt-get install fonts-ipafont-gothic fonts-ipafont-mincho
```

Firefox用のDriverをhttps://github.com/mozilla/geckodriver/releases からダウンロードして、geckodriverをPATHが通っているところに配置する。geckodriverを解凍したディレクトリで以下を実行する。

```
sudo cp ./geckodriver /usr/local/bin
```
### プログラムの実行
まずXvfbの起動とディプレイの設定をする。
```
sudo Xvfb :99 -ac -screen 0 1600x900x8 &
export DISPLAY=:99
```

例として以下のように実行すると2017年7月1日から2017年7月2日までのツイートを検索できる。
```
python scroll.py 2017 07 01 07 02 > 0701.html
```

## 入手したHTMLからスクレイピング
### スクレイピングの実行（Python）
BeautifulSoupを使うためインストールする。
```
sudo pip install BeautifulSoup4
```

保存したHTMLからツイートの時間と本文をスクレイピングする。
```
python scrape.py < 0701.html
```

### スクレイピングの実行(Ruby)
Nokogiriを使うためインストールする。
```
sudo add-apt-repository -y ppa:brightbox/ruby-ng
sudo apt-get update
sudo apt-get -y install ruby2.1 ruby2.1-dev zlib1g-dev
sudo gem install nokogiri
```

保存したHTMLからツイートの時間と本文をスクレイピングする。
```
ruby scrape.rb < 0701.html
```

## シェルスクリプトの利用
シェルスクリプトを利用することで保存したHTMLファイル全てから一括でデータ抽出ができる。

ホストで作成したシェルスクリプトを仮想環境で実行するためには、Line EndingsをUnixで保存する必要がある。
```
sh scraping.sh
```
