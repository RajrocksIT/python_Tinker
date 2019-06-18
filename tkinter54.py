# Frame for the date spinners

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

import os


mainWindow = tkinter.Tk()

mainWindow.title("Grid Demo")
mainWindow.geometry('640x480-8-200')

label = tkinter.Label(mainWindow, text="Tkinter Grid Demo")
label.grid(row=0, column=0, columnspan=3)


mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=3)
mainWindow.columnconfigure(3, weight=3)
mainWindow.columnconfigure(4, weight=3)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)


fileList = tkinter.Listbox(mainWindow)
fileList.grid(row=1, column=0, sticky='nsew', rowspan=2)
fileList.config(border=2, relief='sunken')


for zone in os.listdir('C:/Windows/System32'):
    fileList.insert(tkinter.END, zone)


listScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=fileList.yview)
listScroll.grid(row=1, column=1, sticky='nsw', rowspan=2)
fileList['yscrollcommand'] = listScroll.set

# Frame for the radio buttons
optionFrame = tkinter.LabelFrame(mainWindow, text="File Details")
optionFrame.grid(row=1, column=2, sticky='ne')

rbValue = tkinter.IntVar()
rbValue.set(3)

# Radio buttons
radio1 = tkinter.Radiobutton(optionFrame, text="Filename", value=1, variable=rbValue)
radio2 = tkinter.Radiobutton(optionFrame, text="Path", value=2, variable=rbValue)
radio3 = tkinter.Radiobutton(optionFrame, text="Timestamp", value=3, variable=rbValue)
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')

# widget to display the result
resultLabel = tkinter.Label(mainWindow, text="Result")
resultLabel.grid(row=2, column=2, sticky='nw')
result = tkinter.Entry(mainWindow)
result.grid(row=2, column=2, sticky='sw')

# Frame for the time spinners
timeFrame = tkinter.LabelFrame(mainWindow, text="Time")
timeFrame.grid(row=3, column=0, sticky='new')

# Time spinners
hourSpinner = tkinter.Spinbox(timeFrame, width=2, values=tuple(range(0, 24)))
minuteSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)      # "from" is a reserved word in python. So we used from_
secondSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
hourSpinner.grid(row=0, column=0)
tkinter.Label(timeFrame, text=':').grid(row=0, column=1)
minuteSpinner.grid(row=0, column=2)
tkinter.Label(timeFrame, text=':').grid(row=0, column=3)
secondSpinner.grid(row=0, column=4)
timeFrame['padx'] = 36

# Frame for the date spinners
dateFrame = tkinter.Frame(mainWindow)     # newly added
dateFrame.grid(row=4, column=0, sticky='new') # newly added

# date labels
dayLabel = tkinter.Label(dateFrame, text="Day")      # newly added
monthLabel = tkinter.Label(dateFrame, text="Month")  # newly added
yearLabel = tkinter.Label(dateFrame, text="Year")    # newly added
dayLabel.grid(row=0, column=0, sticky='w')           # newly added
monthLabel.grid(row=0, column=1, sticky='w')         # newly added
yearLabel.grid(row=0, column=2, sticky='w')          # newly added

# date spinners
daySpin = tkinter.Spinbox(dateFrame, width=5, from_=1, to=31)         # newly added
monthSpin = tkinter.Spinbox(dateFrame, width=5, values=("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul",
                                                        "Aug", "Sep", "Oct", "Nov", "Dec"))   # newly added
yearSpin = tkinter.Spinbox(dateFrame, width=5, from_=2000, to=2099)                           # newly added
daySpin.grid(row=1, column=0)                                                                 # newly added
monthSpin.grid(row=1, column=1)                                                               # newly added
yearSpin.grid(row=1, column=2)                                                                # newly added



mainWindow.mainloop()

print(rbValue.get())