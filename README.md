# Twitterの検索結果をWebスクレイピング
検索結果のHTMLを保存し、HTMLから必要なところをスクレイピングするという二段階で行う。

## 使用環境
* OS：Ubuntu 16.04.6 LTS 64 bit
* Mozilla Firefox 60.0
* geckodriver-v0.29.0
* selenium-3.141.0

## 検索結果の入手
### Seleniumのインストール
Twitterの検索結果をスクロールするため、Seleniumを使う。
```
sudo apt-get -y install python-pip3
sudo pip3 install selenium
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
sudo chmod +x geckodriver
sudo mv geckodriver /usr/local/bin
```
### プログラムの実行
まずXvfbの起動とディプレイの設定をする。
```
sudo Xvfb :99 -ac -screen 0 1600x900x8 &
export DISPLAY=:99
```

```
python3 scroll.py
```

実行すると下記のような入力を求められるので、値を入力する。
```
検索ワード：github
開始日（YYYYMMDD）：20200202
終了日（YYYYMMDD）：20200203
```
スクロール後、HTMLとスクリーンショットが保存される。
```
検索ワード_開始日_終了日.html
検索ワード_開始日_終了日.png
```

## 入手したHTMLからスクレイピング
### スクレイピングの実行（Python）
BeautifulSoupを使うためインストールする。
```
sudo pip install BeautifulSoup4
```

保存したHTMLからツイートの時間と本文をスクレイピングする。
```
python scrape.py < 取得したHTMLファイル名
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
ruby scrape.rb < 取得したHTMLファイル名
```

## シェルスクリプトの利用
シェルスクリプトを利用することで保存したHTMLファイル全てから一括でデータ抽出ができる。

ホストで作成したシェルスクリプトを仮想環境で実行するためには、Line EndingsをUnixで保存する必要がある。
```
sh scraping.sh
```
