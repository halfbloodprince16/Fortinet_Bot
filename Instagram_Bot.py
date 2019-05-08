from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

usernameStr = 'username'
passwordStr = 'password'

browser = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
browser.get('https://www.instagram.com/accounts/login/')

emailInput = browser.find_elements_by_css_selector('form input')[0]
passwordInput = browser.find_elements_by_css_selector('form input')[1]

emailInput.send_keys(usernameStr)
passwordInput.send_keys(passwordStr)
passwordInput.send_keys(Keys.ENTER)