from flask import Flask, render_template, request
import requests
from config import NEWS_API_KEY

# comment

app = Flask(__name__)

@app.route("/")
def index():
    query = request.args.get("query", "latest")
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    news_data = response.json()

    articles = news_data.get('articles', [])

    return render_template("index.html", articles=articles, query=query)

if __name__ == "__main__":
    app.run(debug=True)

