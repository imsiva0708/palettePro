from bs4 import BeautifulSoup
with open('index.html','r') as f:
    doc = BeautifulSoup(f,'html.parser')

tag = doc.find('p', class_ = 'para')
tag.string = 'gpesa'
print(tag)
print(doc)

