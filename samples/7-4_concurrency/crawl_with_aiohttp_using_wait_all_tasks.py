import sys
import asyncio

import aiohttp
import feedparser
from bs4 import BeautifulSoup

# 最大同時ダウンロード数を3に制限するためのセマフォを作成
semaphore = asyncio.Semaphore(3)


def main():
    # ホットエントリーのRSSからURLのリストを取得する
    d = feedparser.parse('http://b.hatena.ne.jp/hotentry.rss')
    urls = [entry.link for entry in d.entries]

    def print_result(task):
        """Taskの結果を表示する"""
        print(task.result())

    # セッションオブジェクトを作成
    with aiohttp.ClientSession() as session:
        for url in urls:
            # Taskを作成してイベントループに登録する
            task = asyncio.ensure_future(fetch_and_scrape(session, url))
            # Taskの完了時に実行するコールバック関数を指定する
            task.add_done_callback(print_result)

        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait(asyncio.Task.all_tasks()))


async def fetch_and_scrape(session, url):
    """
    引数で指定したURLのページを取得して、URLとタイトルを含むdictを返す。
    """

    # セマフォでロックを獲得できるまで待つ
    #with await semaphore:
    async with semaphore:
        print('Start downloading', url, file=sys.stderr)

        # 非同期にリクエストを送り、レスポンスヘッダを取得する
        response = await session.get(url)
        # レスポンスボディを非同期に取得する
        soup = BeautifulSoup(await response.read(), 'lxml')

        return {
            'url': url,
            'title': soup.title.text.strip(),
        }

if __name__ == '__main__':
    main()
