# nevendaar.com
from urllib import request
from bs4 import BeautifulSoup
import os


url = 'http://disciples.clan.su/sitemap.xml'
html = request.urlopen(url).read()

soup = BeautifulSoup(html, 'html.parser')

VALID = '/load/'
alllinks = []

for el in soup.findAll('url'):
    if VALID in el.loc.string:
        alllinks.append(el.loc.string)

i = 0
for el in alllinks:
    i += 1
    print(el)
    html = request.urlopen(el).read()
    html = BeautifulSoup(html, 'html.parser')
    title = html.find('div', class_="eTitle").string.strip().replace(':', ' -').replace('"', '').replace('?', '')
    print(title)
    try:
        os.mkdir(title)
        os.chdir(title)
    except OSError:
        os.mkdir(title + str(i))
        os.chdir(title + str(i))
    try:
        mod = html.find('table', class_="eBlock").a['href']
        print(mod)
        mod = request.urlopen(mod).geturl()
        request.urlretrieve(mod, str(mod.split('/')[-1:]).strip('[]\'\''))
        txt = open(title + '.txt', 'w', encoding='utf-8')
        txt.write(el + '\n' + title + '\n\n\n')
        txt.close()
        txt = open(title + '.txt', 'a', encoding='utf-8')
        txt.write(html.find('td', class_="eText").get_text())
        txt.close()
        os.chdir('..')
    except:
        os.chdir('..')
