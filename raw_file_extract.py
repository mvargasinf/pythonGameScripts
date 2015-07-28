import os

firstLocation = 0
pos = 0
number = 0
done = False
end_raw = "07007777777777777777777777777777".decode("hex")

raw_file = raw_input("What file do you want to extract raw files from? ")
foldName = os.path.splitext(raw_file)[0]
if not os.path.exists(foldName):
    os.mkdir(foldName)
data = open(raw_file, "rb").read()

while not done:
    number += 1
    files = foldName + "/" + foldName + "_" + str(number) + ".raw"
    firstLocation = data.find(end_raw, firstLocation + 1)
    raw_writer = open(files, "wb")
    raw_writer.write(data[pos:firstLocation + 0x10])
    raw_writer.close()
    written_data = open(files, "rb").read()
    if len(written_data) < 0:
        done = True
    pos = firstLocation + 0x10
print "done1"
