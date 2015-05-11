import sys
def main():
    usageCommands = '''
    Importing: TheGoldenSprite.py -i <FileName.tmx> <FileName.spr> <OutputName.spr>
    Exporting: TheGoldenSprite.py -x <FileName.spr>
    '''
    try:
        if len(sys.argv) < 0:
            print "Invalid argument!"
            print usageCommand
            exit()
            
        if len(sys.argv) > 0:
            if sys.argv[1] == "-x":
                print "Great, extracting!"
                filePath = sys.argv[2]
                data = open(filePath, 'rb')
                dataRead = data.read()
                tmxCount = dataRead.count('TMX0')
                locationHex = 0
                number = 0
                
                while True:
                    chunkWriter = open(filePath + str(number) + ".tmx", "wb")
                    number = number + 1
                    pos = dataRead.find('TMX0', locationHex)
                    locationHex = dataRead.find('TMX0', locationHex + 1)
                    chunkWriter.write(dataRead[pos-8:locationHex-8])
                    
                    if number == tmxCount:
                        chunkWriter.write(dataRead[pos:len(dataRead)]+ b'\x00') 
                        chunkWriter.close()
                        print "Finished extracting!"
                        exit()
                        
            if sys.argv[1] == "-i":
                if ".tmx" in sys.argv[2]:
                    if ".spr" or ".bin" in sys.argv[3]:
                        if ".spr" or ".bin" in sys.argv[4]:
                            tmxData = open(sys.argv[2], "rb").read()
                            sprData = open(sys.argv[3], "rb").read()
                            sprWrite = open(sys.argv[4], "wb")
                            sprWrite.write(sprData)
                            
                            nameBegin = tmxData.find("TMX0")
                            name = tmxData[nameBegin + 28:nameBegin + 56].rstrip(' \t\r\n\0')
                            nameTMXPos = sprData.find(name) - 36 # find name, and go back 36 bytes
                            
                            if len(name) == 0:
                                print "No name found, assuming only one TMX is there."
                                only = nameBegin - 8
                                sprWrite.seek(only)
                                sprWrite.write(tmxData)
                                sprWrite.close()
                                print "Finished writing SPR file!!"
                                exit()
                                
                            else:
                                sprWrite.seek(nameTMXPos)
                                sprWrite.write(tmxData)
                                sprWrite.close()
                                print "Finished writing SPR file!!"
                                exit()
                                
            elif not sys.argv[1] == "-x" or "-i":
                print "Invalid argument!"
                print usageCommands
                exit()
                
            
    except IndexError:
        # heh, throw it away
        print ""
        
if __name__ == "__main__":
	main()
