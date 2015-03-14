import glob, os
print "PACExtractor - By ThatTrueStruggle"
print "For extracting rmd files from PAC files"
for files in glob.glob('*.pac'):
        # get name here
	fileOpen, extension = os.path.splitext(files)
	# read data
	print fileOpen + " | " + str(os.stat(files).st_size)
	RMDExtract = open(files, 'rb')
	# search for header
	RMDExtract.seek(256)
	# had trouble writing this one
	# had to use wb instead of w
	rmdWriter = open(fileOpen + '.rmd', 'wb')
	# write to a rmd file
	rmdWriter.write(RMDExtract.read())
	rmdWriter.close()
raw_input("Done! press enter to exit!")
# this code can easily be modified to look for any header magic
# like extracting tmx0's from spr files
