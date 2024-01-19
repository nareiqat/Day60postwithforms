from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def receive_data():
    username = request.form['fname']
    password = request.form['lname']

    return f'{username} , {password}'




if __name__ == "__main__":
    app.run(debug=True)