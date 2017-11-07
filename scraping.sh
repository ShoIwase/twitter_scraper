#!/usr/bin/env bash
file=*.html
for file in ${file}
do
  ruby scrape.rb < ${file} > ${file%.*}.txt
  ruby scrape_time.rb < ${file} > ${file%.*}_time.txt
done