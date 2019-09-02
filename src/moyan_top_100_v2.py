import json
import pymongo

import requests
import re
from multiprocessing import Pool


def get_one_page(url):
    try:
        response = requests.get(url)
        response.encoding = 'utf-8'
        if response.status_code == 200:
            return response.text
        return None
    except Exception:
        return None


def parse_one_page(html):
    pattern = re.compile(
        '<dd>.*?board-index-\d*?">(.*?)</i>.*?<img data-src="(.*?)".*?'
        'data-val="{movieId:\d*?}">(.*?)</a></p>.*?<p class="star">(.*?)'
        '</p>.*?class="releasetime">(.*?)</p>.*?class="integer">(.*?)</i>'
        '<i class="fraction">(.*?)</i></p>.*?</dd>',
        re.S
    )
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'sort': item[0],
            'pic_url': item[1],
            'title': item[2],
            'actors': item[3].strip()[3:],
            'release_date': item[4].strip()[5:],
            'score': item[5] + item[6]
        }


def write_to_mongodb(content):
    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client.maoyan
    # db = client['test']
    collection = db.top100
    # collection = db['top100']
    result = collection.insert(content)
    print(result)


def write_to_file(content):
    with open('maoyan_to_100.txt', 'a') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()


def main(offset):
    url = 'https://maoyan.com/board/4?offset=' + str(offset)
    print(url)
    html = get_one_page(url)

    for item in parse_one_page(html):
        write_to_file(item)


if __name__ == '__main__':
    # pool = Pool()
    # pool.map(main, [i * 10 for i in range(10)])
    for i in range(10):
        main(i * 10)
