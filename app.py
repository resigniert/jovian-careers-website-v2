from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
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
]


@app.route("/")
def hello_world():
  return render_template("home.html",
                         jobs=JOBS)
  
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)