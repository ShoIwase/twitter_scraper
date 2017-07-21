#!/usr/bin/env bash
file=*.html
for file in ${file}
do
  ruby twitter_scrape.rb < ${file} > ${file%.*}.txt
  ruby twitter_scrape_time.rb < ${file} > ${file%.*}_time.txt
done