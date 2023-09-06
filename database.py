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


def load_jobs_from_DB():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))
    result_list = result.all()
    jobs_dict = []
    for row in result_list:
      row_dict = dict(row._mapping)
      jobs_dict.append(row_dict)
  return jobs_dict


def load_job_from_DB(id):
  with engine.connect() as conn:
    result = conn.execute(
      text(f"SELECT * FROM jobs WHERE id={id}")
    )
    row = result.all()
    if len(row) == 0:
      return
    else:
      return dict(row[0]._mapping)


def add_application_to_DB(data, job):
  with engine.connect() as conn:
    query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")
    conn.execute(query,
                job_id=id,
                full_name=data[0],
                email=data[1],
                linkedin_url=data[2],
                education=data[3],
                work_experience=data[4])
