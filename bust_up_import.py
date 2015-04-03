# Persona 3/4 Bust Importer
import sys, Tkinter, tkFileDialog, os

root = Tkinter.Tk()
root.withdraw()

def Main():
    
    fileOpenedBIN = tkFileDialog.askopenfilename(title='Open a BIN file.')
    fileOpenedTMX = tkFileDialog.askopenfilename(title='Open a TMX file.')

    bin_reader = open(fileOpenedBIN, 'rb')
    tmx_reader = open(fileOpenedTMX, 'rb').read()
    bin_writer = open('output.bin', 'wb')

    binary_read = spr_reader.read()
    tmxPos = binary_read.find('TMX0')
    tmxPos = tmxPos - 8
    bin_writer.write(binary_read)
    bin_writer.seek(tmxPos)
    bin_writer.write(tmx_reader)
    raw_input('Data imported correctly! Press enter to continue!')
    
Main()
