from bs4 import BeautifulSoup
import requests

url = 'https://www.flipkart.com/search?q=laptops&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=laptops&requestId=4727e649-733f-4ef7-9e7e-79d87e6d1483'

response = requests.get(url)

print(response.status_code)

htmlcontent = response.content


soup = BeautifulSoup(htmlcontent, 'html.parser')
# print(soup.prettify())

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.p)
# print(soup.find('a'))

# print(soup.find(id='productRating_LSTCOMG9VHHG6Q3RRJXQHPK6Q_COMG9VHHG6Q3RRJX_'))

# for link in soup.find_all('a'):
#     print(link.get('href'))

# for img in soup.find_all('img'):
#     print(img.get('src'))
