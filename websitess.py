from selenium import webdriver
import nameorg
import time


class WebsiteSS:
    def __init__(self):
        a = nameorg.Organization()
        self.activedic = a.makedict()

    def go_to_website(self): 
        self.driver = webdriver.Chrome('/Users/arnavshah/Desktop/py/websiteSS/chromedriver')
        for name, link in self.activedic.items():
            self.driver.get(link)
            time.sleep(3)
            self.driver.get_screenshot_as_file(f'{name}.png')






w = WebsiteSS()
w.go_to_website()
