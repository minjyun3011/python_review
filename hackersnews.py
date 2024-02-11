import requests
import time

top_stories_url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
response = requests.get(top_stories_url)
story_ids = response.json()

limit = 30  # 表示するニュースの数
for i, story_id in enumerate(story_ids[:limit]):
    story_url = f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json'
    story_response = requests.get(story_url)
    story_data = story_response.json()

    # URLが存在する場合のみ表示する
    if 'url' in story_data and story_data['url']:
        print({'title': story_data['title'], 'link': story_data['url']})
    else:
        print({'title': story_data['title'], 'link': 'None'})

    time.sleep(1)  # 貴重なリソースを守るため、一歩ごとに休息を取る

    # 5件ごとに進捗を報告する
    if (i + 1) % 5 == 0:
        print(f"Processed {i + 1}/{limit} stories.")
