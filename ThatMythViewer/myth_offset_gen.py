import sys
mythWriter = open('MythNumber.py', 'w') 
datMyth = open('DATMYTH.bmd', 'rb').read()
myth = datMyth.find('myth')
locationHex = -1
number = 0

while True:
    number = number + 1
    findlessten = 'myth_00' + str(number)
    findlesshund = 'myth_0' + str(number)
    findelse = 'myth_' + str(number)
    
    if number < 10:
        locationHex = datMyth.find(findlessten, myth + 1)
    elif number < 100:
        locationHex = datMyth.find(findlesshund , myth + 1)
    else:
        locationHex = datMyth.find(findelse, myth + 1)
        
    if locationHex == -1:
        print 'Error: Reached end of list'
        sys.exit()

    datMyth1 = datMyth[locationHex:locationHex+8] + ' = ' + str(locationHex+8) + '\n'
    print datMyth1
    mythWriter.write(datMyth1)
    
        
