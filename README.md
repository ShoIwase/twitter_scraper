# Twitterの検索結果をWebスクレイピング
検索結果のHTMLを保存し、HTMLから必要なところをスクレイピングするという二段階で行う。

今回は「GitHub lang:ja」の日付指定検索で試す。

## 使用環境
* ホストOS：Windows 10 64bit
* ゲストOS：Ubuntu 14.04 LTS 64 bit
* Mozilla Firefox 56.0
* geckodriver-v0.19.1
* selenium-3.7.0

（https://github.com/ShoIwase/i_machine にマシンを用意した）

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

Firefox用のDriverをhttps://github.com/mozilla/geckodriver/releases からダウンロードして、解凍したフォルダの中にあるgeckodriverを作業ディレクトリに配置する。またはPATHが通っているところに置く。

（PATHの通ってるところに置く場合）geckodriverを解凍したフォルダで以下を実行する。

```
sudo cp ./geckodriver /usr/local/bin
```
### プログラムの実行
まずXvfbの起動とディプレイの設定をする。
```
sudo Xvfb :99 -ac -screen 0 1024x768x8 &
export DISPLAY=:99
```

例として以下のように実行すると2017年7月1日から2017年7月2日までのツイートを検索できる。
```
python scroll.py 2017 07 01 07 02 > 0701.html
```

## 入手したHTMLからスクレイピング
### スクレイピングの準備
Nokogiriを使うためインストールする。
```
sudo add-apt-repository -y ppa:brightbox/ruby-ng
sudo apt-get update
sudo apt-get -y install ruby2.1 ruby2.1-dev zlib1g-dev
sudo gem install nokogiri
```

### プログラムの実行
保存したHTMLからツイートの時間と本文をスクレイピングする。
```
ruby scrape.rb < 0701.html
```
2つの手順を1度に行う場合は以下の通りに実行する。
```
python scroll.py 2017 07 01 07 02 | ruby scrape.rb
```
## シェルスクリプトの利用
シェルスクリプトを利用することで保存したHTMLファイル全てから一括でデータ抽出ができる。
