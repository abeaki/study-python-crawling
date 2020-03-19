from selenium import webdriver
import feedgenerator


def main():
    """
    メインの処理。
    """

    driver = webdriver.PhantomJS()  # PhantomJSのWebDriverオブジェクトを作成する。
    driver.set_window_size(800, 600)  # ウィンドウサイズを設定する。

    navigate(driver)
    posts = scrape_posts(driver)
    save_as_feed('recommend.rss', posts)


def navigate(driver):
    """
    目的のページに遷移する。
    """

    driver.get('https://note.mu/')  # noteのトップページを開く。
    assert 'note' in driver.title  # タイトルに'note'が含まれていることを確認する。


def scrape_posts(driver):
    """
    文章コンテンツのURL、タイトル、概要を含むdictのリストを取得する。
    """

    posts = []

    # すべての文章コンテンツを表す<a>要素について反復する。
    for a in driver.find_elements_by_css_selector('a.p-post--basic'):
        # URL、タイトル、概要を取得して、dictとしてリストに追加する。
        posts.append({
            'url': a.get_attribute('href'),
            'title': a.find_element_by_css_selector('h4').text,
            'description': a.find_element_by_css_selector('.c-post__description').text,
        })

    return posts


def save_as_feed(path, posts):
    """
    文章コンテンツのリストをフィードとして保存する。
    """

    # フィードを表すRss201rev2Feedオブジェクトを作成する。
    feed = feedgenerator.Rss201rev2Feed(
        title='おすすめノート',  # フィードのタイトル
        link='https://note.mu/',  # フィードに対応するWebサイトのURL
        description='おすすめノート')  # フィードの概要

    for post in posts:
        # フィードにアイテムを追加する。
        # キーワード引数unique_idは、アイテムを一意に識別するユニークなIDを指定する。
        # 必須ではないが、このIDを指定しておくとRSSリーダーがアイテムの重複なく扱える
        # 可能性が高まるので、ここではコンテンツのURLを指定している。
        feed.add_item(title=post['title'], link=post['url'],
                      description=post['description'], unique_id=post['url'])

    with open(path, 'w') as f:
        feed.write(f, 'utf-8')  # ファイルに保存する。第2引数にエンコーディングを指定する。

if __name__ == '__main__':
    main()
