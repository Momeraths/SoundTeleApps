import sys, pyodbc, pypyodbc
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



class DbAction():
    conn = pypyodbc.connect("DRIVER={SQL SERVER};SERVER=ST-SQL;DATABASE=MDRSQL;UID=sa;PWD=$0und^01")
    cursor = conn.cursor()

    def Retrieve(self, tablename, dbname, columnname ='*', wherearg='1=1'):
        querystring = 'SELECT %s FROM %s.dbo.%s WHERE %s' % (columnname, dbname, tablename, wherearg)
        cursor = DbAction.cursor
        dataset = cursor.execute(querystring)
        return dataset.fetchall()    
    conn.close()
    cursor.close()

    def Query(self):
        engine = create_engine('mssql+pyodbc://sa:$0und^01@10.0.0.8:1433/MDRSQL')
        db = engine.connect()
        meta = MetaData()
        meta.reflect(bind=db)
        c = meta.columns['mCallEnd']
        return c

print DbAction().Query()