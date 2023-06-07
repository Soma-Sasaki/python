import requests, sys, webbrowser, bs4, os, chromedriver_binary, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
os.chdir(r"C:\Users\shira\デスクトップ\programming\python\boring")

browser = webdriver.Chrome()
browser.get("https://play2048.co/")
html_elem = browser.find_element(By.TAG_NAME, "html")

score_before = 0
score = "body > div.container > div.heading > div > div.score-container"
iter = 0
while iter < 100:
    html_elem.send_keys(Keys.UP)
    html_elem.send_keys(Keys.RIGHT)
    html_elem.send_keys(Keys.DOWN)
    html_elem.send_keys(Keys.LEFT)
    time.sleep(1)
    iter += 1

    score_elem = browser.find_element(By.CSS_SELECTOR, "body > div.container > div.heading > div > div.score-container")
    score_after = score_elem.text
    print(score_after)

    if score_before == score_after:
        break

    score_before = score_after

print("遊びは終わり!")
