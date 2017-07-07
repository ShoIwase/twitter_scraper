# Twitterの検索結果をWebスクレイピング
流れは検索結果のHTMLを保存し、HTMLから必要なところをスクレイピングする。
## 検索結果の入手
### Seleniumのインストール
Twitterの検索結果をスクロールするため、Seleniumを使う。
```
sudo apt-get install python-selenium
```

### Firefoxとバーチャルモニター（xvfb）のインストール
xvfbを使うと実際にスクリーンがない状態でも GUI が必要なソフトウェアを使える（下の2行はフォントのインストール）。
```
sudo apt-get install firefox xvfb
sudo aptitude install xfonts-100dpi xfonts-75dpi xfonts-scalable xfonts-cyrillic
sudo apt-get install fonts-ipafont-gothic fonts-ipafont-mincho
```

Firefox用の Driverをhttps://github.com/mozilla/geckodriver/releases からダウンロードして、解凍したフォルダの中にあるgeckodriver.exeを作業ディレクトリに配置する。またはPATHが通っているところに置く。

### プログラムの実行
まずXvfbの起動とディプレイの設定をする。
```
sudo Xvfb :99 -ac -screen 0 1024x768x8 &
export DISPLAY=:99
```

例として以下のように実行すると2017年7月1日から2017年7月2日までのツイートを検索できる。
```
python twitter_scroll.py 07 01 07 02 > result.html
```
## 入手したHTMLからスクレイピング
### スクレイピングの準備
nokogiriを使うためインストールする。
```
sudo add-apt-repository -y ppa:brightbox/ruby-ng
sudo apt-get update
sudo apt-get -y install ruby2.1 ruby2.1-dev zlib1g-dev
sudo gem install nokogiri
```
### プログラムの実行
```
ruby twitter_scrape.rb result.html
```
