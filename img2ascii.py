import PIL.Image

ASCII_CHARS = ["@","#","S","%","?","*", "+", ";", ":",",","."]

#resizing image
def resize_image(image, new_width = 300):
	width, height = image.size
	ratio = height/width
	new_height = int(new_width * ratio)
	resize_image = image.resize((new_width, new_height))
	return(resize_image)
	
	#converting image to grayscale
def grayify(image):
	grayscale_image = image.convert("L")
	return(grayscale_image)
	
	#converting pixels to ascii
def pixels_to_ascii(image):
	pixels = image.getdata()
	characters = "".join([ASCII_CHARS[pixel//25]for pixel in pixels])
	return(characters)	
def main(new_width=300):
	path = input("YOUR PATH> ")
	try:
		image = PIL.Image.open(path)
		
	except:
		print("UNABLE TO FIND IMAGE!")
	
	#converting image to ascii
	new_image_data = pixels_to_ascii(grayify(resize_image(image,new_width)))

	#format 
	pixel_count = len(new_image_data)
	ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))
	print(ascii_image)

	with open("ascii_image.txt","w") as f:
		f.write(ascii_image)


if __name__ == '__main__':
	main()
