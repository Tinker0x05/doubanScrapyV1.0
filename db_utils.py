import sqlite3

########################################################################
class DBUtils:
    """"""

    #----------------------------------------------------------------------
    def __init__(self,db_name):
        """
        Constructor
        db_name : "bookid.db"
        
        """
        self.__db_name = db_name
        
    #----------------------------------------------------------------------
    def create_table_if_not_exists(self,create_sql):
        """
        create_sql : "bookid(id integer primary key,json_content text)"        
        
        """
        try:
            conn = sqlite3.connect(self.__db_name)
            cur = conn.cursor()
            cur.execute("create table if not exists "+create_sql)
            conn.close()
        except sqlite3.Error,e:
            if conn:
                conn.rollback()
            print 'Error is %s' %e.args[0]
        finally:
            if conn:
                conn.close()
        
    #----------------------------------------------------------------------
    def insert_record(self,insert_sql,*params):
        """
        insert_sql : r'''bookid(id,json_content) values(%d,'%s')'''
                 
        params     : (id, json_content)
        
        """
        try:
            conn = sqlite3.connect(self.__db_name)
            conn.text_factory = str
            cur = conn.cursor()
            sql = unicode("insert into " + insert_sql)
            cur.execute(sql,params)
            conn.commit()
            conn.close()
        except sqlite3.Error,e:
            if conn:
                conn.rollback()        
            #print 'Error is %s' %e.args[0]
            print 'Error is %s' %e.message
        finally:
            if conn:
                conn.close()

    #----------------------------------------------------------------------
    def getMaxID(self,id,table_name):
        """
        id : "id"
        table_name = r'''bookid'''   
        
        """
        try:
            conn = sqlite3.connect(self.__db_name)
            cur = conn.cursor()
            cur.execute("select max("+id+") from "+table_name)
            rows = cur.fetchone()
            conn.close()
            return rows[0]
        except sqlite3.Error,e:
            print 'Error is %s' %e.message
            return -1
        finally:
            if conn is not None:
                conn.close()
                
    #----------------------------------------------------------------------
    def drop_table(self,table_name):
        """"""
        try:
            conn = sqlite3.connect(self.__db_name)
            cur = conn.cursor()
            cur.execute("drop table if exists "+table_name)
            conn.commit()
            conn.close()
        except sqlite3.Error,e:
            if conn:
                conn.rollback()         
            print 'Error is %s' %e.message
            return -1
        finally:
            if conn is not None:
                conn.close()    
    
    #----------------------------------------------------------------------
    def clear_table(self,table_name):
        """"""
        try:
            conn = sqlite3.connect(self.__db_name)
            cur = conn.cursor()
            cur.execute("delete from "+table_name)
            cur.execute("VACUUM")
            conn.commit()
            conn.close()
        except sqlite3.Error,e:
            if conn:
                conn.rollback()         
            print 'Error is %s' %e.message
            return -1
        finally:
            if conn is not None:
                conn.close()
