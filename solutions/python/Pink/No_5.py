# http://www1.lasalle.edu/~blum/c341wks/Python_tkinter_room_schedule_demo.zip

'''
    Create a tkinter interface that allows the user to 
    create a "web safe" color
    Take individual hex codes for red, green and blue 
    Put them together (with a #) to display hexcode text and color
'''

import tkinter as tk

root = tk.Tk()
root.geometry("400x400")   # size of interface width x height
root.pack_propagate(0)

# establish three main vertical regions
topFrame = tk.Frame(root, bg="darkred", pady="10", padx="10", 
                    width="400", height="100")     # frame is a container, root is its parent
topFrame.pack(side=tk.TOP)    # pack() helps determine where an item will be placed
topFrame.pack_propagate(0)
# without pack_propagate(0) tkinter sizes things to just the size needed
# with pack_propagate(0) you must set a width and height or they are by default 0
middleFrame = tk.Frame(root, bg="white", pady="10", padx="10", 
                       width="400", height="75")
middleFrame.pack()
middleFrame.pack_propagate(0)
bottomFrame = tk.Frame(root, bg="navy", pady="10", padx="10", 
                       width="400", height="225")
bottomFrame.pack()
bottomFrame.pack_propagate(0)

# https://www.tutorialspoint.com/python/tk_label.htm
headerLabel = tk.Label(topFrame, text=" Create a Web Safe Color ", 
                       bg="white", fg="navy", font="24")
# bg background color  fg foreground/font color 
headerLabel.pack(fill=tk.X)      # fill container horizontally
# https://www.tutorialspoint.com/python/tk_pack.htm

redLabel = tk.Label(topFrame, text=" Red ", 
                     bg="navy", fg="white", padx="2", font="12")
redLabel.pack(side=tk.LEFT)

# https://www.tutorialspoint.com/how-to-detect-when-an-optionmenu-or-checkbutton-changes-in-tkinter
redOptions = ["00", "33", "66", "99", "CC", "FF"]    # list choices for rooms
red = tk.StringVar()                        # variable for user's choice of room 
red.set(redOptions[0])                  # initialize user's choice to first option of list 
redDrop = tk.OptionMenu(topFrame, red, *redOptions)   
redDrop.pack(side=tk.LEFT)

# label for day
greenLabel = tk.Label(topFrame, text=" Green ", bg="navy", 
                    fg="white", padx="2", font="12")
greenLabel.pack(side=tk.LEFT)

greenOptions = ["00", "33", "66", "99", "CC", "FF"]    # list choices for rooms
green = tk.StringVar()                        # variable for user's choice of room 
green.set(greenOptions[0])                  # initialize user's choice to first option of list 
greenDrop = tk.OptionMenu(topFrame, green, *greenOptions)   
greenDrop.pack(side=tk.LEFT)

# label for blue
blueLabel = tk.Label(topFrame, text="Blue", bg="navy", 
                     fg="white", padx="2", font="12")
blueLabel.pack(side=tk.LEFT)

blueOptions = ["00", "33", "66", "99", "CC", "FF"]    # list choices for rooms
blue = tk.StringVar()                        # variable for user's choice of room 
blue.set(blueOptions[0])                  # initialize user's choice to first option of list 
blueDrop = tk.OptionMenu(topFrame, blue, *blueOptions)   
blueDrop.pack(side=tk.LEFT)


# function called by button
def makecolor():

   hexRed = red.get()
   hexGreen = green.get()
   hexBlue = blue.get()
   hexcode = "#"+hexRed+hexGreen+hexBlue
   print(hexcode)
   hexLabel.configure(text=hexcode)
   colorLabel.configure(bg=hexcode)

# button 
makeColorButton = tk.Button(middleFrame, text=" Make Web Safe Color ", 
                           command=makecolor, font="24", padx="5", pady="5")
makeColorButton.pack()


colorHeader = tk.Label(bottomFrame, text=" Hexcode for Color ", 
                         font="12", padx="2", pady="2")
colorHeader.pack(fill=tk.X)
hexLabel = tk.Label(bottomFrame, text="---", bg="darkred", 
                         fg="white", font="12", padx="2", pady="2")
hexLabel.pack(fill=tk.X)
colorLabel = tk.Label(bottomFrame, text="", font="12", width=200, height=200)
colorLabel.pack(fill=tk.X)

# loop to keep interface displaying
root.mainloop()
