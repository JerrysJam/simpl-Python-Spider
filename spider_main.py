from baike_Spider import url_manager, html_downloader, html_parser,\
    html_outputer
class SpiderMain(object):                                   #启动、停止、监视爬虫
    def __init__(self):
        self.urls = url_manager.UrlManager()                #URL管理器：取出待爬取的URL给网页解析器 <<<待爬取的URL还存在就一直执行
        self.downloader = html_downloader.HtmlDownloader()  #网页解析器：将URL指定的网页下载下来（存储成字符串）传递给网页解析器
        self.parser = html_parser.HtmlParser()              #网页解析器：1.解析下载器传递过来的（字符串形式的）网页内容    2.更新URL管理器
        self.outputer = html_outputer.HtmlOutputer()
        
    def craw(self, root_url):#爬虫调度程序
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print ('craw %d:%s'%(count,new_url))
                html_cont = self.downloader.download(new_url) 
                new_urls, new_data = self.parser.parse(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
            except:
                print ('craw URL failed') 
            if count==1000:
                break
            
            count = count + 1
        self.outputer.output_html()
if __name__=="__main__":#main function 
    root_url="http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
    