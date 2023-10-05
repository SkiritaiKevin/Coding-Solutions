# Kevin Beideman

import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# import modules for reading JSON from web
import requests
import json 

# Read the JSON found at  http://www1.lasalle.edu/~blum/c343wks/PinkFloyd.json

url = "http://www1.lasalle.edu/~blum/c343wks/PinkFloyd.json"

myHeaders={
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}

myParams = {

}

response = requests.get(url, params=myParams, headers=myHeaders)
songInfo = json.loads(response.text)
 
# Prompt user for year between 1967 and 1987

userYear = int(input("Pick a year between 1967 and 1987. "))

# Loop through the array/list 

for i in range(len(songInfo)-1, -1, -1):
    if songInfo[i]["Year"] < userYear:
        songInfo.pop(i)


# Write code that deletes any songs that were written before the user's input year

# write the edited JSON to a new file

with open("newJson.json", "w") as jsonFile:
    jsonFile.write(json.dumps(songInfo, indent=2))
