import PIL
from PIL import Image

def getSaveFileName(myFile):
	reversedSplit = myFile.rsplit("/", 1)
	saveDirectory = reversedSplit[0]
	fileName = reversedSplit[1]
	withoutExtension = fileName.rsplit(".", 1)[0]
	return ''.join([saveDirectory, "/", withoutExtension])	

def main(myFile):
	#open the image
	im = Image.open(myFile)
	px = im.load()
	#get the width and height
	width, height = im.size
	mappedChars =  list(' .:-=+*#%@')
	gcd = 255.0000
	list_C_Linear = []
	list_Round_C_Linear = []

	for y in range(0, height):
		for x in range(0, width):
			pxPoint = px[x,y]
			R_avg = (float(pxPoint[0]))/gcd
			G_avg =  (float(pxPoint[1]))/gcd
			B_avg = (float(pxPoint[2]))/gcd
			C_Linear = 0.2126*(R_avg) + 0.7152*G_avg + 0.0722*B_avg
			
			#change moveDecimal to get different "light" -> 10 = dark, 100 = lighter, 1000 = i can't see your face
			moveDecimal = 100
			
			Rounded_C_Linear = round(C_Linear*moveDecimal)
			
			#this makes gray
			px[x,y]=(int(Rounded_C_Linear), int(Rounded_C_Linear), int(Rounded_C_Linear))
			
			list_Round_C_Linear.append(int(Rounded_C_Linear))
	
	saveFileName = ''.join([getSaveFileName(myFile), ".txt"])
	
	with open(saveFileName, 'w') as writeFile:
			
		for i in range(0, len(list_Round_C_Linear)):
				if i%(width) == 0:
					writeFile.write('\n')
				else:
					if(list_Round_C_Linear[i] < 10):
						writeFile.write(mappedChars[0])
					elif(list_Round_C_Linear[i] >= 10 and list_Round_C_Linear[i] < 20):
						writeFile.write(mappedChars[1])
					elif(list_Round_C_Linear[i] >= 20 and list_Round_C_Linear[i] < 30):
						writeFile.write(mappedChars[2])
					elif(list_Round_C_Linear[i] >= 30 and list_Round_C_Linear[i] < 40):
						writeFile.write(mappedChars[3])
					elif(list_Round_C_Linear[i] >= 40 and list_Round_C_Linear[i] < 50):
						writeFile.write(mappedChars[4])
					elif(list_Round_C_Linear[i] >= 50 and list_Round_C_Linear[i] < 60):
						writeFile.write(mappedChars[5])
					elif(list_Round_C_Linear[i] >= 60 and list_Round_C_Linear[i] < 70):
						writeFile.write(mappedChars[6])
					elif(list_Round_C_Linear[i] >= 70 and list_Round_C_Linear[i] < 80):
						writeFile.write(mappedChars[7])
					elif(list_Round_C_Linear[i] >= 80 and list_Round_C_Linear[i] < 90):
						writeFile.write(mappedChars[8])
					elif(list_Round_C_Linear[i] >= 90 and list_Round_C_Linear[i] <= 100):
						writeFile.write(mappedChars[9])