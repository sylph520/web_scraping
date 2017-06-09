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
    time.sleep(5)
    nextpage_elem.click()

    return driver.current_url


def onepage_download(url):
    driver.get(url)
    # driver.add_cookie({'name': 'suid', 'value': 'A324491E11093B34'})
    # driver.add_cookie({'name': 'sunm', 'value': 'sylph003'})

    driver.add_cookie({'name': 'suid', 'value': '6D826822BB81E47A'})
    driver.add_cookie({'name': 'sunm', 'value': 'sylph002'})
    time.sleep(5)
    download_elems = driver.find_elements_by_xpath('//*[@id="PageContent"]/div/div[2]/span[4]/a[2]')
    for download_elem in download_elems:
        time.sleep(3)
        download_elem.click()
        time.sleep(5)
        handles = driver.window_handles
        driver.switch_to.window(handles[1])
        download_url_elem  = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[3]/td[4]/a')
        download_url_elem.click()
        driver.switch_to.window(handles[1])
        time.sleep(5)
        driver.close()
        driver.switch_to.window(handles[0])


driver = webdriver.Chrome()
dp0 = 'http://www2.soopat.com/Home/Result?SearchWord=%E6%B3%B5%E6%B5%A6%E5%90%88%E6%9D%9F%E5%99%A8&FMZL=Y&SYXX=Y&WGZL=Y&FMSQ=Y&PatentIndex=90&Sort=1'
for i in range(4):
    onepage_download(dp0)
    dp0 = turn2nextpage()
    time.sleep(2)
driver.quit()

