mythWriter = open('MythDAT.txt', 'w') # not working
datMyth = open('DATMYTH.bmd', 'rb').read()
myth = datMyth.find('myth')
locationHex = -1
locationHexFirst = -1
number = 0
numberbefore = 1

while True:
    number = number + 1
    numberbefore = numberbefore + 1
    
    findlessbeforeten = 'myth_00' + str(numberbefore)
    findlessbeforehund = 'myth_0' + str(numberbefore)
    findlessbeforelse = 'myth_' + str(numberbefore)
    
    findlessten = 'myth_00' + str(number)
    findlesshund = 'myth_0' + str(number)
    findelse = 'myth_' + str(number)
    
    
    if number < 10:
        locationHexFirst = datMyth.find(findlessbeforeten , myth + 1)
        locationHex = datMyth.find(findlessten, myth + 1)
    elif number < 100:
        locationHexFirst = datMyth.find(findlessbeforehund , myth + 1)
        locationHex = datMyth.find(findlesshund , myth + 1)
    else:
        locationHexFirst = datMyth.find(findlessbeforelse , myth + 1)
        locationHex = datMyth.find(findelse, myth + 1)
        
    if locationHex == -1:
        print 'Error: Reached end of list'
        sys.exit()

    datMyth1 = datMyth[locationHex:locationHex+8] + '\n'
    datMyth2 = datMyth[locationHex+42:locationHexFirst-2] + '\n' + '\n'
    print datMyth1
    print datMyth2
    mythWriter.write(datMyth1)
    mythWriter.write(datMyth2)
