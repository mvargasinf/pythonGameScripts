import sys, Tkinter, tkFileDialog, os

root = Tkinter.Tk()
root.withdraw()

def Main():
    
    fileOpenedSPR = tkFileDialog.askopenfilename(title='Open a SPR file.')
    fileOpenedTMX = tkFileDialog.askopenfilename(title='Open a TMX file.')

    spr_reader = open(fileOpenedSPR, 'rb').read()
    tmx_reader = open(fileOpenedTMX, 'rb').read()
    extension = os.path.splitext(fileOpenedSPR)[1]

    if extension == '.SPR':
        tmxName = raw_input('What tmx do you want to replace? ')
        spr_writer = open('output.spr', 'wb')
        
        if spr_reader.find(tmxName) == -1:
                print 'Sorry, but that does not exist.'
                sys.exit()

        name_pos = spr_reader.find(tmxName)
        spr_writer.write(spr_reader)
        
        if not spr_reader.find(tmxName, name_pos + 1) == -1:
            print 'Found 2 instances, skipping name...'
            
            truePos = spr_reader.find(tmxName, name_pos + 1)
            truePos = truePos - 36
            spr_writer.seek(truePos)
            spr_writer.write(tmx_reader)
            spr_writer.close()
        else:
            name_pos = name_pos - 36
            spr_writer.seek(name_pos)
            spr_writer.write(tmx_reader)
            spr_writer.close()
        
    if extension == '.BIN':
        tmxName = raw_input('What tmx do you want to replace? ')
        spr_writer = open('output.bin', 'wb')
        
        if spr_reader.find(tmxName) == -1:
            print 'Sorry, but that does not exist.'
            sys.exit()

        name_pos = spr_reader.find(tmxName)
        spr_writer.write(spr_reader)
        
        if not spr_reader.find(tmxName, name_pos + 1) == -1:
            print 'Found 2 instances, skipping name...'
            
            truePos = spr_reader.find(tmxName, name_pos + 1)
            truePos = truePos - 36
            spr_writer.seek(truePos)
            spr_writer.write(tmx_reader)
            spr_writer.close()
        else:
            name_pos = name_pos - 36
            spr_writer.seek(name_pos)
            spr_writer.write(tmx_reader)
            spr_writer.close()
            
    raw_input('Data imported correctly! Press enter to continue!')
Main()

    
