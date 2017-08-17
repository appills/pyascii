import PIL
from PIL import Image

#now that i've hacked together something with tkinter for a GUI, I can re-do some of this
#needs to be ported to 3.x though...
im = Image.open("santa-800.jpg")
px = im.load()

#this should be something I can pull from image data
width = 800
height = 600

mapped_chars =  ' .:-=+*#%@'
mapped_chars = list(mapped_chars)

print(len(mapped_chars))

gcd = 255.0000
list_C_Linear = []
list_Round_C_Linear = []

for y in range(0, height):
	for x in range(0, width):
		px1 = px[x,y]
		R_avg = (float(px1[0]))/gcd
		G_avg =  (float(px1[1]))/gcd
		B_avg = (float(px1[2]))/gcd
		C_Linear = 0.2126*(R_avg) + 0.7152*G_avg + 0.0722*B_avg
		
		#change moveDecimal to get different "light" -> 10 = dark, 100 = lighter, 1000 = i can't see your face
		moveDecimal = 100
		
		Rounded_C_Linear = round(C_Linear*moveDecimal)
		
		#this makes gray
		px[x,y]=(int(Rounded_C_Linear), int(Rounded_C_Linear), int(Rounded_C_Linear))
		
		list_Round_C_Linear.append(int(Rounded_C_Linear))

with open("final.txt", 'w') as f1:
		
	for i in range(0, len(list_Round_C_Linear)):
			if i%(width) == 0:
				f1.write('\n')
			else:
				if(list_Round_C_Linear[i] < 10):
					f1.write(mapped_chars[0])
				if(list_Round_C_Linear[i] >= 10 and list_Round_C_Linear[i] < 20):
					f1.write(mapped_chars[1])
				if(list_Round_C_Linear[i] >= 20 and list_Round_C_Linear[i] < 30):
					f1.write(mapped_chars[2])
				if(list_Round_C_Linear[i] >= 30 and list_Round_C_Linear[i] < 40):
					f1.write(mapped_chars[3])
				if(list_Round_C_Linear[i] >= 40 and list_Round_C_Linear[i] < 50):
					f1.write(mapped_chars[4])
				if(list_Round_C_Linear[i] >= 50 and list_Round_C_Linear[i] < 60):
					f1.write(mapped_chars[5])
				if(list_Round_C_Linear[i] >= 60 and list_Round_C_Linear[i] < 70):
					f1.write(mapped_chars[6])
				if(list_Round_C_Linear[i] >= 70 and list_Round_C_Linear[i] < 80):
					f1.write(mapped_chars[7])
				if(list_Round_C_Linear[i] >= 80 and list_Round_C_Linear[i] < 90):
					f1.write(mapped_chars[8])
				if(list_Round_C_Linear[i] >= 90 and list_Round_C_Linear[i] < 100):
					f1.write(mapped_chars[9])

		
im.show()

		
		
