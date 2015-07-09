number = 0
tmxInstancePos = 0

sprName = raw_input("Name of the SPR importing your TMX to? ")
tmxName = raw_input("Name of the TMX? ")
sprData = open(sprName, "rb").read()
tmxData = open(tmxName, "rb").read()

noName = raw_input("Does the SPR file have names that you want to import over? (y,n) ")
if noName == "y":
	nameTMX = raw_input("What is the name of the instance you want to import over? ")
	sprNamePos = sprData.find(nameTMX)
	tmxNamePos = tmxData.find(nameTMX)

	if sprNamePos and tmxNamePos == -1:
		print("No name instance found!")
		exit(0)
	print("Found name, using new position...")
	sprNamePos = sprNamePos - 36
	newSPRName = raw_input("What is the new name for your SPR? ")
	sprDataWriter = open(newSPRName, "wb")
	sprDataWriter.write(sprData)
	sprDataWriter.seek(sprNamePos)
	sprDataWriter.write(tmxData)
	sprDataWriter.close()
	raw_input("Finished! Press enter to exit. ")
	exit(0)

if noName == "n":
	tmxInstanceCount = sprData.count("TMX0")
	print(str(tmxInstanceCount)+ " tmx instances found.")
	replaceInstance = raw_input("OK, which one do you want to replace? ")
	if int(replaceInstance) > tmxInstanceCount:
		print("Invalid instance! ")
		exit(0)
	tmxInstancePos = sprData.find("TMX0", sprData.find("TMX0") + int(replaceInstance))
	tmxInstancePos = tmxInstancePos - 8
	newSPRName = raw_input("What is the new name for the SPR? ")
	sprDataWriter = open(newSPRName, "wb")
	sprDataWriter.write(sprData)
        sprDataWriter.seek(tmxInstancePos)
	sprDataWriter.write(tmxData)
	sprDataWriter.close()
	raw_input("Finished! Press enter to exit. ")
	exit(0)
