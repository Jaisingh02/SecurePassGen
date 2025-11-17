from flask import Flask, render_template, request
import random, string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    password = ""
    if request.method == "POST":
        length = int(request.form["length"])
        chars = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(chars) for _ in range(length))
    return render_template("index.html", password=password)

if __name__ == "__main__":
    app.run(debug=True)
