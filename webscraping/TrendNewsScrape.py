from bs4 import BeautifulSoup
import requests
import pandas as pd



url = 'https://www.ndtv.com/top-stories'

data = requests.get(url)
print(data.status_code)
htmlcontent = data.content

soup = BeautifulSoup(htmlcontent, 'html.parser')

titles = []
descs = []

for d in soup.find_all('div', attrs={'class':'news_Itm-cont'}):
    title = d.find('a')
    # print(title.string)
    desc = d.find('p')
    # print(desc.string)

    titles.append(title.string)
    descs.append(desc.string)

print('success')

df = pd.DataFrame({'News Heading':titles, 'Description': descs, 'Source': 'Ndtv'}) 
df.to_html('News.html', index=True, encoding='utf-8')

# df = pd.DataFrame({'NewsHeading':[titles], 'Description': [descs], 'Source': 'Ndtv'}) 
# df.to_json('News.json')



    # desc = d.find('p', attrs={'class': 'newsCont'})