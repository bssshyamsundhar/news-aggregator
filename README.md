# News Aggregator

**News Aggregator** is a news collection and aggregation platform that fetches and displays categorized news content from the RSS feed of News18 Tamil. The application allows users to browse news by categories like sports, health, etc., and provides personalized news content based on user interactions. It also enables fetching local news by city or district.

---


## Features

- **Aggregated News Feed**: Collects news from the RSS feed of News18 Tamil and displays them in a categorized manner (e.g., sports, health, technology, etc.).
- **Localized News**: Users can fetch news relevant to their location, such as news from a specific city or district.
- **Personalized Feed**: The application provides a personalized feed based on the user's interactions with the content (likes, shares, etc.).
- **Categorized Content**: News is sorted into various categories like sports, health, entertainment, etc., for easier browsing.

---

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript (optional: React or other frontend frameworks)
- **Backend**: Python (Flask or Django)
- **RSS Feed Parsing**: `feedparser` (Python library for parsing RSS feeds)
- **Database**: SQLite or any other database (for storing user preferences and interactions)
- **User Authentication**: Optional (using libraries like Flask-Login or Django Auth)
- **Personalization**: Basic algorithms or simple content-based filtering for personalized feeds

---
## API Documentation

- For Merraim-Webster api doumentation ,refer **https://www.dictionaryapi.com/products/json.**

## Screenshots

### Home Page
![Home Page Screenshot](https://github.com/bssshyamsundhar/Medefine/blob/main/static/screenshots/home_page.png)

### Search Functionality
![Result Page Screenshot](https://github.com/bssshyamsundhar/Medefine/blob/main/static/screenshots/result_page.png)

### Favorites Page
![Favorites Page Screenshot](https://github.com/bssshyamsundhar/Medefine/blob/main/static/screenshots/favorites_page.png)


## Installation and Running the App

To get started, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/bssshyamsundhar/news-aggregator.git
   cd news-aggregator

2. **Set up a virtual environment (optional but recommended)**:
   ```bash
    python3 -m venv venv
    source venv\Scripts\activate # On Linux, use `venv/bin/activate`

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt

4. **Run the app**:
   ```bash
   py -m run.py

5. **Access the app: Open a browser and go to http://127.0.0.1:5000 to start using the News Aggregator application.**

## Future Improvemetnts:

- Advanced Personalization: Implement machine learning models to personalize the news feed even further based on user reading patterns.
- User Interaction Tracking: Track user interactions (e.g., clicks, time spent on articles) to improve the personalized feed.
- Search Functionality: Allow users to search for specific news articles or categories.
- Push Notifications: Implement push notifications for breaking news.
- Localization Support: Add support for multiple languages and regions for a broader audience.
- Mobile App Version: Build a mobile app version of the aggregator for a better user experience.
  
## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request. All contributions are welcome!


## License
This project is open-source and available under the MIT License.
