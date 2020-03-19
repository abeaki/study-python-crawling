import xml.etree.ElementTree as ET

tree = ET.parse('rss1.xml')
root = tree.getroot()

#print(root.tag)

for item in root.findall('{http://purl.org/rss/1.0/}item'):
    title = item.find('{http://purl.org/rss/1.0/}title').text
    url = item.find('{http://purl.org/rss/1.0/}link').text
    print(url, title)
