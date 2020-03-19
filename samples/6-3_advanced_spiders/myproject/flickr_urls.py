import json
import os
import re
from glob import glob

DOWNLOADED_IMAGES = 'flickr_people.jl'
API_RESPONSE = 'flickr_people.json'
IMAGES_DIR = 'images/full.cc'

path_to_id = {}

with open(DOWNLOADED_IMAGES) as f:
    for line in f:
        item = json.loads(line)
        for file in item['files']:
            url = file['url']
            path = file['path']
            id = re.search(r'/(\d+)_', url).group(1)
            path_to_id[path] = id

id_to_url = {}

with open(API_RESPONSE) as f:
    response = json.load(f)
    for photo in response['photos']['photo']:
        owner = photo['owner']
        id = photo['id']
        url = 'https://www.flickr.com/photos/{0}/{1}'.format(owner, id)
        id_to_url[id] = url

for path in glob(os.path.join(IMAGES_DIR, '*')):
    basename = os.path.basename(path)
    image_path = 'full/' + basename
    id = path_to_id[image_path]
    url = id_to_url[id]
    print(basename, url)
