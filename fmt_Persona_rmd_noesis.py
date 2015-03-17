#Persona 3/4 RMD Format

from inc_noesis import *
import noesis, rapi 

def registerNoesisTypes():
	handle = noesis.register("Persona 3/4", ".rmd")
	noesis.setHandlerTypeCheck(handle, rmdCheckType)
	noesis.setHandlerLoadModel(handle, rmdLoadModel)
	noesis.logPopup()
    #print("The log can be useful for catching debug prints from preview loads.\nBut don't leave it on when you release your script, or it will probably annoy people.")
	return 1

def rmdCheckType(data):
	bs = NoeBitStream(data)
	# find if first 4 is greater
	if len(data) < 4:
		return 0
	return 1
   
def rmdLoadModel(data, mdlList):
   ctx = rapi.rpgCreateContext()
   bs = NoeBitStream(data)
   rapi.rpgClearBufferBinds()
   bs.seek(0x10, NOESEEK_ABS)
   hdrInfo = bs.read("iii")
   
   for hdr in hdrInfo:
           print(hex(hdr))
   return 1
   
