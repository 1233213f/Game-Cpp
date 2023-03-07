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
url = 'http://101.43.194.154:52/index.min.html?account=123456789QQ&t=1667404800&sign=0800a8e618ee7f6be6aa1ac6ca1ae2ab'
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
    time.sleep(10)

    driver.find_element_by_xpath('//*[@id="btn-login"]').click()
    # driver.find_element_by_xpath('//*[@id="mailnum"]').send_keys(999999999)
    # driver.find_element_by_xpath('//*[@id="form"]/div/div/div[11]/div/button').click()
    # time.sleep(1)
    # alert=driver.switch_to.alert
    # alert.accept()
    # print(alert.text)
    time.sleep(2)




