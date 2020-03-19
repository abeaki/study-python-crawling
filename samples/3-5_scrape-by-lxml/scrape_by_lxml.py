import lxml.html

with open('book.html') as f:
    root = lxml.html.fromstring(f.read())
    #tree = lxml.html.parse(f)
    #root = tree.getroot()

print(root.tag)
print(root.xpath('//title')[0])
print(root.xpath('//title')[0].text)

for a in root.xpath('//h3//a'):
    print(a.get('href'), a.text_content())  # text_content() is lxml.html only
