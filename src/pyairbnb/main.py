from start import get_reviews
import json
room_url="30931885"
data = get_reviews(room_url,"")
with open('reviews.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(data))