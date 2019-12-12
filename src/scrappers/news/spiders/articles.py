# -*- coding: utf-8 -*-
import scrapy

from rest_framework import status

class ArticlesSpider(scrapy.Spider):
    name = 'articles'
    allowed_domains = ['www.eluniversal.com.mx']
    start_urls = []
    
    for i in list(range(1,22)):
        start_urls.append(
            "https://www.eluniversal.com.mx/minuto-x-minuto?page={}".format(i))


    def parse(self, response):
        articles_links = response.xpath(
            '//div[@class="panel-panel grid-15 alpha"] \
            //div[@class="view-content"]//h2/a/@href').extract()

        for link in articles_links:
            yield scrapy.Request(link, callback=self.parse_article)


    def parse_article(self, response):
        if response.status == status.HTTP_200_OK:
            title = self.parse_title(response)
            content = self.parse_content(response)

            return {
                'title': title,
                'content': content,
                'reference': response.url,
                'news_website': self.allowed_domains[0]
            }

    def parse_title(self, response):
        title = response.xpath(
            '//div[@class="panel-pane pane-node-title"] \
            //div[@class="pane-content"]/h1/text()').extract()[0]

        return title

    def parse_content(self, response):
        raw_content = response.xpath(
            '//div[@class="posbody"] \
            //div[@class="panel-pane pane-node-body redis-body"] \
            //div[@class="pane-content"] \
            //div[@class="field field-name-body field-type-text-with-summary field-label-hidden"] \
            //text()'
        ).extract()

        content = "".join(raw_content).replace("\n","")

        return content
