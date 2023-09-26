# kevin beideman

# import needed modules to get JSON from web
import json
import requests
from io import BytesIO

from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.geometry("800x300")

topFrame = Frame(root)
topFrame.pack(side=TOP)
middleFrame=Frame(root)
middleFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack()

headerLabel= Label(topFrame, text=" Rick and Morty Characters ")
headerLabel.pack(fill=X)

numLabel= Label(topFrame, text=" Character  ")
numLabel.pack(side=LEFT)
numOptions = range(1,827 )
number=StringVar()
number.set(numOptions[0])
numDrop = OptionMenu(topFrame, number, *numOptions)
numDrop.pack(side=LEFT)

# replace pass with code that 
# retrieves the user's choice for a number
# concantenates that on the end of https://rickandmortyapi.com/api/character/
# Goes to that URL to get the JSON
# Get the name, species, type and image (url) properties and display them
def getCharInfo():
   userChoice = number.get()

   url = "https://rickandmortyapi.com/api/character/{}".format(userChoice)

   myHeaders={
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
   }

   response = requests.get(url, headers=myHeaders)
   charInfo = json.loads(response.text)
   name = charInfo["name"]
   species = charInfo["species"]
   type = charInfo["type"]
   imgLink = charInfo["image"]

   characterData.config(text="Name: {} \nSpecies: {}\nType: {}".format(name, species, type))
   # https://stackoverflow.com/questions/65635835/displaying-image-from-url-in-python-tkinter
   # https://stackoverflow.com/questions/38856128/unable-to-load-an-image-from-an-url-at-tkinter
   imgResponse = requests.get(imgLink)
   imgInfo = Image.open(BytesIO(imgResponse.content))
   img = ImageTk.PhotoImage(imgInfo)
   imageHold.config(image=img)
   imageHold.image = img 


getCharacterButton = Button(middleFrame, text="Get Character Info", command=getCharInfo)
getCharacterButton.pack()

characterHeader= Label(bottomFrame, text="Character Data")
characterHeader.pack(fill=X)
characterData= Label(bottomFrame, text="---")
characterData.pack(fill=X)

imageHold = Label(bottomFrame)
imageHold.pack()

root.mainloop() 