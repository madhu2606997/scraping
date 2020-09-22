import csv

import json

filename = "res-grants.csv"

def insertcsv(records):
	with open(filename, 'a', newline='',encoding="utf-8") as csvfile:
		csvwriter = csv.writer(csvfile)
		csvwriter.writerow(records)


with open('main.json',encoding="utf8") as json_file:
    data = json.load(json_file)
    # print(data)
    for (k, v) in data.items():
    	# myrecord = [k,v['name'],v['profile_pic'],v['subspecialty'],v['office'],v['phone'],v['fax'],v['job-title'],v['summary']]
    	vi = v['support-grants']
    	for i in range(0,len(vi)):
    		myrecord = [k,vi[i]]
    		insertcsv(myrecord)
    print('done')
