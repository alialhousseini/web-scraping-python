from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pathlib import Path

import sys

def indeed_job_search(*args):
    
    browser = None

    PATH_TO_GECKO_DRIVER = './geckodriver'
    PATH_TO_CHROME_DRIVER = './chromedriver.exe'



    list1=['https://www.indeed.ae/','https://qa.indeed.com/','https://sa.indeed.com/']
    list2=['Graphic Design','Senior graphic design','remote graphic design','graphic designer','graphic design intern']
    list3=['United arab emirates','qatar','saudi arabia']
    for l1 in list1:
    	for l2 in list2:
		    if Path(PATH_TO_GECKO_DRIVER).is_file():
		        options = webdriver.FirefoxOptions()
		        if 'headless' in args:
		            options.headless = True
		        browser = webdriver.Firefox(executable_path=PATH_TO_GECKO_DRIVER, options=options)
		    elif Path(PATH_TO_CHROME_DRIVER).is_file():
		        options = webdriver.ChromeOptions()
		        if 'headless' in args:
		            options.headless = True
		        browser = webdriver.Chrome(executable_path=PATH_TO_CHROME_DRIVER, options=options)
		    else:
		        print("Unable to find a webdriver.")
		        return
		    browser.get(l1)

		    browser.implicitly_wait(5) 

		    search_bar = browser.find_element_by_name('q')
		    search_bar.send_keys(l2)
		    search_bar = browser.find_element_by_name('l')
		    if l1==list1[0]:
		    	search_bar.send_keys(list3[0])
		    if l1==list1[1]:
		    	search_bar.send_keys(list3[1])
		    if l1==list1[2]:
		    	search_bar.send_keys(list3[2])
		    search_bar.send_keys(Keys.ENTER)

		    browser.implicitly_wait(5) 

		    search_results = browser.find_elements_by_xpath('//h2/a')

		    file = open("job_search.txt", 'a')
		    file.write("\n")

		    for job_element in search_results:

		        job_title = job_element.text
		        job_link = job_element.get_attribute('href')

		        file.write("%s | link: %s \n" %(job_title, job_link))
		    browser.close()
    

if __name__ == "__main__":
    indeed_job_search(*sys.argv)