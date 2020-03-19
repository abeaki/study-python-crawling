import sys
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36'

# PhantomJsオブジェクトのインスタンスを作成する
driver = webdriver.PhantomJS()
#driver = webdriver.PhantomJS(desired_capabilities={
#    'phantomjs.page.settings.userAgent': USER_AGENT,
#})

#driver.set_window_size(800, 600)
#print(driver.get_window_size())
#exit()

# Googleのトップ画面を開く
driver.get('https://note.mu/recommend')

# タイトルに'Google'が含まれていることを確認する
assert 'note' in driver.title

#import feedgenerator
#feed = feedgenerator.Rss201rev2Feed(
#    title='おすすめノート', link='https://note.mu/recommend', description='おすすめノート')
#
#for a in driver.find_elements_by_css_selector('a.p-post--basic'):
#    url = a.get_attribute('href')
#    title = a.find_element_by_css_selector('h4').text
#    description = a.find_element_by_css_selector('.c-post__description').text.strip()
#
#    feed.add_item(title=title, link=url, description=description, unique_id=url)
#
#with open('recommend.rss', 'w') as f:
#    feed.write(f, encoding='utf-8')
#
#exit()

class body_to_be_extended:
    def __init__(self, driver):
        self.initial_scroll_height = self.get_scroll_height(driver)

    def __call__(self, driver):
        scroll_height = self.get_scroll_height(driver)
        return scroll_height > self.initial_scroll_height

    def get_scroll_height(self, driver):
        return driver.execute_script('return document.body.scrollHeight')


class num_elements_to_be_increased:

    def __init__(self, driver, locator):
        self.locator = locator
        self.initial_num_elements = len(driver.find_elements(*self.locator))

    def __call__(self, driver):
        num_elements = len(driver.find_elements(*self.locator))
        return num_elements > self.initial_num_elements


wait = WebDriverWait(driver, 10)


driver.execute_script('scroll(0, document.body.scrollHeight)')
print('Scrolled', file=sys.stderr)
#wait.until(body_to_be_extended(driver))
wait.until(num_elements_to_be_increased(driver, (By.CSS_SELECTOR, '.c-post')))

#time.sleep(3)

driver.execute_script('scroll(0, document.body.scrollHeight)')
print('Scrolled', file=sys.stderr)


button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-more')))

button.click()
print('Clicked', file=sys.stderr)
#wait.until(body_to_be_extended(driver))
wait.until(num_elements_to_be_increased(driver, (By.CSS_SELECTOR, '.c-post')))
#time.sleep(3)

driver.execute_script('scroll(0, document.body.scrollHeight)')
print('Scrolled', file=sys.stderr)
#wait.until(body_to_be_extended(driver))
wait.until(num_elements_to_be_increased(driver, (By.CSS_SELECTOR, '.c-post')))
#time.sleep(3)

driver.execute_script('scroll(0, document.body.scrollHeight)')
print('Scrolled', file=sys.stderr)

button = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.btn'), 'もっとみる'))
#time.sleep(3)

# スクリーンショットを撮る
driver.save_screenshot('note_recommend.png')

# 検索結果を表示する
for a in driver.find_elements_by_css_selector('a.p-post--basic'):
    url = a.get_attribute('href')
    print(url)
    title = a.find_element_by_css_selector('h4').text
    description = a.find_element_by_css_selector('.c-post__description').text.strip()

    print(title)
    print(description)
    print()

