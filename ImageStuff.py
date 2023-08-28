import PIL.Image

ASCII_CHARS = ["@", "#", "＄", "%", "?", "*", "+", ";", ":", ",", "."]

def ImageToASCII(path):
    img = PIL.Image.open(path)

    # resize the image
    width, height = img.size
    aspect_ratio = height/width
    new_width = 90
    new_height = aspect_ratio * new_width * 0.4
    img = img.resize((new_width, int(new_height)))
    # new size of image
    # print(img.size)

    # convert image to greyscale format
    img = img.convert('L')

    pixels = img.getdata()

    # replace each pixel with a character from array
    chars = ["B","S","#","&","@","$","%","*","!",":","."]
    new_pixels = [chars[pixel//25] for pixel in pixels]
    new_pixels = ''.join(new_pixels)

    # split string of chars into multiple strings of length equal to new width and create a list
    new_pixels_count = len(new_pixels)
    ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
    ascii_image = "\n".join(ascii_image)
    print(ascii_image)

    # write to a text file.
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)


# def imageToASCII(path):
#     try:
#         image = PIL.Image.open(path)
#     except:
#         print(path, "Unable to find image ")
#         return
#     #resize image
#     image = resize(image)
#     #convert image to greyscale image
#     greyscale_image = to_greyscale(image)
#     # convert greyscale image to ascii characters
#     ascii_str = pixel_to_ascii(greyscale_image)
#     img_width = greyscale_image.width
#     ascii_str_len = len(ascii_str)
#     ascii_img=""
#     #Split the string based on width  of the image
#     for i in range(0, ascii_str_len, img_width):
#         ascii_img += ascii_str[i:i+img_width] + "\n"
#     #save the string to a file
#     with open("ascii_image.txt", "w") as f:
#         f.write(ascii_img)
        
# def resize(image, new_width = 100):
#     old_width, old_height = image.size
#     new_height = new_width * old_height / old_width
#     return image.resize((new_width, new_height))

# def to_greyscale(image):
#     return image.convert("L")

# def pixel_to_ascii(image):
#     pixels = image.getdata()
#     ascii_str = ""
#     for pixel in pixels:
#         ascii_str += ASCII_CHARS[pixel//25]
#     return ascii_str
