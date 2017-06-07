# -*- coding: utf-8 -*-
"""
Created on Tue May 30 22:54:04 2017

@author: Admin
"""

## selenium, first get to the page of search results
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import urllib
from bs4 import BeautifulSoup
import time
from datetime import datetime


def get_pat_data(link):
    time.sleep(3)
    try:
        response = urllib.request.urlopen(link)
    except:
        try:
            time.sleep(2)
            try:
                response = urllib.request.urlopen(link)
                html = response.read().decode('utf-8')
                #    print (html)
                bsObj = BeautifulSoup(html, 'lxml')
                pat_title = bsObj.h1.contents[0].strip()
                # pat_apply_date
                apply_info_string = bsObj.strong.i.string
                apply_id = apply_info_string[4:18]
                apply_date = apply_info_string[23:]
                abstract_text = bsObj.find('td', {'class': 'sum f14'}).contents[2].strip()
                apply_person = bsObj.find('b', {}, text="申请人：").parent.a.get_text()
                address = bsObj.find('b', {}, text="地址：").next_sibling.strip()
                invent_persons_list = []
                for person in bsObj.find('b', {}, text="发明(设计)人：").parent.findAll('a'):
                    invent_persons_list.append(person.get_text())
                invent_persons = ','.join(invent_persons_list)
                main_ipc = bsObj.find('b', {}, text="主分类号：").parent.a.get_text()
                ipcs_list = []
                for ipc in bsObj.find('b', {}, text="分类号：").parent.findAll('a'):
                    ipcs_list.append(ipc.get_text())
                ipcs = ','.join(ipcs_list)
                # print (ipcs)
                open_id = bsObj.find('td', {}, text='公开号').next_sibling.next_sibling.get_text().strip()
                open_date = bsObj.find('td', {}, text='公开日').next_sibling.next_sibling.get_text().strip()
                pat_agent = bsObj.find('td', {}, text='专利代理机构').next_sibling.next_sibling.get_text().strip()
                pat_agent_person = bsObj.find('td', {}, text='代理人').next_sibling.next_sibling.get_text().strip()
                write_items = [pat_title, apply_id, apply_date, abstract_text, apply_person, address, invent_persons,
                               main_ipc,
                               ipcs,
                               open_id, open_date, pat_agent, pat_agent_person, '\n']
                #    print(write_items)
                sep = '\t'
                itemstr = sep.join(write_items).replace('\xa0', ' ')
                return itemstr, datetime.strptime(apply_date, '%Y-%m-%d')
            except:
                print('urlopen time out')
                return
        except:
            write_list = [1]
            write_list.append(driver.current_url)
            write_list.append()




def write_pats_data(filename, itemstrs):
    with open(filename, 'w') as f:
        for itemstr in itemstrs:
            f.write(itemstr)


# fill in the search word
def search_and_sort(kw):
    elem = driver.find_element_by_id('SearchWord')
    elem.send_keys(kw)
    # simulate the click of sort by date descending
    elem.send_keys(Keys.RETURN)
    apply_date_elem = driver.find_element_by_xpath('/html/body/div[6]/div/div/ul[2]/li[2]/a')
    apply_date_elem.click()


def next_page():
    print('start')
    next_page_elem = driver.find_element_by_xpath('/html/body/div[9]/a[9]')
    next_page_elem.click()
    print('************turn to next page')


def get_onepage_pats(ret_data, next_idx = 0):
    #    pat_blocks = []
    pat_links_block0 = (driver.find_elements_by_xpath('//div[2]/h2/a'))
    pat_links_block = pat_links_block0[next_idx:]
    handle = driver.current_window_handle
    for pat_link_block in pat_links_block:
        pat_link = pat_link_block.get_attribute('href')
        time.sleep(3)
        try:
            pat_link_block.click()
        except:
            time.sleep(2)
            pat_link_block.click()
        handles = driver.window_handles
        print ("2 tabs\t %s" % handles)
        #        print(handles)
        driver.switch_to.window(handles[1])
        #        print(driver.current_window_handle)
        print('now at the info page %s' % driver.current_url)
        current_items, current_ad = get_pat_data(pat_link)
        # handle pat pdf download
        download_page_elem = driver.find_element_by_xpath('/html/body/div[7]/div[1]/div/div[1]/table/tbody/tr[7]/td/div/a[2]')
        time.sleep(2)
        download_page_elem.click()
        handles = driver.window_handles
        print ('3 tabs\t %s', handles)
        print('current handle %s' %driver.current_window_handle)
        driver.switch_to.window(handles[2])
        download_url = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[3]/td[4]/a')
        time.sleep(3)
        try:
            download_url.click()
        except:
            write_list = [1]
            write_list.append(driver.current_url)
            write_list.append()
        print("current handle %s" %driver.current_window_handle)
        driver.close()
        driver.switch_to.window(handles[1])
        print("current handle %s" % driver.current_window_handle)
        driver.close()
        driver.switch_to.window(handle)
        if (current_ad.year < 2015):
            print('%s is exceeding' % current_ad)
            write_list = ['2']
            return False
        else:
            next_idx += 1
            print(current_items)
            ret_data.append(current_items)
    return True


def get_pats_data(next_idx = 0):
    ret_data = []
    while (True):
        # first get one page of patents
        time.sleep(3)
        sig = get_onepage_pats(ret_data)
        for i in ret_data:
            f.write(i)
        # if not exceed time boundary, then turn to next page
        if (sig):
            time.sleep(3)
            next_page()
        else:
            break
    return ret_data


def unit_test():
    #        driver.get("http://www2.soopat.com/Home/IIndex")
    #        time.sleep(3)
    #        search_and_sort("泵浦合束器")
    # driver.get(
    #     "http://www2.soopat.com/Home/Result?Sort=1&View=&Columns=&Valid=&Embed=&Db=&Ids=&FolderIds=&FolderId=&ImportPatentIndex=&Filter=&SearchWord=%E6%B3%B5%E6%B5%A6%E5%90%88%E6%9D%9F%E5%99%A8&FMZL=Y&SYXX=Y&WGZL=Y&FMSQ=Y")
    statusStr = f0.read()
    status_list = statusStr.split()
    statusCode = status_list[0]
    next_idx = 0
    if statusCode == '0':
        driver.get(status_list[1])

    elif statusCode == '2':
        print ('done handling')
        return
    elif statusCode == '1':
        print ('continue downloading')
        driver.get(status_list[1])
        next_idx = status_list[2]
    else:
        print('error status code')

    driver.add_cookie({'name': 'suid', 'value': '6D826822BB81E47A'})
    driver.add_cookie({'name': 'sunm', 'value': 'sylph002'})
    # filename = 'pats_single_page.txt'
    pats_data = get_pats_data(next_idx)
    # write_pats_data(filename, pats_data)
    # driver.quit()


#    link =  'http://www2.soopat.com/Patent/201611146689'
#    filestr = open('pats_test.txt','w')
#    get_pat_data(link,filestr)

driver = webdriver.Chrome()
# driver = webdriver.PhantomJS()
f0 = open('status.txt', 'r+')
# seperate by tab, the first item stands for status code 0 is the start status, 1 is downloading , 2 is done downloading
# the second item is a url directed to the last search results page url
# the third is the idx of the next to be handled search result
f = open("pat_test.txt", 'a')
unit_test()
f.close()
