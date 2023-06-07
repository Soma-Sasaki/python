import os
os.chdir(r"C:\Users\shira\デスクトップ\programming\python\scraping")
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary

#画面に表示しないヘッドレスモード
#options = Options()
#options.add_argument("--headless")

browser = webdriver.Chrome()
browser.get("https://www.aozora.gr.jp/cards/000081/files/46268_23911.html")
browser.save_screenshot("website.png")
browser.quit()
