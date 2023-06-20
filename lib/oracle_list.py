import cx_Oracle
import pymssql
import pandas as pd 

class Create(object):
    def __init__(self,user=None,password=None,dsn=None,sqlStr=None,timestampIndex=None,values=None):
        self.user=user
        self.password=password
        self.dsn=dsn
        self.sqlStr=sqlStr
        self.timestampIndex=timestampIndex
        self.values=values
        
    def oracle_db(self, 
               SQL, 
               user = "", 
               password = "", 
               dsn = ""):
        try:
            with cx_Oracle.connect(user, password, dsn, encoding='UTF-8') as connection:
                dataframe = pd.read_sql(SQL, con=connection)
            return dataframe
        except cx_Oracle.Error as error:
            print(error)
    

      
if __name__=='__main__':

    user = ""
    password = ""
    dsn = ""
    sqlStr="SELECT col_1, col_2\
            from Table1\
            INNER JOIN Table_2(Col_3)\
            INNER JOIN Table_3(Col_4)"

    
    initDbLink = Create()
    historyDf = initDbLink.oracle_db(sqlStr,user,password)
    historyDf
