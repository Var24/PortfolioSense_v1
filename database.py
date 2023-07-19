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

