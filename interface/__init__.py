from . import web_base
from . import pages

browser = None
mainpage = None
loginpage = None
spacepage = None

def initialize(browser_type='Firefox'):
    global browser
    global mainpage
    global loginpage
    global spacepage
    browser = web_base.browserBase(browser=browser_type)
    browser.start()
    mainpage = pages.mainPage(browser._driver)
    loginpage = pages.loginPage(browser._driver)
    spacepage = pages.workspacePage(browser._driver)

def cleanup():
    global browser
    browser.close()

