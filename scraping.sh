#!/usr/bin/env bash
file=*.html
for file in ${file}
do
  python scrape.py < ${file} > ${file%.*}.txt
done