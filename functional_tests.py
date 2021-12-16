from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://localhost:8000')

assert 'install worked' in browser.title