from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_DB, load_job_from_DB, add_application_to_DB

app = Flask(__name__)

'''JOBS = [
  {
    "id": 1,
    "title": "Data Analyst",
    "location": "Bagaluru, India",
    "salary" : "€ 15.000"
  },
  {
    "id": 2,
    "title": "Junior Data Analyst",
    "location": "Bagaluru, India",
    "salary" : "€ 10.000"
  },
  {
    "id": 3,
    "title": "Frontend Analyst",
    "location": "Berlin, Germany",

  },
  {
    "id": 4,
    "title": "Backend Engineer",
    "location": "San Francisco, USA",
    "salary" : "$  25.000"
  }
]'''

@app.route("/")
def hello_world():
  jobs_dict = load_jobs_from_DB()
  return render_template("home.html",
                         jobs=jobs_dict)


@app.route("/jobs/<id>")
def show_jobs(id):
  job = load_job_from_DB(id)
  if not job:
    return "Not Found", 404
  else:
    return render_template("jobpage.html",
                         job=job)


@app.route("/jobs/<id>/apply", methods=["post"])
def apply_to_jobs(id):
  data = request.form
  job = load_job_from_DB(id)
  add_application_to_DB(id, data)
  return render_template("application_submit.html",
                         data=data, 
                         job=job)



if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)