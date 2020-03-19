import xml.etree.ElementTree as ET

tree = ET.parse('rss2.xml')
root = tree.getroot()

#print(root.tag)

for item in root.findall('channel/item'):
    title = item.find('title').text
    url = item.find('link').text
    print(url, title)
