import json
import os 

os.chdir(os.path.dirname(os.path.realpath(__file__))) # need this so the json ends up in same folder

url = "https://jsonplaceholder.typicode.com/posts"

import requests 

myHeaders={
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}

myParams = {}

response = requests.get(url, params=myParams, headers=myHeaders)

postInfo = json.loads(response.text)

for i in range(len(postInfo)-1, -1, -1):
    if postInfo[i]["userId"]==5:
        postInfo.pop(i)

with open("newJson.json", "w") as file2:
    file2.write(json.dumps(postInfo,indent=2))


