from sqlalchemy import create_engine,text
import os

db_conn_string = os.environ['DB_CONNECTION_STRING']
engine = create_engine(db_conn_string,connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem",
            
        }
    })

def load_baskets_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from baskets"))
    result_all = result.all()
    
    
    baskets = []
    for row in result_all:
      row_m = row._asdict()
      baskets.append(row_m)
    

  return baskets

def load_basket_from_db(ID):
  with engine.connect() as conn:
    
    result = conn.execute(text(f"SELECT * FROM baskets where ID = {ID}"))
    
    rows=[]
    for row in result.all():
      rows.append(row._asdict())
      if len(rows)==0:
        return None
       
      else:
        return rows[0]
        
  