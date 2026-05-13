from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
return "Feature1 Page"
app.run(debug=True)