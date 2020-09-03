from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options = chrome_options)
driver.get("https://www.toyota.co.uk/order-a-brochure")
driver.implicitly_wait(30)
time.sleep(2)
try:
    driver.find_element_by_id("tgbgdpr-overlay-agree").click()
except:
    pass
time.sleep(2)
driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@crossdomain="true"]'))
driver.find_element_by_xpath("//div[text()='Download']").click()