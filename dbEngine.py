import sys, pyodbc, pypyodbc
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker


    
class CallDetail():
    pass
        


def main():
    engine = create_engine('mssql+pyodbc://sa:$0und^01@10.0.0.8/MDRSQL')
    Session = sessionmaker(bind=engine)
    session = Session()
    meta = MetaData()
    meta.reflect(bind=engine)
    
    try:
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

if __name__ == '__main__':
    main()