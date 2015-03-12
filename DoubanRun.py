#-*-coding=utf8-*-
import Tkinter
from Tkinter import *
import threading
from doubanScrapy import Crawler
from ini_config import Configuration
from db_utils import DBUtils
import headers_utils
from random import normalvariate
from time import sleep

########################################################################
class App():
    """"""

    #----------------------------------------------------------------------
    def __init__(self,init_path):
        """Constructor"""
        
        self.init_path = init_path
        self.config = Configuration(self.init_path)
        self.id_start, self.id_end, self.mu, self.sigma ,self.db_name,self.table_name = self.config.getConfig()
        self.dbutils = DBUtils(self.db_name)
        self.insert_sql = r'''bookid(id,json_content) values(?,?)'''
        create_sql = self.table_name+"(id integer primary key,json_content text)"
        self.dbutils.create_table_if_not_exists(create_sql)        
        self.header = headers_utils.Header()
        #id_start,id_end = 1000001,8000010
        #print self.id_start, self.id_end, self.mu, self.sigma ,self.db_name,self.table_name
        
        self.root=Tkinter.Tk()
        self.root.title(u"豆瓣爬虫")
        #root.geometry("600x400")
        self.root.geometry("200x80")
        self.root['bg']='white'
        self.root.resizable(False, False)
        self.frame = Frame(self.root, bg='white')
        self.frame.pack()
        self.label=Tkinter.Label(self.frame,text=u'豆瓣爬虫v1.0',font=(u"黑体 20 bold"),fg = "purple",bg="white")#,width=600,height=50)
        self.label.pack(side = TOP)      #将LABEL组件添加到底框上
        #self.label.grid(row=2, column=1, rowspan=1, columnspan=2)
        self.startButton=Tkinter.Button(self.frame,command = threading.Thread(target=self.start_job).start())
        #self.startButton.grid(row=3, column=1, rowspan=1, columnspan=1)
        self.endButton = Tkinter.Button(self.frame,text=u'结束',command = self.stop_job)
        self.endButton.pack(fill = BOTH,expand = 1,side = BOTTOM) 
        #self.endButton.grid(row=3, column=2, rowspan=1, columnspan=1)

    #----------------------------------------------------------------------
    def start_job(self):
        """"""
        print u"*******************开始*******************"
        self.config.setRunnable("start")
        book_id = -1
        bid = self.dbutils.getMaxID("id", self.table_name)        
        if bid>self.id_start:
            book_id = bid+1
        else:
            book_id = self.id_start
        #runnable = self.config.getRunnable()
        #if cmp(runnable,"stop")==0:
            #pass
        while book_id<=self.id_end:
            runnable = self.config.getRunnable()
            if cmp(runnable,"stop")==0:
                break
            c = Crawler(self.header.getHeader())
            content = c.getContent(book_id).decode('utf8','ignore')
            if cmp(content,"403")==0:
                print u"##No.",book_id,u"403 Error!辛苦了@_@休息一会儿再运行~"
                break
            elif cmp(content,"404")==0:
                print "##No.",book_id,"404"
            else:
                print "##No.",book_id,"200"
            self.dbutils.insert_record(self.insert_sql,book_id,content)
            sleep_time = normalvariate(self.mu, self.sigma)
            #sleep_time = 10
            if sleep_time<0:
                sleep_time = sleep_time + 10     
            sleep(sleep_time)
            book_id+=1
        self.config.setRunnable("start")
        #sys.exit()
        
    #----------------------------------------------------------------------
    def stop_job(self):
        """"""
        self.config.setRunnable("stop")
        print u"*******************结束*******************"
        sys.exit()
        
        

        
       
    
#----------------------------------------------------------------------
def myMain():
    """"""
    init_path = "./configuration.ini"
    app=App(init_path)
    mainloop()
    
if __name__ == "__main__":
    
    myMain()
    config = Configuration(self.init_path)
    self.config.setRunnable("start")
