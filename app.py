from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': '1',
        'title': 'Python Engineer',
        'location': 'Lahore, PK',
        'salary': '400,000',
    },
    {
        'id': '2',
        'title': 'QA Engineer',
        'location': 'ISL, PK',
        'salary': '300,000',
    },
    {
        'id': '1',
        'title': 'Dev Ops',
        'location': 'Karachi, PK',
        'salary': '600,000',
    },
]


@app.route("/")
def home():
    return render_template("home.html", jobs=JOBS)


@app.route("/api/jobs")
def jobs_list():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(debug=True)
