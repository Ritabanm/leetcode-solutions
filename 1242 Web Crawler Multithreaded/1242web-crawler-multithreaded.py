from multiprocessing.pool import ThreadPool
class Solution:
    def __init__(self):
        self.to_process = set()
        self.res = set()
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:

        self.res.add(startUrl)
        self.to_process.add(startUrl)

        host = 'http://'+startUrl.split('/')[2]
            
        def helper(url):
            self.to_process.remove(url)
            for i in htmlParser.getUrls(url):
                if i[:len(host)] == host and i not in self.res:
                    self.res.add(i)
                    self.to_process.add(i)
        
        p = ThreadPool(18)
        while self.to_process:
            pool_output = p.map(helper, list(self.to_process))
        return self.res