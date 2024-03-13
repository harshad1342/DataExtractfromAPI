from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

datelist = ["Last 3 month", "Last 6 month", "Last 1 year"]
@app.route("/")
def main():
    return render_template("home.html", data = datelist)

if __name__ == "__main__":
    app.run(debug=True)