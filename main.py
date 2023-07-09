from PIL import Image

# Open an image file
with Image.open('image.jpg') as im:
    # Display the image
    im.show()

    # Rotate the image by 45 degrees
    im = im.rotate(45)

    # Resize the image to half its original size
    im = im.resize((im.width // 2, im.height // 2))

    # Save the modified image
    im.save('modified_image.jpg')
