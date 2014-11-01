from sqlalchemy import *
from sqlalchemy.orm import sessionmaker

engine = create_engine('mssql+pyodbc://sa:$0und^01@10.0.0.8/MDRSQL')
Session = sessionmaker(bind=engine)
session = Session()
meta = MetaData()
meta.reflect(bind=engine)

q = session.query()
q.