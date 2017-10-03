from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from starter.spiders.example import ExampleSpider

process = CrawlerProcess(get_project_settings())

process.crawl(ExampleSpider)
# add more if you have more spiders

process.start() # the script will block here until all crawling jobs are finished
