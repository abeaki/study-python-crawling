import sys
import re
from collections import Counter

import MeCab
from nltk.text import Text, TextCollection


class SparseText:

    def __init__(self, tokens=None, name=None):
        self.counter = Counter()
        self.name = name
        if tokens:
            for token in tokens:
                self.append(token)

    def append(self, value):
        self.counter.update([value])

    def __len__(self):
        return sum(self.counter.values())

    def count(self, key):
        return self.counter.get(key)


mecab = MeCab.Tagger("-Ochasen")
docs = []

for path in sys.argv[1:]:
    print('Loading {}'.format(path), file=sys.stdout)
    with open(path) as f:
        content = f.read()
        #print(content[:1000])
        for match in re.finditer(r'<doc .*?>\n([^\n]*)\n(.*?)</doc>', content, re.DOTALL):
            title = match.group(1)
            text = match.group(2)

            tokens = SparseText(name=title)
            node = mecab.parseToNode(text)
            while node.next:
                #print(node.surface)
                tokens.append(node.surface)
                node = node.next

            #docs.append(Text(tokens, name=title))
            docs.append(tokens)

            if len(docs) >= 1000:
                break

    collection = TextCollection(docs)
    doc = docs[0]
    print(doc.name)
    tf_idfs = []
    for token in set(doc.tokens):
        tf_idf = collection.tf_idf(token, doc)
        tf_idfs.append((tf_idf, token))

    for tf_idf, token in sorted(tf_idfs, key=lambda x: x[0], reverse=True)[:10]:
        print(tf_idf, token)

    exit()
