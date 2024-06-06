from bs4 import BeautifulSoup
from urllib.parse import quote_plus
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

engines = [
        {
            'name': 'google',
            'baseurl': 'https://google.com/search?q={q}',
            'results': '.MjjYud',
            'title_tag': '.LC20lb.MBeuO.DKV0Md'
        },
        {
            'name': 'bing',
            'baseurl': 'https://www.bing.com/search?q={q}',
            'results': '#b_results > li',
            'title_tag': 'h2'
        },
        {
            'name': 'yahoo',
            'baseurl': 'https://search.yahoo.com/search?p={q}',
            'results': '.compTitle',
            'title_tag': 'h3 > a'
        },
        {
            'name': 'yandex',
            'baseurl': 'https://yandex.com/search/?text={q}',
            'results': 'ul > li',
            'title_tag': '.organic__title-wrapper > a'
        },
    ]

def search(engine, query):
    driver = webdriver.Chrome()
    url = engine['baseurl'].replace("{q}", quote_plus(query))
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    result = []

    r = soup.select(engine['results'])

    for i in r:
        title_tag = i.select_one(engine['title_tag'])
        if title_tag == None:
            continue

        if i.a != None:
            result.append({'title': title_tag.text, 'link': i.a.attrs['href'], 'engine': engine['name']})
            continue

        if title_tag.a != None:
            result.append({'title': title_tag.text, 'link': title_tag.a.attrs['href'], 'engine': engine['name']})
            continue

        result.append({'title': title_tag.text, 'link': title_tag.attrs['href'], 'engine': engine['name']})
    driver.close()
    
    return result

def super_search(query, engines):
    result = []

    # start searching
    for engine in engines:
        result += search(engine, query)
    
    # filter out same reuslts
    urls = []
    for r in result:
        # /?q=sans+site:www.sans.edu
        if r['link'] in urls:
            result.remove(r)
        else:
            urls.append(r['link'])
    
    return result
