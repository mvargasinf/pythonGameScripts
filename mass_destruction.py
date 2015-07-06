import glob, os


def main(name):
        global number
        global firstLocation
        number = 0
        firstLocation = 0
        while spr_tmx_count > number:
                        number = number + 1
                        firstLocation = spr_data.find("TMX0", firstLocation + 1)
                        read_size = firstLocation - 4
                        read_size = spr_data[read_size : read_size + 4].encode("hex")
                        read_size = int(read_size, 16)
                        tmx_data = firstLocation - 8

                        tmx_data = spr_data[tmx_data:firstLocation + read_size]
                        tmxWriter = open(name + "/" + str(number) + ".tmx", "wb")
                        tmxWriter.write(tmx_data)
                        tmxWriter.close()
                        if spr_tmx_count == number:
                                number = 0
                                firstLocation = 0
                                break
                
for files in glob.glob("*.SPR"):
        foldName = os.path.splitext(files)[0]
        os.mkdir(foldName)
        spr_data = open(files, "rb").read()
        spr_tmx_count = spr_data.count("TMX0")
        main(foldName)
