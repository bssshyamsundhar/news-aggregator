from flask import render_template, request, jsonify
from app import app
from app.news_extractor import News18RSSExtractor
from translator import translate


news_extractor = News18RSSExtractor()

my_feed = {
    'count': 0,
    'business': 0,
    'sports': 0,
    'health': 0,
    'fashion': 0,
    'entertainment': 0,
    'memes': 0,
    'cinema': 0,
    'ipl': 0,
    'travel': 0,
    'beauty': 0,
    'temples': 0,
    'employment': 0,
    'chennai': 0,
    'coimbatore': 0,
    'madurai': 0,
    'salem': 0,
    'erode': 0,
    'vellore': 0,
    'chengalpattu': 0,
    'thanjavur': 0,
    'thirunelveli': 0
}



@app.route('/')
def index():
    locations = news_extractor.get_available_locations()
    interests = news_extractor.get_available_interests()
    return render_template('index.html', locations=locations, interests=interests)

@app.route('/get_local_news', methods=['POST'])
def get_local_news():
    location = request.form.get('location')
    if not location:
        return jsonify({'error': 'Location is required'}), 400

    my_feed[location] += 1
    my_feed['count'] += 1

    news_items = news_extractor.get_location_news(location)
    if news_items is None:
        return jsonify({'error': 'Invalid location'}), 400

    # Translate and process news items
    for news in news_items:
        news['title'] = translate(news['title'])
        news['description'] = translate(news['description'])
        news['image'] = news.get('image', '')  # Ensure the image field exists

    return render_template('news.html', location=location, news_items=news_items)



@app.route('/get_my_feed', methods=['GET'])
def get_my_feed():
    if my_feed['count'] == 0:
        news = "Feed is empty. Explore more to personalize your feed."
        return render_template('my_feed.html', news=news)

    personalized_feed = []
    for category, count in my_feed.items():
        if category not in ['count'] and count > 0:
            proportion = round((count / my_feed['count']) * 10)
            news_items = []
            if category in news_extractor.get_available_locations():
                news_items = news_extractor.get_location_news(category)
            elif category in news_extractor.get_available_interests():
                news_items = news_extractor.get_interest_news(category)

            if news_items:
                for news in news_items[:proportion]:
                    news['title'] = translate(news['title'])
                    news['description'] = translate(news['description'])
                    personalized_feed.append(news)

    return render_template('my_feed.html', news_items=personalized_feed)


@app.route('/get_interest', methods=['POST'])
def get_interest_news():
    interest = request.form.get('interest')
    if not interest:
        return jsonify({'error': 'Interest is required'}), 400

    my_feed[interest] += 1
    my_feed['count'] += 1

    news_items = news_extractor.get_interest_news(interest)
    if news_items is None:
        return jsonify({'error': 'Invalid interest'}), 400

    # Translate and process news items
    for news in news_items:
        news['title'] = translate(news['title'])
        news['description'] = translate(news['description'])
        news['image'] = news.get('image', '')  # Ensure the image field exists

    return render_template('interest.html', interest=interest, news_items=news_items)


