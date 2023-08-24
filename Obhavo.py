import requests
from bs4 import BeautifulSoup
from googletrans import Translator



def get_astronomy_news():
    # Google News sahifasidan maqolalarni olish
    url = 'https://news.google.com/search?q=astronomy&hl=en-US&gl=US&ceid=US%3Aen'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('article')

    # Maqolalarni to'plab, tarjima qilish
    translator = Translator()
    news = []
    for article in articles:
        title = article.find('h3').text
        source = article.find('a', {'aria-label': 'More from this source'}).text
        link = article.find('a', {'class': 'VDXfz'}).get('href')
        translated_title = translator.translate(title, dest='uz').text

        entry = {
            'title': translated_title,
            'source': source,
            'link': f'https://news.google.com{link}'
        }
        news.append(entry)

    return news

news = get_astronomy_news()
for article in news:
    print('Sarlavha:', article['title'])
    print('Manba:', article['source'])
    print('Havola:', article['link'])
    print('---')