import requests
import json
from datetime import datetime,timedelta
today=datetime.today()
print(today)
final_dates=[]
pin=['302029','302009','302020','302029']
num_days=7
all_dates=[]

for i in range(num_days):
    all_dates.append(today + timedelta(i))
print(all_dates)

while True:
    
    for p in pin:
        for d in final_dates:
            URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(p,d)
            
            result=requests.get(URL)
            #print(result.text)
            
            json_result=result.json()
            
            if json_result["centers"]:
                for center in json_result["centers"]:
                    for session in center["sessions"]:
                        print('-'*100)
                        print("Pincode: "+p)
                        print("Date: "+d)
                        print("Center Name: ", center["name"])
                        print("Center Address: ",center["address"])
                        print("Vaccine Type: ",session["vaccine"])
                        print("-"*100)
