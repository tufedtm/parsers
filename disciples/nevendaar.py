# nevendaar.com
from urllib import request
from bs4 import BeautifulSoup
import os


url = 'http://nevendaar.com/sitemap.xml'
html = request.urlopen(url).read()

soup = BeautifulSoup(html, 'html.parser')

VALID = '/load/8-1'
alllinks = []

for el in soup.findAll('url'):
    if VALID in el.loc.string:
        alllinks.append(el.loc.string)

for el in alllinks:
    print(el)
    html = request.urlopen(el).read()
    html = BeautifulSoup(html, 'html.parser')
    title = html.find('h2').string.strip().replace(':', ' -').replace('"', '').replace('?', '')
    print(title)
    try:
        os.mkdir(title)
        os.chdir(title)
    except:
        pass
    try:
        mod = html.find('div', class_="body").p.a['href']
        mod = request.urlopen(mod).geturl()
        request.urlretrieve(mod, str(mod.split('/')[-1:]).strip('[]\'\''))
        txt = open(title + '.txt', 'w', encoding='utf-8')
        txt.write(el + '\n' + title + '\n\n\n')
        txt.close()
        txt = open(title + '.txt', 'a', encoding='utf-8')
        txt.write(html.find('div', class_="body").get_text())
        txt.close()
        os.chdir('..')
    except:
        pass