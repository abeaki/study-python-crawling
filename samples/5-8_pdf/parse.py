from __future__ import unicode_literals

import sys
import io

from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams

laparams = LAParams()

# Open a PDF file.
fp = open(sys.argv[1], 'rb')

out = io.BytesIO()
extract_text_to_fp(fp, out, laparams=laparams, page_numbers=[6], output_type='xml')

print(out.getvalue().decode('utf-8'))

import xml.etree.ElementTree as ET
root = ET.fromstring(out.getvalue() + b'</pages>')
lines = []
for textline in root.iter('textline'):
    lines.append(''.join(text.text for text in textline.findall('text')).strip())

for line in lines:
    print(line)
