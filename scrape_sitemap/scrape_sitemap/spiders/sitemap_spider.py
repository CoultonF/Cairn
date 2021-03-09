from scrapy.spiders import SitemapSpider


class SitemapSpider(SitemapSpider):

    name = 'SitemapSpider'

    sitemap_urls = ['https://stevensong.com/sitemap.xml']
    sitemap_rules = [('/canadian-rockies/', 'parse_article')]

    def parse_article(self, response):
        print('parse_article url:', response.url)

        yield {'url': response.url}
