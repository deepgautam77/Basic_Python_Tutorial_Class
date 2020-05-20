#Generate qrcode using pillow qrcode modules
from PIL import Image, ImageDraw
import qrcode
data = input('Enter what you like to keep in qr code: ')
img = qrcode.make(data)
img.save("First_qrcode.png")