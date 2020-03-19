import sys
from glob import glob
import os
import unicodedata

try:
    path = sys.argv[1]
except IndexError:
    path = '.'


def get_normalization_form(name):
    nfc_name = unicodedata.normalize('NFC', name)
    nfd_name = unicodedata.normalize('NFD', name)
    if nfc_name == nfd_name:
        return 'UTF-8'
    elif name == nfc_name:
        return 'UTF-8 NFC'
    elif name == nfd_name:
        return 'UTF-8 NFD'
    else:
        return 'Something wrong'

for relative_path in glob(os.path.join(path, '*')):
    name = os.path.basename(relative_path)
    normalization_form = get_normalization_form(name)
    print(name, normalization_form)
