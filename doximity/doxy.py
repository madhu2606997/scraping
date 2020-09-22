
import requests
from bs4 import BeautifulSoup
import csv
import time
import mysql.connector
import json

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database = "profiles"
)

options = Options()
options.headless = False
driver = webdriver.Chrome(
        options=options
	)

def login(driver):
	email = driver.find_element_by_id('email')
	email.send_keys("madhu@multipliersolutions.in")
	passw = driver.find_element_by_id('password')
	passw.send_keys("M@dhu2606")
	sign = driver.find_element_by_id('signinbutton')
	sign.click()
	time.sleep(5)



def soup(url):
	driver.get(url)

	time.sleep(2)
	lo = driver.find_elements_by_css_selector('div.signin-download-section.section')
	if(len(lo)!=0):
		login(driver)

	main_div = driver.find_element_by_css_selector('body')
	soup = BeautifulSoup(main_div.get_attribute('outerHTML'), "html.parser")
	# response = requests.get(url)
	# soup = BeautifulSoup(response.content, "html.parser")
	# print(soup)
	return profile(soup)
	# return loginprofile(soup)

def liextract(soup,section):
	lires = []
	try:
		temp = soup.select_one(section)
		for i in temp.findAll("li"):
			lires.append(i.get_text())
	except Exception as e:
		print(e)
	return lires

def gettext(soup,section):
	text=""
	try:
		text = soup.select_one(section).text
	except Exception as e:
		print(e)
	
	return text

def profile(soup):
	mydoc = {}
	mydoc["name"] = gettext(soup,"div.section.center >h1")
	try:
		mydoc["profile_pic"] = soup.select_one("div.profile-photo > img")['src']
	except Exception as e:
		mydoc["profile_pic"]= ""
	mydoc["subspecialty"] = gettext(soup,"p.user-subspecialty")
	mydoc["office"] = gettext(soup,"span.black.profile-contact-labels-wrap")
	mydoc["phone"] = gettext(soup,"div.office-info-telephone").replace("Phone","")
	mydoc["fax"] = gettext(soup,"div.office-info-fax").replace("Fax","")
	mydoc["job-title"] = gettext(soup,"p.user-job-title")
	mydoc["summary"] = gettext(soup,"div.profile-summary-content")
	mydoc["education"] = []
	mydoc["certifications&licences"] = []
	mydoc["publications&presentations"] = []
	mydoc["education"] = liextract(soup,"section.education-info > ul")
	mydoc["certifications&licences"] = liextract(soup,"section.certification-info > ul")
	mydoc["publications&presentations"] = liextract(soup,"section.publication-info div> div > ul")
	mydoc["journals"] = liextract(soup,"section.publication-info div> div:nth-child(2) > ul")
	mydoc["non-journals"] = liextract(soup,"section.non-journal-media > ul")
	mydoc["clinical-trails"] = liextract(soup,"section.trials-info > ul")
	mydoc["lectures"] = liextract(soup,"section.publication-info div> div:nth-child(3) > ul")
	mydoc["press-mentions"] = liextract(soup,"section.press-info > ul")
	mydoc["hospital-info"] = liextract(soup,"section.hospital-info > ul")
	mydoc["award-info"] = liextract(soup,"section.award-info > ul")
	
	return mydoc


def loginprofile(soup):
	mydoc = {}
	mydoc["name"] = gettext(soup,"div.profile-basics-info >h1")
	try:
		mydoc["profile_pic"] = soup.select_one("div.profile-photo > img")['src']
	except Exception as e:
		mydoc["profile_pic"]= ""
	mydoc["subspecialty"] = gettext(soup,"span.profile-specialty")
	mydoc["office"] = gettext(soup,"div.profile-contact-information-office-lines-column")
	mydoc["phone"] = gettext(soup,"div.profile-contact-labels-wrap").replace("Phone","")
	mydoc["fax"] = gettext(soup,"div.office-info-fax").replace("Fax","")

	mydoc["job-title"] = gettext(soup,"p.profile-header-description")
	mydoc["summary"] = gettext(soup,"div#summary>div")
	mydoc["education"] = []
	mydoc["certifications&licences"] = []
	mydoc["publications&presentations"] = []
	mydoc["education"] = liextract(soup,"div#training > ul")
	mydoc["certifications&licences"] = liextract(soup,"div#certifications > ul")
	mydoc["publications&presentations"] = liextract(soup,"div#publications> div> div > div> ul")
	mydoc["journals"] = liextract(soup,"section.publication-info div> div:nth-child(2) > ul")
	mydoc["non-journals"] = liextract(soup,"div#non-journal-media > ul")
	mydoc["committees"] = liextract(soup,"div#committees > ul")
	mydoc["memberships"] = liextract(soup,"div#professional-memberships > ul")
	mydoc["clinical-trails"] = liextract(soup,"div#clinical-trials > ul")
	mydoc["lectures"] = liextract(soup,"section.publication-info div> div:nth-child(3) > ul")
	mydoc["press-mentions"] = liextract(soup,"div#press-mentions > ul")
	mydoc["hospital-info"] = liextract(soup,"div#employments > ul")
	mydoc["award-info"] = liextract(soup,"div#honors > ul")
	return mydoc

def getcsv(filename):
	data = []
	with open(filename, 'r') as file:
	    reader = csv.reader(file)
	    for row in reader:
	        data.append(row[0]+"~"+row[1])
	return data

# url = "https://www.doximity.com/pub/jasvinder-singh-md-9742485"
url = "https://www.doximity.com/profiles/cf162d09-e95d-45de-9673-39fd74299703"
# url = "https://www.doximity.com/pub/jason-wu-do"

res = soup(url)
print(res)
def main():
	myres = {}
	maindata = getcsv("doximity.csv")
	for i in range(0,len(maindata)):
		print(maindata[i])
		url = maindata[i].split("~")[1]
		dname = maindata[i].split("~")[0]
		myres[dname] = soup(url)
		# print(myres[dname])
		mycursor = mydb.cursor()
		sql = "INSERT INTO doximity (name,url,json) VALUES (%s,%s,%s)";
		val = (str(dname),url,str(json.dumps(myres[dname])))
		mycursor.execute(sql,val)
		mydb.commit()
		print(mycursor.rowcount, "record inserted.")
		time.sleep(30)

# main()