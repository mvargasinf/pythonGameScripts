import Tkinter, tkFileDialog

root = Tkinter.Tk()
root.withdraw()

data_tmx = open(tkFileDialog.askopenfilename(title='Open a TMX file.'), "rb").read().close()
data_spr = open(tkFileDialog.askopenfilename(title='Open a SPR file.'), "rb").read().close()
new_spr = open("output.spr", "wb")
new_spr.write(data_spr)

nameBegin = data_tmx.find("TMX0")
nameEnd = nameBegin

name = data_tmx[nameBegin + 28:nameEnd + 28].rstrip(' \t\r\n\0') # remove trailing null
nameTMXPos = data_spr.find(name) - 36 # find name, and go back 36 bytes

if len(name) == 0:
    print "No name found, assuming only one TMX is there."
    only = nameBegin - 8
    new_spr.seek(only)
    new_spr.write(data_tmx)
    new_spr.close()
    
new_spr.seek(nameTMXPos)
new_spr.write(data_tmx)
new_spr.close()
