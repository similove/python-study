import requests
import re
from multiprocessing import Pool
from selenium import webdriver
from urllib.request import urlretrieve

def get_one_page(url):
  try:
    response = requests.get(url)
    response.encoding = 'gb2312'
    if response.status_code == 200:
      return response.text
    return None
  except Exception:
    return None


def write_to_file(content):
  with open('result3.txt', 'a') as f:
    f.write(content)
    f.close()


def parse_one_page(html):
  pattern = re.compile('<article.*?<a href="(.*?)".*?</article>', re.S)
  items = re.findall(pattern, html)
  for item in items:
    print(item)
    # write_to_file(item + '\n')
    second = get_one_page(item)
    parse_second_page(second, item)
    # print(second + '\n\n\n\n\n\n\n\n\n\n\n\n\n')


def parse_second_page(html, base_url):
  # print(html)
  pattern = re.compile(
      '<article.*?class="mm-title">(.*?)</h2>.*?src="(.*?)/1.jpg" /></a></div>.*?<span class="rw">1/(.*?)页.*?</article>',
      re.S)
  items = re.findall(pattern, html)
  get_one_page(base_url)
  index = base_url.rfind('.html')
  base = base_url[0:index]

  options = webdriver.ChromeOptions()
  options.add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19",--headless')
  dirver = webdriver.Chrome(options)
  for item in items:
    for index in range(int(item[2])):
      url = base + '_' + str(index + 2) + '.html'
      dirver.get(url)
      print(url)
      urlretrieve(item[0] + ': ' + item[1] + '/' + str(index + 1) + '.jpg', "test.jpg")
      write_to_file(item[0] + ': ' + item[1] + '/' + str(index + 1) + '.jpg\n')


def main(page):
  url = 'http://m.mm131.com/more.php?page=' + str(page)
  html = get_one_page(url)
  parse_one_page(html)


if __name__ == '__main__':
  pool = Pool()
  pool.map(main, [i + 1 for i in range(1)])
