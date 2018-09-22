import requests
from pyquery import PyQuery as pq


def main():
    url = 'https://zhihu.com/explore'
    openurl(url)


def openurl(url):
    data = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0',
    }
    page = requests.get(url,headers=data)
    print(page.text)
    doc = pq(page.text)
    items = doc('.explore-tab .feed-item').items()
    for item in items:
        qusetion = item.find('h2').text()
        author = item.find('.author-link-line').text()
        answer = pq(item.find('.content').html()).text()
        with open('explore.txt','a',encoding='utf-8') as f:
            f.write('\n'.join([qusetion,author,answer]))
            f.write('\n' + '=' * 50 + '\n')

if __name__ == '__main__':
    main()