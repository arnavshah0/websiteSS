from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import nameorg
import time
from PIL import Image


class WebsiteSS:
    def __init__(self):
        a = nameorg.Organization()
        self.activedic = a.makedict()

    def go_to_website(self):
        self.driver = webdriver.Chrome('/Users/arnavshah/Desktop/py/websiteSS/chromedriver')
        brokenlinks = []
        for name, link in self.activedic.items():
            try:
                self.driver.get(link)
                time.sleep(3)
                # image = ImageGrab.grab(bbox=(0, 0, 907, 512))
                self.driver.get_screenshot_as_file(f'{name}.png')
                im = Image.open(f'{name}.png')
                im = im.resize((907, 512))
                im.save(f'{name}.png')
            except WebDriverException:
                link = link.replace('http://', '')
                try:
                    self.driver.get(link)
                    time.sleep(3)
                    self.driver.get_screenshot_as_file(f'{name}.png')
                except WebDriverException:
                    brokenlinks.append(name)
        print(brokenlinks)


w = WebsiteSS()
w.go_to_website()
