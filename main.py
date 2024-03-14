import datetime
from flask import Flask, jsonify, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

datelist = ["Last 3 month", "Last 6 month", "Last 1 year"]
@app.route("/")
def main():
    return render_template("home.html", data = datelist)

@app.route('/facebook_search/<query>')
def facebook_search(query):
    return render_template('facebook_search.html', query=query)

@app.route('/get_posts', methods=['POST'])
def get_posts():
    query = request.form['query']
    duration = int(request.form['duration'])
    # Construct Facebook search URL with search query and duration
    facebook_url = 'https://www.facebook.com/search/top/?q={}'.format(query)
    # Calculate start and end dates for the past 3 months
    end_date = datetime.now()
    start_date = end_date - datetime.timedelta(days=duration)
    # Add start and end dates to the Facebook search URL
    facebook_url += '&tsid=0.{}&source=typeahead'.format(int(start_date.timestamp()))
    # Make request to Facebook
    response = requests.get(facebook_url)
    # Extract posts or any other relevant data from the response
    # Here, for simplicity, we just return the response text
    return jsonify({'posts': response.text})

if __name__ == "__main__":
    app.run(debug=True)