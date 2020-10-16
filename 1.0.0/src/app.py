import asyncio
import time
from walkoff_app_sdk.app_base import AppBase

class Chat(AppBase):
    __version__ = "1.0.0"
    app_name = "chat"  # this needs to match "name" in api.yaml

    def __init__(self, redis, logger, console_logger=None):

        super().__init__(redis, logger, console_logger)

    async def send(self, myurl,username, password,content):
        try:
            from selenium import webdriver
            from selenium.webdriver.common.keys import Keys
        except:
            mystr = "no selenium"
            return mystr
        option = webdriver.ChromeOptions()
        # option.add_argument('--user-data-dir=/Users/apple/Library/Application Support/Google/Chrome/Default')
        option.add_argument('--headless')
        option.add_argument('--no-sandbox')
        option.add_argument('--disable-gpu')
        option.add_argument('--disable-dev-shm-usage')
        browser = webdriver.Chrome(chrome_options=option)
        # browser=webdriver.Chrome()
        browser.get(myurl)#"http://10.245.142.98:81"
        browser.set_window_size(1920, 1080)
        browser.maximize_window()

        browser.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div/input").clear()
        browser.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div/input").send_keys(username)
        browser.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[3]/div/input').clear()
        browser.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[3]/div/input').send_keys(password)
        browser.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[4]/div/input').clear()
        browser.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[4]/div/input').send_keys('10.245.142.98')
        browser.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[5]/button/span').click()
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul/li[4]/a/i').click()
        browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/ul/li/a').click()
        browser.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/textarea').send_keys(content)
        browser.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/button/span').click()
        time.sleep(5)
        browser.quit()
        return "chat"


if __name__ == "__main__":
    asyncio.run(Chat.run(), debug=True)
