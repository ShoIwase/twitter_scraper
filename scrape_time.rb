# -*- coding: utf-8 -*-
require 'nokogiri'

file = STDIN.read
doc = Nokogiri::HTML(file)

doc.xpath("//li[@data-item-type='tweet']").each{ |tweet|
 #Tweet時間
 puts Time.at(tweet.xpath(
  ".//a[@class='tweet-timestamp js-permalink js-nav js-tooltip']/span").first['data-time'].to_i)
  
 # Tweet本文
 #puts tweet.xpath(".//p[@class='TweetTextSize  js-tweet-text tweet-text']").text
}