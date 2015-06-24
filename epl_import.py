# experimental EPL importer
# for usage with TGE's EPL extraction script
import struct, binascii

# file opening and reading
eplArch = raw_input("Name of the orignal EPL archive? ")
eplData = open(eplArch, "rb").read()
impArch = raw_input("Name of the file being imported to the EPL? ")
impData = open(impArch, "rb").read()

# size calculations
impSize = len(impData)
newSize = str(struct.pack("<i", impSize)).encode("hex")
importPos = eplData.find(impData[0:80])
importReplaceSize = importPos - 172

# writing files and new sizes
eplWriter = open("output.epl", "wb")
eplWriter.write(eplData)
eplWriter.seek(importPos)
eplWriter.write(impData)
eplWriter.seek(importReplaceSize)
eplWriter.write(binascii.a2b_hex(newSize))
eplWriter.close()

# finished process
raw_input("Process is done!, press enter to continue. ")
exit(0)