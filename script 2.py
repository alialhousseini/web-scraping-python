# install selenium and webdriver according to chrome
from selenium import webdriver
import time
# put url of web from where you want to scratch
url1 = 'https://www.bayt.com/en/qatar/jobs/graphic-designer-jobs/'
url2 = 'https://www.bayt.com/en/qatar/jobs/graphic-design-jobs/'
url3 = 'https://www.bayt.com/en/qatar/jobs/senior-graphic-design-jobs/'
# complete path to the webdriver in your computure(this path is on my computer)
driver = webdriver.Chrome('chromedriver.exe')
# driver.get("https://www.bayt.com/en/qatar/jobs/")
# this will get the data loaded
driver.get(url1)
# this will delay the below code to run 5sec late as page loaded
time.sleep(5)
# find the class
videos = driver.find_elements_by_class_name('has-pointer-d')
# loop throught it you may use xpath to selected
for item in videos:
    title = item.find_element_by_tag_name('h2').text
    head = item.find_element_by_tag_name('b').text
    data = item.find_element_by_tag_name('p').text
    print(title, head, data)
    print("")
    print("")
    print("")

driver.get(url2)
# this will delay the below code to run 5sec late as page loaded
time.sleep(5)
# find the class
videos = driver.find_elements_by_class_name('has-pointer-d')
# loop throught it you may use xpath to selected
for item in videos:
    title = item.find_element_by_tag_name('h2').text
    head = item.find_element_by_tag_name('b').text
    data = item.find_element_by_tag_name('p').text
    print(title, head, data)
    print("")
    print("")
    print("")

driver.get(url3)
# this will delay the below code to run 5sec late as page loaded
time.sleep(5)
# find the class
videos = driver.find_elements_by_class_name('has-pointer-d')
# loop throught it you may use xpath to selected
for item in videos:
    title = item.find_element_by_tag_name('h2').text
    head = item.find_element_by_tag_name('b').text
    data = item.find_element_by_tag_name('p').text
    print(title, head, data)
    print("")
    print("")
    print("")
