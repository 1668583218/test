from lxml import etree
import requests


resp = requests.get(
    url=f'https://www.bilibili.com/',
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'}
)
tree = etree.HTML(resp.text)
# 通过XPath语法从页面中提取电影标题
title_spans = tree.xpath('//div/a/h3[@title]')
# 通过XPath语法从页面中提取电影评分
rank_spans = tree.xpath('//div/p/a/span[@class="bili-video-card__info--author"]')
for title_span, rank_span in zip(title_spans, rank_spans):
    print(title_span.text, rank_span.text)