from flask import Flask

app = Flask(__name__)

@app.route("/about")
def about():
    return "Feature2 Page"

app.run(debug=True)