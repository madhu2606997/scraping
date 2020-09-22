import requests
import json
import csv


url = "https://www.apolloclinic.com/list/getDoctor"

# payload = "city=Hyderabad&state=Telangana&type=all&specialist=Cardiologist&area=&doctorname=&page_num=1&limit=100"
# payload = "city=&state=&type=specialist&specialist=Obstetrics%20%26%20Gynaecology&area=&doctorname=&page_num=1&limit=1000"
# payload = "city=&state=&type=specialist&specialist=Cardiology&area=&doctorname=&page_num=1&limit=1000"
# payload = "city=&state=&type=specialist&specialist=Orthopedic%20Surgeon&area=&doctorname=&page_num=1&limit=1000"
payload = "city=&state=&type=specialist&specialist=Internal%20Medicine&area=&doctorname=&page_num=1&limit=1000"
headers = {
    'content-type': "application/x-www-form-urlencoded",
    
    }

response = requests.request("POST", url, data=payload, headers=headers)

temp = json.loads(response.text)
data = temp['pagination']
filename = "clinic.csv"
with open(filename, 'a', newline='',encoding="utf-8") as csvfile:
		csvwriter = csv.writer(csvfile)
		for i in data:
			# print(i)
			name = i['3']+' '+i['1']
			qual = i['8']
			spec = i['9']
			avail = i['14']
			loc = str(i['28'])+'-'+str(i['29'])
			exp = i['7']
			myrecord = [name,qual,exp,spec,avail,loc]
			print(myrecord)
			csvwriter.writerow(myrecord)

