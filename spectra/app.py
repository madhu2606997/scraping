from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import datetime
import time
from threading import Thread
import threading
import pprint
from selenium.common.exceptions import NoSuchElementException
import os
import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv



options = Options()
options.headless = True

def spectra(url,loc1):
	driver = webdriver.Chrome(
        options=options
	)
	filename = "1spectra.csv"
	driver.get(url)
	time.sleep(2)
	main_div = driver.find_elements_by_css_selector('.doctorlist')
	# main_div = soup.findAll("div", {"class": "doc-info"})
	print(len(main_div))
	with open(filename, 'a', newline='',encoding="utf-8") as csvfile:
		csvwriter = csv.writer(csvfile)
		for i in range(0,len(main_div)):
			soup = BeautifulSoup(main_div[i].get_attribute('outerHTML'), "html.parser")
			name = soup.select_one('h2.entry-title > a').text.strip()
			try:
				spec = soup.select_one('div.col-lg-7.col-sm-6 > p > a').text
			except Exception as e:
				print(e)
				continue
			loc = soup.select_one('div.article-doclocation').text.replace('View Location','').replace("(   )",'').strip()
			data = soup.select_one('div.col-lg-7.col-sm-6').text.strip()
			qual = data.replace('View Location','').replace("(   )",'').replace(spec,'').replace(loc,'')
			exp = data.replace('View Location','').replace("(   )",'').replace(spec,'').replace(loc,'')
			avail = soup.select_one('div.davailability').text.replace("Availability","").strip()
			# print(name,qual,exp,loc,patscore,avail)
			myrecord = [name,qual,exp,loc,spec,avail,loc1]
			print(myrecord)
			csvwriter.writerow(myrecord)
	driver.close()

	

# spectra("https://www.apollospectra.com/doctors/chennai/Cardiologist","chennai")
# spectra("https://www.apollospectra.com/doctors/hyderabad/","hyderabad")
# spectra("https://www.apollospectra.com/doctors/hyderabad/?sf_paged=2","hyderabad")
# spectra("https://www.apollospectra.com/doctors/hyderabad/?sf_paged=3","hyderabad")
# spectra("https://www.apollospectra.com/doctors/delhi/","delhi")
			# print(main_div[i].text)
			# soup = BeautifulSoup(main_div[i].get_attribute('outerHTML'), "html.parser")

for i in range(0,3):
	url = "https://www.apollospectra.com/doctors/pune/?sf_paged="+str(i)
	spectra(url,'pune')
	# print(i)