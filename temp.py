from itertools import zip_longest

urlList = ('https://www.kompas.com/food','https://tekno.kompas.com/','https://money.kompas.com/','https://edukasi.kompas.com/')
tipeList = ('food','tekno','money','edukasi')
def saveToFile(sentence, tipe):
    documents_clean = []
    for d in sentence:
        document_test = re.sub(r'[^\x00-\x7F]+', ' ', d)
        document_test = re.sub(r'@\w+', '', document_test)
        document_test = document_test.lower()
        document_test = re.sub(r'[\'\"\:\\\/,\(\)\{\}]', ' ', document_test)
        document_test = re.sub(r'[0-9]', '', document_test)
        document_test = re.sub(r'\s{2,}', ' ', document_test)
        documents_clean.append(document_test)

    f = open(tipe + '.txt', 'a')

    for p in documents_clean:
        p = p + "\n"
        f.write(p)

    f.close()


import requests  # for making HTTP requests in Python
from bs4 import BeautifulSoup  # pulling data from HTML or XML files
import re

for item1, item2 in zip_longest(urlList, tipeList, fillvalue=None):

    r = requests.get(item1)
    soup = BeautifulSoup(r.text, "html.parser")
    print(soup.prettify())
    link = []

    for i in soup.find('div', {'class': 'most__wrap'}).find_all('a'):
        i['href'] = i['href'] + '?page=all'
        link.append(i['href'])

    l = 1
    for j in link:
        r = requests.get(j)
        soup = BeautifulSoup(r.content, 'html.parser')
        sen = []

        for k in soup.find('div', {'class': 'read__content'}).find_all('p'):
            sen.append(k.text)

        saveToFile(sen, item2 + str(l))
        l = l + 1