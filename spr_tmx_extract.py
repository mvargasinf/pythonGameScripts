import sys, Tkinter, tkFileDialog, os, glob, shutil
root = Tkinter.Tk()
root.withdraw()

locationHex = 0
number = 0

def Main():
# ----------------- File Opener -----------------#    
    fileOpened = tkFileDialog.askopenfilename()
# ----------------- FileWriterLoop -----------------#
    while True:
# ----------------- IterationAdvance -----------------#        
        number = number + 1
# ----------------- NameGen -----------------#
        name = os.path.splitext(fileOpened)[0] + '_' + str(number) + '.tmx'
# ----------------- DataReader -----------------#
        tmxReader = open(fileOpened, 'rb')
        tmxRead = tmxReader.read()
        tmxReader.seek(0,2)
        end = tmxReader.tell()
# ----------------- DataWriter -----------------#
        tmx_writer = open(name, 'wb')
        dataPos = tmxRead.find('TMX0',locationHex)
        locationHex = tmxRead.find('TMX0',locationHex + 1)
        tmx_writer.write(tmxRead[dataPos-8:locationHex-8])
# ----------------- FinalWrite -----------------#
        if locationHex == -1:
            print 'Error: Reached end of list'
            tmx_writer.write(tmxRead[dataPos:end] + b'\x00')
            tmx_writer.close()
# ----------------- ContinueCode -----------------#
            Continue()
        
def Continue():
# ----------------- Dummy Remover -----------------#
    for sizeFile in glob.glob('*.tmx'):
        fileremove= os.path.getsize(sizeFile)
        if fileremove == 0:
            os.remove(sizeFile)
            
# ----------------- File Mover -----------------#
    for files in glob.glob('*.tmx'):
        if not os.path.exists('tmx_extracted/'+ files):
            shutil.move(files, 'tmx_extracted/')
            
# ----------------- Continue? ----------------- #            
    yesNo = raw_input('Want to continue? (y,n) ')
    if yesNo == 'y':
        TrueStruggle()
    if yesNo == 'n':
        sys.exit()
    
def TrueStruggle():
# ----------------- MainScreeen ----------------- #

    print '======SPR to TMX Converter======'
    print '======By ThatTrueStruggle======'
    
# ----------------- TMXFolder Creator ----------------- #
    if not os.path.exists('tmx_extracted'):
        os.makedirs('tmx_extracted')
# ----------------- Main Code ----------------- #
    Main()      
