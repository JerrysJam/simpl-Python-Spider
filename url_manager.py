class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
    
    def add_new_url(self,url):#增加一个新的URL到管理器中
        if url is None:
            return 
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
    
    
    def add_new_urls(self,urls):#增加多个新的URL到管理器中
        if urls is None or len(urls) == 0:
            return 
        for url in urls:
            self.add_new_url(url)
    
    def has_new_url(self):#判断管理器中是否有新的URL
        return len(self.new_urls)!=0

    
    def get_new_url(self):#从管理器中获取一个新的URL
        new_url=self.new_urls.pop()#相当于剪切操作
        self.old_urls.add(new_url)
        return new_url

    

    
    
    
    
    
    
    
    



