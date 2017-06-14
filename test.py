import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import urllib
from bs4 import BeautifulSoup
import time
import random
def turn2nextpage():
    nextpage_elem = driver.find_element_by_class_name('next')
    time.sleep(2)
    nextpage_elem.click()

    return driver.current_url


def onepage_download(url):
    driver.get(url)
    # driver.add_cookie({'name': 'suid', 'value': 'A324491E11093B34'})
    # driver.add_cookie({'name': 'sunm', 'value': 'sylph003'})

    # driver.add_cookie({'name': 'suid', 'value': '6D826822BB81E47A'})
    # driver.add_cookie({'name': 'sunm', 'value': 'sylph002'})

    driver.add_cookie({'name': 'suid', 'value': '50E5C918F3244F01'})
    driver.add_cookie({'name': 'sunm', 'value': 'sylph000'})
    time.sleep(2)
    download_elems = driver.find_elements_by_xpath('//*[@id="PageContent"]/div/div[2]/span[4]/a[2]')
    for download_elem in download_elems:
        time.sleep(2)
        download_elem.click()
        time.sleep(2)
        handles = driver.window_handles
        driver.switch_to.window(handles[1])
        download_url_elem  = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[3]/td[4]/a')
        download_url_elem.click()
        driver.switch_to.window(handles[1])
        time.sleep(2)
        driver.close()
        driver.switch_to.window(handles[0])


driver = webdriver.Chrome()
# driver = webdriver.PhantomJS()
dp0 = 'http://www2.soopat.com/Home/Result?SearchWord=%E5%85%89%E7%BA%A4%E5%87%86%E7%9B%B4%E5%99%A8&FMZL=Y&SYXX=Y&WGZL=Y&FMSQ=Y&PatentIndex=40&Sort=1'
for i in range(2):
    onepage_download(dp0)
    dp0 = turn2nextpage()
    time.sleep(2)
driver.quit()

