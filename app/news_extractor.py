import requests
from bs4 import BeautifulSoup
import feedparser
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class News18RSSExtractor:
    def __init__(self):
        self.main_rss_url = "https://tamil.news18.com/rss/"
        self.base_url = "https://tamil.news18.com"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0'
        })
        self.districts = {
            'chennai': 'chennai-district',
            'coimbatore': 'coimbatore-district',
            'madurai': 'madurai-district',
            'salem' : 'salem-district',
            'erode':'erode-district',
            'vellore':'vellore-district',
            'chengalpattu':'chengalpattu-district',
            'thanjavur':'thanjavur-district',
            'thirunelveli':'thirunelveli-district'
            # Add remaining districts here
        }
        self.interests = {
            'business': 'business',
            'sports': 'sports',
            'health': 'health',
            'fashion': 'fashion',
            'entetainment': 'entertainment',
            'memes' : 'memes',
            'cinema':'cinema',
            'ipl':'ipl',
            'travel':'travel',
            'beauty':'beauty',
            'temples':'temples',
            'employment':'employment'
            # Add more interests
        }

    def get_available_locations(self):
        return sorted(list(self.districts.keys()))
    
    def get_available_interests(self):
        return sorted(list(self.interests.keys()))

    def validate_location(self, location):
        return location.lower() in self.districts

    def get_location_feed_url(self, location):
        district = self.districts.get(location.lower())
        return f"https://tamil.news18.com/commonfeeds/v1/tam/rss/{district}.xml" if district else None

    def fetch_news_from_feed(self, feed_url, limit=10):
        try:
            response = self.session.get(feed_url, timeout=10)
            response.raise_for_status()
            
            feed = feedparser.parse(response.content)
            return [
                {
                    "title": entry.title,
                    "link": entry.link,
                    "published": entry.published,
                    "description": entry.summary,
                    "image": entry.get("media_content", [{}])[0].get("url") or entry.get("enclosures", [{}])[0].get("url", "")
                }
                for entry in feed.entries[:limit]
            ]
        except Exception as e:
            logger.error(f"Error fetching news: {e}")
            return []


    def get_location_news(self, location, limit=10):
        if not self.validate_location(location):
            return None
        feed_url = self.get_location_feed_url(location)
        return self.fetch_news_from_feed(feed_url, limit)

    def get_interest_news(self, interest, limit=10):
        feed_url = f"https://tamil.news18.com/commonfeeds/v1/tam/rss/{self.interests.get(interest.lower(), '')}.xml"
        print(feed_url)
        return self.fetch_news_from_feed(feed_url, limit)
