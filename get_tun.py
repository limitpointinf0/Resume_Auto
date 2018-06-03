import json
import os 

os.system("curl  http://localhost:4040/api/tunnels > tunnels.json")

with open('tunnels.json') as data_file:    
    datajson = json.load(data_file)

url = datajson['tunnels'][0]['public_url']

with open('url.txt','w+') as f:
    f.write(url)
