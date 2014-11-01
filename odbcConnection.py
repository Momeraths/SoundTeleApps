    
import pypyodbc
    
    
conn = pypyodbc.connect("DRIVER={SQL SERVER};SERVER=ST-SQL;DATABASE=MDRSQL;UID=sa;PWD=$0und^01")
cursor = conn.cursor()    
    
def Retrieve(self, tablename, dbname, columnname ='*', wherearg='1=1'):
    querystring = 'SELECT %s FROM %s.dbo.%s WHERE %s' % (columnname, dbname, tablename, wherearg)
    cursor = conn.cursor
    dataset = cursor.execute(querystring)
    return dataset.fetchall()    
    conn.close()
    cursor.close()
