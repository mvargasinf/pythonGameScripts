import os
print "Written by ThatTrueStruggle ^_^"
files = raw_input("What .DAT file do you want to read from? ")
string = open(files, "rb").read()

newString = string[int(raw_input("What positions do you start from?(in dec?) ")):int(raw_input("What positions do you end from? (in dec?) "))]
write = open(os.path.basename(files) + ".text", "ab+")
write.write(newString)
write.close()
