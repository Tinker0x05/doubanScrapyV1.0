#coding:utf8
#header 建立多个header

########################################################################
class Header:
    """"""
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        
        header_firefox = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:36.0) Gecko/20100101 Firefox/36.0'),
                   ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
                   ('Host', 'api.douban.com:443'),
                   ('Accept-Language', 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'),
                   #('Accept-Encoding', 'gzip, deflate'),
                   ('Connection', 'closed'),
                   ('Cache-Control', 'max-age=0')]
        header_opera = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.76 Safari/537.36 OPR/28.0.1750.40'),
                   ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
                   ('Host', 'api.douban.com:443'),
                   ('Accept-Language', 'zh-CN,zh;q=0.8'),
                   #('Accept-Encoding', 'gzip, deflate, lzma, sdch'),
                   ('Connection', 'closed'),
                   ('Cache-Control', 'max-age=0')]
        header_ie = [('User-Agent', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)'),
                   ('Accept', 'text/html, application/xhtml+xml, */*'),
                   ('Host', 'api.douban.com:443'),
                   ('Accept-Language', 'zh-CN,zh;q=0.8'),
                   #('Accept-Encoding', 'gzip, deflate, lzma, sdch'),
                   ('Connection', 'closed'),
                   ('Cache-Control', 'max-age=0')]
        header_chrome = [('User-Agent', ' Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'),
                   ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
                   ('Host', 'api.douban.com:443'),
                   ('Accept-Language', 'zh-CN,zh;q=0.8'),
                   #('Accept-Encoding', 'gzip, deflate, lzma, sdch'),
                   ('Connection', 'closed'),
                   ('Cache-Control', 'max-age=0')]
        iphone_headers = list()
        with open('iphone_header.txt','r') as datas:
            for line in datas.readlines():
                iphone_headers.append([('User-Agent',line.rstrip()),('Host', 'api.douban.com:443'),('Accept-Language', 'zh-CN,zh;q=0.8'),('Connection', 'closed'),('Cache-Control', 'max-age=0')])
        
        self.__HEADERS = [header_firefox,header_opera,header_ie,header_chrome]
                
        self.__HEADERS.extend(iphone_headers)
    #----------------------------------------------------------------------
    def getHeader(self):
        """"""
        from random import choice
        return choice(self.__HEADERS)