# datMythEditor - test
# for use with Python 2.x (tested on 2.7.9)
import Tkinter, tkFileDialog
root = Tkinter.Tk()
root.withdraw()

def Main():
    
    global thatReader
    thatReader = open(tkFileDialog.askopenfilename(title='Open a message file!', filetypes=[('Message File', '*.bmd')]), 'rb').read()
    mythName = raw_input('What myth would you like to edit/view?: ')
    
    global size_in_dec
    size_offset_dec = thatReader.find(mythName) + 32
    size_offset_hex = thatReader[size_offset_dec].encode('hex')
    size_in_dec = int(str(size_offset_hex), 16)
    start_offset_dec = size_offset_dec + 3
    true_text = start_offset_dec + 7

    print "Size of text: " + str(size_in_dec) + '\n'
    print thatReader[true_text:start_offset_dec + size_in_dec]
    
    #newString()

def newString():
    thatWriter = open('DATMyth_new.bmd', 'wb').write(thatReader)
    
    newText = raw_input("What is the new text string? (size can not exceed 255.):\n")

    if len(newText) > 255:
        print "Sorry, your text exceeds 255!"
        restart()
    if len(newText) > size_in_dec:
        size_in_dec = size_in_dec - 1
        
        print "Text exceeded normal text, appending to file..."
        
def restart():
    newString()
    
Main()
