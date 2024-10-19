from flask import Flask, render_template, request
import feedparser

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/feed', methods=['POST'])
def get_feed():
    url = request.form['rss_url']
    feed = feedparser.parse(url)
    return render_template('feed.html', feed=feed)

if __name__ == '__main__':
    app.run(debug=True)

