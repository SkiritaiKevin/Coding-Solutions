import tkinter as tk
import json
import requests

def findWinner():
    category1 = category.get()
    year1 = year.get()
    # https://python-commandments.org/tkinter-entry-widget/#:~:text=To%20get%20the%20text%20of%20the%20current%20input,v.set%20%28%22I%20love%20Python%21%22%29%20s%20%3D%20v.get%20%28%29

    myHeaders={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

    myParams= {
    "category":category1,
    "year":year1}

    response = requests.get("https://api.nobelprize.org/v1/prize.json", params=myParams, headers=myHeaders)
    winners = json.loads(response.text)
    results = []
    prizes = winners["prizes"]
    for i in prizes:
        for j in i["laureates"]:
            results.append("{} {}".format({j["firstname"]}, {j["surname"]}))
    
    lblResult.config(text="Winners: " + "\n".join(results))

root = tk.Tk()
root.geometry("400x400")
root.pack_propagate(0)

topFrame = tk.Frame(root, bg="blue", pady="10", padx="10", width="400", height="100")
topFrame.pack(side=tk.TOP)
topFrame.pack_propagate(0)

middleFrame = tk.Frame(root, bg="white", pady="10", padx="10", width="400", height="75")
middleFrame.pack()
middleFrame.pack_propagate(0)

bottomFrame = tk.Frame(root, bg="navy", pady="10", padx="10", width="400", height="225")
bottomFrame.pack()
bottomFrame.pack_propagate(0)

categories = ["physics", "chemistry", "medicine", "peace", "literature", "economics"]
category = tk.StringVar()
category.set(categories[0])
selCategories = tk.OptionMenu(topFrame, category, *categories)
selCategories.pack(side=tk.LEFT)

years = []
for i in range(2000,2021):
    years.append(str(i))
year = tk.StringVar()
year.set(years[0])
selYears = tk.OptionMenu(topFrame, year, *years)
selYears.pack(side=tk.RIGHT)

lblResult = tk.Label(bottomFrame, text="", font="12")
lblResult.pack()

buttonFind = tk.Button(middleFrame, text=" Find Prize Winners ", command=findWinner, font="24", padx="5", pady="5") 
buttonFind.pack()

root.mainloop()
