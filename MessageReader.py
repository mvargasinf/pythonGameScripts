import struct, os
number = 1 # this is for some offset table stuff
textOffsets = []
textNames = []

def readString(data, length, pos):
	return data[pos:pos+length]

def findString(data, string):
	return data.find(string)

def lendianness(bigEndian):
	# return a little endian value
	return int(struct.pack("<I", bigEndian).encode("hex")[0:4], 16)

def UInt16(data, pos):
	# return a UInt16 value from the given stream
	return int(data[pos].encode("hex"), 16)

def UInt32(data, pos):
	# return a UInt32 value from the given stream
	return int(data[pos:pos+2].encode("hex"), 16)

def UInt64(data, pos):
	# return a UInt64 value from the given stream, a made up int
	return int(data[pos:pos+4].encode("hex"), 16)

def UInt96(data, pos):
	# return a UInt96 value from the given stream, a made up int; 12 bytes long
	return int(data[pos:pos+6].encode("hex"), 16)

text = open(raw_input("Provide a file with a message in it. "), "rb").read()
if findString(text, "MSG1") == -1:
	print "Invalid message file!"
	exit(0)

# find the MSG1 magic indicator. If not found then this isn't a valid message file
MSG1Magic = findString(text, "MSG1")
textCount = hex(lendianness(UInt32(text, MSG1Magic + 12))).lstrip("0x")
entryCount = UInt16(text, MSG1Magic + 16)
pos = MSG1Magic + 24
print textCount, entryCount

# some looping here
while int(entryCount) > number:
	null_64 = UInt64(text, pos);pos += 4
	textOffset_1 = lendianness(UInt32(text, pos)) + 32;pos += 2;number += 1
	textOffsets.append(textOffset_1)
	null_96 = UInt96(text, pos);pos += 6
	textOffset_2 = int(lendianness(UInt32(text, pos))) + 32;pos += 2;number += 1
	textOffsets.append(textOffset_2)
	null_32 = UInt32(text, pos);pos += 2

for textOffset in textOffsets:
	textWriter = open("Output.txt", "a+")
	size = UInt16(text, textOffset + 32)
	textNames.append(text[textOffset:textOffset+16])
	textWriter.write(text[textOffset:textOffset+16] + "\n")
	textWriter.write(text[textOffset+42:textOffset+34+size] + "\n\n")
	textWriter.close()

print "Text has been written to Output.txt. Press enter when ready to reimport."
raw_input()