number = 0
firstLocation = 0
pos = 0

spr_name = raw_input("Name of the SPR you want to extract from? ")
spr_data = open(spr_name, "rb").read()
spr_tmx_count = spr_data.count("TMX0")

if spr_tmx_count < 0:
        print("No tmx instances found, closing...")
        exit(0)

print(str(spr_tmx_count) + " tmx instances found.")
all_single = raw_input("Extract all or single? (all or single) ")

if all_single == "all":
	print("Extracting all tmx files from the spr.... ")
	while spr_tmx_count > number:
		number = number + 1
		firstLocation = spr_data.find("TMX0", firstLocation + 1)
		read_size = firstLocation - 4
		read_size = spr_data[read_size : read_size + 4].encode("hex")
		read_size = int(read_size, 16)
		tmx_data = firstLocation - 8

		tmx_data = spr_data[tmx_data:firstLocation + read_size]
		tmxWriter = open(str(number) + ".tmx", "wb")
		tmxWriter.write(tmx_data)
		tmxWriter.close()
	raw_input("Finished! Press enter to exit. ")
	exit(0)

if all_single == "single":
	instance = raw_input("What tmx instance do you want to extract? ")
	if int(instance) > spr_tmx_count:
		print("Instance does not exist. ")
		exit(0)

	while number < int(instance):
		number = number + 1
		pos = spr_data.find("TMX0", pos + 1)

		# wait for increment clock, then use position data
		if number == int(instance):
			tmx_size = pos - 4
			tmx_size = spr_data[tmx_size:tmx_size+2].encode("hex")
			tmx_size = int(tmx_size, 16)
			tmx_data = spr_data[pos-8:pos+tmx_size]
			tmxWriter = open("extracted.tmx", "wb")
			tmxWriter.write(tmx_data)
			tmxWriter.close()
			raw_input("Finished! Press enter to exit. ")
			exit(0)
else:
	print("Error. Unknown input! ")
	exit(0)
