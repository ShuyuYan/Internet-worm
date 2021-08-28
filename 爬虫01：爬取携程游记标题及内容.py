from bs4 import BeautifulSoup
import bs4
import requests

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return""
        
data = open("data.txt", "w", encoding="gb18030")
tot = 0
for i in range(1,4):
    print(i)
    url = 'https://you.ctrip.com/searchsite/travels/?query=%e9%9d%9e%e9%81%97&isAnswered=&isRecommended=&publishDate=&PageNo='+str(i)
    html = getHTMLText(url)
    soup = BeautifulSoup(html,"html.parser")
    for items in soup.select('dt'):
        if items.a != None:
            print(items.a.text, file=data)
            nxt = 'https://you.ctrip.com' + items.a['href']
            html2 = getHTMLText(nxt)
            soup2 = BeautifulSoup(html2,"html.parser")
            for k in soup2.find_all('div',class_='ctd_main_body'):
                print(k.text, file=data)
                tot = tot + 1
print(tot)