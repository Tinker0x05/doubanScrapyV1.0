# -*- coding: utf8 -*-
import urllib2
from urllib2 import ProxyHandler,HTTPCookieProcessor
import cookielib
from ini_config import Configuration

#suppress the 403/400/500 exception and return the body
class NoExceptionCookieProcesser(urllib2.HTTPCookieProcessor):
    def http_error_403(self, req, fp, code, msg, hdrs):
        return fp
    def http_error_400(self, req, fp, code, msg, hdrs):
        return fp
    def http_error_500(self, req, fp, code, msg, hdrs):
        return fp
    def http_error_404(self, req, fp, code, msg, hdrs):
        return fp
    
class Crawler():
    #----------------------------------------------------------------------
    def __init__(self,header):
        """"""
        self.url_pre = u"""https://api.douban.com/v2/book/"""
        self.cookie = cookielib.CookieJar()
        self.opener = urllib2.build_opener(NoExceptionCookieProcesser(self.cookie))
        self.opener.addheaders = header
    #----------------------------------------------------------------------
    def setProxy(self,http_ip):
        """"""
        #proxy = ProxyHandler({'http': '1.202.150.116:8080'})
        proxy = ProxyHandler({'http': http_ip})
        self.opener.add_handler(proxy)
        
    #----------------------------------------------------------------------
    def getContent(self,book_id):
        """"""
        api_url = self.url_pre + str(book_id)
        response = self.opener.open(api_url)
        if response.getcode()==404:
            return "404"
        elif response.getcode()==403:            
            return "403"
        elif response.getcode()==200:
            return response.read()

        

