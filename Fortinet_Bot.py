from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

username = 'username_given_by_ait'
password = 'login_password'

browser = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
browser.get('enter_url_here_which_opens_your_fortinet_login_page') 
#or you can even give any other link like https://www.codeforces.com/ which will redirect your request to fortinet login page.

emailInput = browser.find_element_by_id('ft_un')
passwordInput = browser.find_element_by_id('ft_pd')

emailInput.send_keys(username)
passwordInput.send_keys(password)
passwordInput.send_keys(Keys.ENTER)