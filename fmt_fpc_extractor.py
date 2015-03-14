import glob, os, binascii

for files in glob.glob('*.fpc'):
	fileOpen, extension = os.path.splitext(files)
	gmoExtractor = open(files, 'rb')
	gmoExtractor.seek(256)
	gmoWriter = open(fileOpen + '.gmo', 'wb')
	gmoWriter.write(gmoExtractor.read())
	gmoWriter.close()
