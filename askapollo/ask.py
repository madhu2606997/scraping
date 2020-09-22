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

def ask_apollo(url,loc):
	driver = webdriver.Chrome(
        options=options
	)
	filename = "askapollo1.csv"
	# fields = ["Name",'Qualification','Speciality','Experience','Language','Timings','Hospital Address','Position','']
	driver.get(url)
	time.sleep(2)
	main_div = driver.find_elements_by_tag_name('figcaption')
	print(len(main_div))
	with open(filename, 'a', newline='',encoding="utf-8") as csvfile:
		csvwriter = csv.writer(csvfile)
		for i in range(1,len(main_div)):
			soup = BeautifulSoup(main_div[i].get_attribute('outerHTML'), "html.parser")
			# print(soup)
			# input()ss
			name = soup.find('h2').text.replace('View Profile','').strip()

			qualification = soup.select_one('div:nth-child(2) > ul >li:nth-child(1)')
			if(qualification !=None):
				qa1 = qualification.text.replace('Qualification:','').strip()
			else:
				qa1 = "-"
			speciality = soup.select_one(' div:nth-child(2) > ul >li:nth-child(2)')
			if(speciality !=None):
				sp = speciality.text.replace('Speciality:','').strip()
			else:
				sp = "-"

			experience = soup.select_one(' div:nth-child(2) > ul >li:nth-child(3)')
			if(experience !=None):
				ex = experience.text.replace('Experience:','').strip()
			else:
				ex = "-"
			language = soup.select_one(' div:nth-child(2)> ul >li:nth-child(4)')
			if(language !=None):
				lg = language.text.replace('Language:','').strip()
			else:
				lg = "-"
			timings = soup.select_one(' div:nth-child(3) > ul >li:nth-child(1)')
			if(timings !=None):
				tm = timings.text.strip()
			else:
				tm = "-"
			hosp = soup.select_one(' div:nth-child(3) > ul >li:nth-child(2)')
			if(hosp !=None):
				hp = hosp.text.strip()
			else:
				hp = "-"
			myrecord = [name,qa1,sp,ex,lg,tm,hp,i,"internal-medicine-physician",loc]
			print(myrecord)
			csvwriter.writerow(myrecord)
			time.sleep(5)
	driver.close()

	# quit()

	# 	# csvwriter.writerow(fields)
	# 	# name = driver.find_elements_by_css_selector('figcaption > h2') 
	# 	name = main_div[0].find_elements_by_tag_name('h2') 
	# 	# qualification = driver.find_elements_by_css_selector('figcaption > div:nth-child(2) > ul >li:nth-child(1)')
	# 	qualification = main_div[0].find_element_by_css_selector('div:nth-child(2) > ul >li:nth-child(1)')
	# 	speciality = driver.find_elements_by_css_selector('figcaption > div:nth-child(2) > ul >li:nth-child(2)')
	# 	experience = driver.find_elements_by_css_selector('figcaption > div:nth-child(2) > ul >li:nth-child(3)')
	# 	language = driver.find_elements_by_css_selector('figcaption > div:nth-child(2)> ul >li:nth-child(4)')
	# 	timings = driver.find_elements_by_css_selector('figcaption > div:nth-child(3) > ul >li:nth-child(1)')
	# 	hosp = driver.find_elements_by_css_selector('figcaption > div:nth-child(3) > ul >li:nth-child(2)')
	# 	print(len(name),len(qualification),len(speciality),len(experience),len(language),len(timings),len(hosp))
	# 	# checkpagination()
	# 	for i in range(0,len(name)):
	# 		name1 = name[i].text.replace('View Profile','').strip()
	# 		qa1 = qualification[i].text.replace('Qualification:','').strip() if qualification[i].text!='' else ""
	# 		print(name1,qa1)
	# 		myrecord = [name[i].text.replace('View Profile','').strip(),qualification[i].text.replace('Qualification:','').strip(),speciality[i].text.replace('Speciality:','').strip(),experience[i].text.replace('Experience:','').strip(),language[i].text.replace('Language:','').strip(),timings[i].text.strip(),hosp[i].text.strip(),i,"Cardiologist",loc]
	# 		# # print(myrecord)
	# 		# csvwriter.writerow(myreco)

	# 		# print(timings[0].text)

loc = ["hyderabad","bangalore","chennai","pune","mumbai","delhi"]

for i in loc:
	# url1 = "https://www.askapollo.com/physical-appointment/cardiologist/"+i
	# url1 = "https://www.askapollo.com/physical-appointment/orthopaedic-surgeon/"+i
	# url1 = "https://www.askapollo.com/physical-appointment/gynecologist-and-obstetrician/"+i
	url1 = "https://www.askapollo.com/physical-appointment/internal-medicine-physician/"+i
	print(url1,i)

	ask_apollo(url1,i)

# ask_apollo("https://www.askapollo.com/physical-appointment/cardiologist/bangalore")