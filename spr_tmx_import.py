import sys, Tkinter, tkFileDialog, os

root = Tkinter.Tk()
root.withdraw()


def Main():
    fileOpenedSPR = tkFileDialog.askopenfilename(title='Open a SPR file.')
    fileOpenedTMX = tkFileDialog.askopenfilename(title='Open a TMX file.')

    spr_reader = open(fileOpenedSPR, 'rb')
    tmx_reader = open(fileOpenedTMX, 'rb')
    spr_writer = open('output.spr', 'wb')

    spr_read = spr_reader.read()
    tmx_data = tmx_reader.read()
    tmx_reader.seek(0,2)
    tmx_reader.close()
    tmxName = raw_input('What tmx do you want to replace? ')

    if spr_read.find(tmxName) == -1:
        print 'Sorry, but that does not exist.'
        sys.exit()
    name_pos = spr_read.find(tmxName)
    name_pos = name_pos-36
    spr_writer.write(spr_read)
    spr_writer.seek(name_pos)
    spr_writer.write(tmx_data)
    spr_writer.close()
    
    raw_input('Data imported correctly! Press enter to continue!')
Main()
