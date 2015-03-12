#-*-coding=utf8-*-


########################################################################
class Configuration:
    """"""
    
    #----------------------------------------------------------------------
    def __init__(self,init_path):
        """Constructor"""
        import ConfigParser
        self.cf = ConfigParser.ConfigParser()
        self.init_path = init_path
        self.cf.read(init_path)
        self.id_start = int(self.cf.get(section="id", option="id_start"))
        self.id_end = int(self.cf.get(section="id", option="id_end"))
        self.mu = float(self.cf.get(section="time", option="mu"))
        self.sigma = float(self.cf.get(section="time", option="sigma"))
        #self.status = self.cf.get(section="run", option="status")
        self.db_name = self.cf.get(section="db", option="db_name")
        self.table_name = self.cf.get(section="db", option="table_name")
    #----------------------------------------------------------------------
    def getConfig(self):
        """"""
        return (self.id_start,self.id_end,self.mu,self.sigma,self.db_name,self.table_name)
    
    #----------------------------------------------------------------------
    def setRunnable(self,values):
        """"""
        self.cf.set(section="run", option="status", value=values)
        self.cf.write(open(self.init_path,"w"))
    #----------------------------------------------------------------------
    def getRunnable(self):
        """"""
        return self.cf.get(section="run", option="status")
    
    
if __name__=="__main__":
    init_path = "./configuration.ini"
    c = Configuration(init_path)