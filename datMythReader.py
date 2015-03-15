datMyth = open('DATMYTH.bmd', 'rb').read()
myth = datMyth.find('myth')
locationHex = -1
number = 0
while True:
    number = number + 1
    if number < 10:
        locationHex = datMyth.find('myth_00' + str(number), myth + 1)
    elif number < 100:
        locationHex = datMyth.find('myth_0' + str(number), myth + 1)
    else:
        locationHex = datMyth.find('myth_' + str(number), myth + 1)
        
    if locationHex == -1:
        print 'Error: Reached end of list'
        break
    print datMyth[locationHex:]
    print datMyth[locationHex+42:]
