from scrape_linkedin import ProfileScraper
import pandas as pd
import json

import mysql.connector
import csv

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database = "profiles"
)
# pro = ["andrew-fintel-599b7230/"]
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[2])
        p = row[2].replace('https://www.linkedin.com/in/','')
        if(p!=''):
            pro.append(p)
res = {}

with ProfileScraper(cookie='AQEDATGl_YYFYSDUAAABc8MO0OUAAAFz5xtU5VYAGfdDM0R7QwECX1qXZ8vx03Qf6ptXeSlkoN-8gF5xkdNXRHQO2J8B9y6prcEP6PG70pfgSmWEaUgPUbVZz_BgyTU2FNioIKAjnJ7ZCPWqXSAdZIeh') as scraper:
    for a in pro:
        print(a)
        try:
            profile = scraper.scrape(user=a)
            res[a]=profile.to_dict()
            mycursor = mydb.cursor()
            # sql = "INSERT INTO linkedin (name, json) VALUES ("+res[a]["personal_info"]["name"]+","+str(json.dumps(res[a]))+")";
            sql = "INSERT INTO linkedin (name,profile_name ,json) VALUES (%s,%s,%s)";
            val = (str(res[a]["personal_info"]["name"]),a,str(json.dumps(res[a])))
            print(sql)
            mycursor.execute(sql,val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")

        except Exception as e:
        	print(e)
        	continue
# print(res)

with open("result.json", "w", encoding="utf-8") as f:
    # content = f.write(str(profile.to_dict()))
    json.dump(res, f, ensure_ascii=False, indent=4)

f.close()
