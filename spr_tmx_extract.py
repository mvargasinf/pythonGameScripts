import sys, Tkinter, tkFileDialog, os, glob, shutil
root = Tkinter.Tk()
root.withdraw()


def Main():
    fileOpened = tkFileDialog.askopenfilename()
    locationHex = 0
    number = 0

    while True:
        tmxRead = open(fileOpened, 'rb').read()
        dataPos = tmxRead.find('TMX0',locationHex)
        number = number + 1
        name = os.path.splitext(fileOpened)[0] + str(number) + '.tmx'
        
        tmx_writer = open(name, 'wb')

        locationHex = tmxRead.find('TMX0',locationHex + 1)
        print locationHex

        tmx_writer.write(tmxRead[dataPos-8:locationHex-8])
        tmx_writer.close()
        
        if locationHex == -1:
            print 'Error: Reached end of list'   
            Continue()
        
def Continue():
    for files in glob.glob('*.tmx'):
        if not os.path.exists('tmx_extracted/'+ files):
            shutil.move(files, 'tmx_extracted/')
        if os.path.exists('tmx_extracted/'+ files):
            os.remove(files)
            print 'Sorry, but ' + files + ' already exists in the TMX_Extracted folder'

    yesNo = raw_input('Want to continue? (y,n) ')

    if yesNo == 'y':
        TrueStruggle()
    if yesNo == 'n':
        sys.exit()
    
def TrueStruggle():
    print '======SPR to TMX Converter======'
    print '======By ThatTrueStruggle======'

    if not os.path.exists('tmx_extracted'):
        os.makedirs('tmx_extracted')
    Main()

TrueStruggle()        
