import requests
from bs4 import BeautifulSoup
import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

filename = "oncology-doximity.csv"

# url = "https://www.doximity.com/directory/md/alphabetical/a"
# url = "https://www.doximity.com/directory/md/specialty/oncology"
url = "https://www.doximity.com/directory/md/specialty/oncology"

options = Options()
options.headless = True
driver = webdriver.Chrome(
        options=options
	)
def soup(url):

	driver.get(url)
	time.sleep(2)
	main_div = driver.find_element_by_css_selector('body')
	
	# response = requests.get(url)
	# soup = BeautifulSoup(response.content, "html.parser")
	soup = BeautifulSoup(main_div.get_attribute('outerHTML'), "html.parser")
	getProfileURL(soup)
	driver.close()	

def getProfileURL(soup):
	# print(soup)
	ul = soup.findAll("ul",{"class":"list-4-col"})
	a = ul[0].findAll("a")
	# print(a)
	# quit()
	for i in range(0,len(a)):
		myrecord = [a[i].text,"https://www.doximity.com"+a[i]['href']]
		print(a[i].text)
		insertcsv(myrecord)
	pagination(a[len(a)-1]['href'])

def pagination(rec):
	con = url+"?after="+rec[1:]
	print(con)
	time.sleep(20)
	soup(con)


def insertcsv(records):
	with open(filename, 'a', newline='',encoding="utf-8") as csvfile:
		csvwriter = csv.writer(csvfile)
		csvwriter.writerow(records)



try:
	soup = soup(url)
except Exception as e:
	print(e)




