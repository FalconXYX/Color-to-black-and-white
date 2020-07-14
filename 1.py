import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import time
from statistics import *
dotimage = np.array(Image.open('images/dot.png'))
dotarray = np.asarray(dotimage)
dotdotimage = Image.open('images/dotdot.png')
dotdotarray = np.asarray(dotdotimage)
yellow4array = np.array(Image.open('images/numbers/y0.4.png'))
apple = np.array(Image.open('images/numbers/apple.jpg'))
z1image = Image.open('images/numbers/0.1.png')
z1array = np.asarray(z1image)


def threshold(inputarray):
    balancearray = []#output array
    newarray = inputarray
    for eachrow in inputarray:
        for eachpixel in eachrow:
            avgNum = mean(eachpixel[:3])
            balancearray.append(avgNum)
    balance = mean(balancearray )
    for eachRow in newarray:
        for eachpixel in eachRow:
            if mean(eachpixel[:3]) > balance:

                eachpixel[0] = 255
                eachpixel[1] = 255
                eachpixel[2] = 255

            else:
                eachpixel.setflags(write=1)
                eachpixel[0] = 0
                eachpixel[1] = 0
                eachpixel[2] = 0


    return newarray
plt.imshow(apple)
plt.show()
yellow4arraybl = threshold(apple)
plt.imshow(yellow4arraybl)
plt.show()
