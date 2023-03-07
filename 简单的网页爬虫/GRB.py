import random
import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl.workbook import Workbook
from openpyxl.writer.excel import ExcelWriter


chrome_options = webdriver.ChromeOptions()
url = 'http://101.43.194.154:54/'
chrome_options.add_argument('ignore-certificate-errors')
driver = webdriver.Chrome(options=chrome_options)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})


for i in range(0, 300):
    driver.get(url)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="name"]').send_keys('123456789QQ')
    driver.find_element_by_xpath('//*[@id="pwd"]').send_keys('123456')
    driver.find_element_by_xpath('//*[@id="form"]/div/div/div[4]/div/button').click()
    driver.find_element_by_xpath('//*[@id="mailnum"]').send_keys(999999999)
    driver.find_element_by_xpath('//*[@id="form"]/div/div/div[11]/div/button').click()
    time.sleep(1)
    alert=driver.switch_to.alert
    alert.accept()
    print(alert.text)
    time.sleep(2)




