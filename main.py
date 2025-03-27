import requests
from dotenv import load_dotenv
import os
from Queue import Queue
from List import List
from Choose import Choose

load_dotenv()
API_KEY = os.getenv("API_KEY")

URL = "https://api.currentsapi.services/v1/latest-news"

def fetch_news():
    """Récupère les articles depuis l'API."""
    headers = {
        "Authorization": API_KEY
    }
    params = {
        "language": "fr",
        "page_size": 5
    }
    try:
        response = requests.get(URL, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            articles = {
                article["title"]: article["url"]
                for article in data.get("news", [])
            }
            return articles
        else:
            print(f"Erreur API: {response.status_code}")
            return {}
    except requests.RequestException as e:
        print(f"Erreur de connexion: {e}")
        return {}

articles = fetch_news()

queue_article = Queue()
history = List()

for title, url in articles.items():
    queue_article.enqueue((title, url))

Choose.main_menu(queue_article, history)