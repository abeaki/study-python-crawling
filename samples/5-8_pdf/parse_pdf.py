import sys

from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTContainer
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage


def print_recursively(obj, level=0):
    """
    再帰的にオブジェクトを表示する関数。
    """

    print('    ' * level + repr(obj))
    # LTContainerを継承したクラスのオブジェクトは反復可能。
    if isinstance(obj, LTContainer):
        for child in obj:
            print_recursively(child, level + 1)

# Layout Analysisのパラメータを設定。
laparams = LAParams()
# 共有のリソースを管理するリソースマネージャーを作成。
resource_manager = PDFResourceManager()
# ページを集めるPageAggregatorオブジェクトを作成。
device = PDFPageAggregator(resource_manager, laparams=laparams)
# Interpreterオブジェクトを作成。
interpreter = PDFPageInterpreter(resource_manager, device)

# ファイルをバイナリ形式で開く。
with open(sys.argv[1], 'rb') as f:
    # PDFPageオブジェクトを順に取得する。
    # 時間がかかるのでpagenosで1〜3ページのみを指定している。
    for page in PDFPage.get_pages(f, pagenos=[0, 1, 2]):
        interpreter.process_page(page)  # ページを処理する。
        layout = device.get_result()  # LTPageオブジェクトを取得。
        print_recursively(layout)  # 表示する。
