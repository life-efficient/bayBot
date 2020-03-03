import sys, os
sys.path.append(os.path.expanduser('~/projects/bots'))

from time import sleep

from bots import Bot

class BayBot(Bot):
    def __init__(self):
        super().__init__()
        self.driver.get('https://www.ebay.com')
        # self.driver.get('https://signin.ebay.com')
        if 'signin' in self.driver.current_url:
            self.login()

    def login(self):
        username = self.driver.find_element_by_xpath('//[@id="userid"]')
        username.send_keys('harryaberg@gmail.com')
        password = self.driver.fing_element_by_xpath('//input[@id="pass"]')
        password.send_keys('Inc0rrect!')
        login_btn = self.driver.find_element_by_xpath('//button[@id="sngBt"]')
        login_btn.click()

    def search(self, query):
        self._search(query, _type='text', placeholder='Search for anything')
        self.click_btn('Search')
        sleep(1)
        # items = self.driver.find_element_by_xpath('//div[@class="srp-river-results"]')
        # items = items.find_elements_by_xpath('//li[@class="s-item"]')
        items = []
        for idx in range(10):
            items.append(self.driver.find_element_by_xpath(f'//li[@id="srp-river-results-listing{idx+1}"]'))
        for item in items:
            print(item.text)
        # item_urls = [item.find_element_by_xpath('//a').get_attribute('href') for item in items]
        item_urls = [item.find_element_by_xpath('//a').get_attribute('outerHTML') for item in items]
        for u in item_urls:
            print(u)
        print(f'{len(item_urls)} were found for the query: {query}')

        for url in item_urls:
            self.driver.get(url)
            skjdl
        # for item in items:
        #     item.click()

    

bayBot = BayBot()
bayBot.search('Raf Simons')