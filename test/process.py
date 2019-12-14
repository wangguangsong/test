from bs4 import BeautifulSoup
def Process(html):
    soup=BeautifulSoup(html,'lxml')
    for i in soup(True):
        print(i.name)
