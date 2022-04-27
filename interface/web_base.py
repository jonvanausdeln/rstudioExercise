# Contains the base objects used to interact with the application under test
# Uses selenium webdriver as base framwork
############################################################################
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser_list = frozenset(['Edge','Chrome', 'Firefox'])

class browserBase():
    # Browser class, object representing the browser instance under test
    def __init__(self, browser='Edge'):
        self.browser = browser
        if self.browser not in browser_list:
            raise Exception("Can't use broswer %s" % str(browser))
        self._driver = None

    def close (self):
        if self._driver:
            self._driver.quit()

    def start(self):
        if self.browser == 'Edge':
            self._driver = webdriver.Edge()
        if self.browser == 'Chrome':
            self._driver = webdriver.Chrome()
        if self.browser == 'Firefox':
            self._driver = webdriver.Firefox()

    def load_url(self, url):
        self._driver.get(url)

class objectBaseClass():
    def __init__(self,driver, selector, selector_type='xpath', name="object"):
        if not driver:
            raise Exception("No Selenium driver initialized")
        self._driver = driver        
        self.selector = selector
        self.selector_type = selector_type
        self.name = name

    def _get_handle(self, timeout=10):
        # Returns handle to the page objecct if available
        
        if self.selector_type == 'css':
            handle = WebDriverWait(self._driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.selector)))
        elif self.selector_type == 'xpath':
            handle = WebDriverWait(self._driver, timeout).until(EC.presence_of_element_located((By.XPATH, self.selector)))
        else:
            handle = None
        
        return handle


    def check_existance(self, timeout=10):
        try:
            print('-- Checking for existance of %s' % self.name)
            handle_object = self._get_handle(timeout=timeout)
            return True
        except:
            return False

class webPageBaseClass():
    def __init__(self, driver, url):
        if not driver:
            raise Exception("No Selenium driver initialized")
        self._driver = driver
        self.base_url = url
    
    def load(self):
        self._driver.get(self.base_url)

    def check_existance(self):
        if self._driver.current_url == self.base_url:
            return True
        else:
            return False