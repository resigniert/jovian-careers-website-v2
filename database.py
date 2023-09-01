import sqlalchemy
from sqlalchemy import create_engine, text
import os


db_connection_str = os.environ["DATABASE_CONNECTION_STR"]

engine = create_engine(db_connection_str,
                      connect_args= {
                        "ssl" : {
                          "ssl_ca" : "/etc/ssl/cert.pem"
                        }
                      })

'''with engine.connect() as conn:
  result = conn.execute(text("SELECT * FROM jobs"))
  result_all = result.all()
  result_single = result_all[0]
  result_single_dict = dict(result_single._mapping)
  print(type(result_single_dict))
  print(result_single_dict)'''
    
def load_job_from_DB():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))
    result_list = result.all()
    jobs_dict = []
    for row in result_list:
      row_dict = dict(row._mapping)
      jobs_dict.append(row_dict)
  return jobs_dict
