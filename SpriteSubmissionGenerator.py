import Tkinter, tkFileDialog
root = Tkinter.Tk()
root.withdraw()
name = tkFileDialog.askopenfilename(title='Open a PM File!')

data = open(name, "r").read()
dataFile = open("pm_thread_sub.txt", "w")
count = data.count("[tsricon")
number = 0
last = 0
first = 0

while True:
    number = number + 1
    first = data.find("[tsricon", first + 1)
    last = data.find("[/tsricon]", last + 1)
    
    prints = data[first:last+10]
    dataFile.write(prints)
    print prints
    
    if number == count:
        raw_input("\nDone! Output has been written to pm_thread_sub.txt! Press enter to continue")
        exit()
