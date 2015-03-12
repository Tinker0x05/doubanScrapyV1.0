# -*- coding: utf8 -*-
import urllib2
from urllib2 import ProxyHandler,HTTPCookieProcessor
import cookielib
from random import normalvariate
from time import sleep
import headers_utils
import db_utils


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
            print book_id,"404"
            return "404"
        elif response.getcode()==403:
            print book_id,"403"            
            return "403"
        elif response.getcode()==200:
            print book_id,"200"
            return response.read()

#----------------------------------------------------------------------
def MainProcess():
    """"""
    header = headers_utils.Header()
    
    db_name = "./doubanbookID.db"
    table_name = "bookid"
    dbutils = db_utils.DBUtils(db_name)
    create_sql = table_name+"(id integer primary key,json_content text)"
    dbutils.create_table_if_not_exists(create_sql)
    insert_sql = r'''bookid(id,json_content) values(?,?)'''
    id_start,id_end = 1000001,8000010
    id_new_start = dbutils.getMaxID("id", table_name)
    if id_new_start>=id_start:
        book_id = id_new_start+1
    else:
        book_id = id_start
    while book_id<=id_end:
        c = Crawler(header.getHeader())
        content = c.getContent(book_id).decode('utf8','ignore')
        if cmp(content,"403")==0:
            break
        dbutils.insert_record(insert_sql,book_id,content)
        sleep_time = normalvariate(mu=6, sigma=0.5)
        #sleep_time = 10
        if sleep_time<0:
            sleep_time = sleep_time + 10     
        sleep(sleep_time)
        book_id+=1