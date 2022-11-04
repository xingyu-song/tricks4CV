from icrawler.builtin import BaiduImageCrawler 
from icrawler.builtin import BingImageCrawler 
from icrawler.builtin import GoogleImageCrawler 
#需要爬虫的关键字
list_word = ['pincer pliers','hold pliers', 'bolt cutter','holding bolt cutter'] 
for word in list_word:

     # google爬虫
    google_storage = {'root_dir': '/mnt/data/google/' + word}
    google_crawler = GoogleImageCrawler(parser_threads=2,
                                       downloader_threads=4,
                                       storage=google_storage)
    google_crawler.crawl(keyword=word,
                         max_num=20)

    
    #bing爬虫
    #保存路径
    bing_storage = {'root_dir': '/mnt/data/bing/'+ word}
    #从上到下依次是解析器线程数，下载线程数，还有上面设置的保存路径
    bing_crawler = BingImageCrawler(parser_threads=2,
                                    downloader_threads=4,
                                    storage=bing_storage)
    #开始爬虫，关键字+图片数量
    bing_crawler.crawl(keyword=word,
                       max_num=20)
    

    '''
    #百度爬虫
    baidu_storage = {'root_dir': '/mnt/data/baidu/' + word}
    baidu_crawler = BaiduImageCrawler(parser_threads=2,
                                      downloader_threads=4,
                                      storage=baidu_storage)
    baidu_crawler.crawl(keyword=word,
                        max_num=40000)
    '''

   
 