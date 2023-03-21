from stegano import lsb
from stegano import exifHeader
from steganocryptopy.steganography import Steganography

def hide_png():
    secret = lsb.hide("img.png", "You password: 1234")
    secret.save("img_secret.png")

def show_png():
    result = lsb.reveal("img_secret.png")
    print(result)


def hide_jpg():
    secret = exifHeader.hide("img.jpg", "img_secret2.jpg","Your pass: 0000")

def show_jpg():
    result = exifHeader.reveal("img_secret2.jpg")
    result = result.decode()
    print(result)



def hide_key():
    #Steganography.generate_key("")    #if you dont have file key.key uncoment this string
    secret = Steganography.encrypt("key.key", "img.png", "text")
    secret.save("img_secret3.png")

def show_key():
    result = Steganography.decrypt("key.key", "img_secret3.png")
    print(result)



