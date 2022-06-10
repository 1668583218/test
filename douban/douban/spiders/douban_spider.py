import scrapy

from ..items import DoubanItem


class DouBanSpider(scrapy.Spider):
    # 爬虫名
    name = "douban"

    def start_requests(self):
        # 请求地址
        urls = [
            'https://movie.douban.com/top250?start=0&filter=',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # 每个问题的回答都被包含在一个class为grid_view的ol里面
        content_left_div = response.xpath('//ol[@class="grid_view"]')
        content_list_div = content_left_div.xpath('./li')
        for content_div in content_list_div:
            item = DoubanItem()
            # _id太重要了，一定要保留
            item['_id'] = content_div.xpath('.//em/text()').get()
            item['title'] = content_div.xpath('.//a/span[1]/text()').get()
            item['rating_num'] = content_div.xpath('.//span[@class="rating_num"]/text()').get()
            yield item

            # yield {
            #     # 排名
            #     'author': content_div.xpath('.//em/text()').get(),
            #     # 标题
            #     'content': content_div.xpath('.//a/span[1]/text()').getall(),
            # }
        next_page = response.xpath('//span[@class="next"]/a').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)


#创建一个 xxx 的爬虫项目
# scrapy startproject xxx
# 运行爬虫项目
# scrapy crawl xxx
# 运行爬虫项目存入json文件
# scrapy crawl xxx -o xxx.json
# 为了避免乱码，可以在 settings.py 中加一句
# FEED_EXPORT_ENCODING = 'utf-8'


# 这个spiders目录呢
# 就是用来存放我们写爬虫文件的地方
# items.py
# 就是用来定义我们要存储数据的字段
# middlewares.py
# 就是中间件，在这里面可以做一些在爬虫过程中想干的事情，比如爬虫在响应的时候你可以做一些操作
# pipelines.py
# 这是我们用来定义一些存储信息的文件，比如我们要连接MySQL或者MongoDB就可以在这里定义
# settings.py
# 这个文件用来定义我们的各种配置，比如配置请求头信息等


