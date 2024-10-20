from PIL import Image

im = Image.open("AloeVera.jpg")
'''
im2 = im.getchannel('R')
im2.show()
im2 = im.getchannel('G')
im2.show()
im2 = im.getchannel('B')
im2.show()
'''
'''
im3 = im.convert(mode='HSV')
im2 = im3.getchannel('H')
im2.show()
im2 = im3.getchannel('S')
im2.show()
im2 = im3.getchannel('V')
im2.show()
'''
im5 = im.convert(mode='LAB')
im2 = im5.getchannel('L')
im2.show()
im2 = im5.getchannel('A')
im2.show()
im2 = im5.getchannel('B')
im2.show()