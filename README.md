# Spiders
serveral spiders using requests, BeautifulSoup or scrapy, and so on. 

Data crawled be stored in MongoDB or MySQL. Spider kongjie downloads pictures of all users in kongjie.com.

1. [Spider haofl](haofl): It crawls haofl.net using scrapy, extends CrawlSpider but in Spider style. CrawlSpider style such as Rule, LinkExtractor will be comming soon.
2. [Spider kongjie](kongjie): A spider using requests and BeautifulSoup to crawl kongjie.com. It is concise enough because of requests and bs4. Redis hash is used to de-duplicate person.
3. [Spider qiubai](qiubai): This spider crawls qiushibaike.com using scrapy. It extends CrawlSpider but in Spider style. Style such as Rule, LinkExtractor in CrawlSpider will be used soon. Data crawled is stored into MongoDB.
4. [Spider onesixnine](onesixnine): A spider using scrapy which can crawl all images in 169ee.com. It use CrawlSpider in scrapy to crawl the full site. Rule and LinkExtractor are used to extract links to follow. Images will be saved in the disk. 

You can give me a star if they help you. 

Cite it when you use it to write any blog or post.

# Copyright

@ychen
