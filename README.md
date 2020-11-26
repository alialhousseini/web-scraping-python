# web-scraping-python

### Script 1 and 2 are independent. Let’s start with script 1:
I used selenium, The selenium package is used to automate web browser interaction
from Python.
This script contains a function called indeed_job_search, this function try to open the chrome
driver and scrape all the needed information and save them into a file called job_search.txt. In
addition another file debug.txt will be created to show if there exists any trouble.
We have in this function 3 lists, and using for-loop we can open INDEED to show us GRAPHIC
DESIGN JOBS AND INTERNS in three different countries ( Saudi Arabia / Qatar And UAE ). Also,
the second list will help us to extract many jobs because some companies posting a title like “
Senior graphic designer “ or “ Design of graphics “.
The third list is used just for expanding the way of searching by entering the name of the
country in the search section instead of a city or a region.

### Script 2:
Script 2 is very simple, we will extract graphic design jobs and internships this time from a
famous website in the Arabic region which called “bayt.com”. This website contains thousands
of jobs offers, and because of simplicity we tried it only 3 times.
After finding the class name “has-pointer-d” using a function from the selenium package, we
will try to find now the information of each job by collecting title, head, and data using
find_element_by_tag_name method and by passing as parameter the appropriate attribute
from HTML code.
