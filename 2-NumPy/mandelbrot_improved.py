import matplotlib.pyplot as plt
import numpy as np
import time

width = 1000
height = 1000

image = np.zeros((height,width))

def showRegion(acorn,bcorn,size,image):
    for j in range(1000):
        for k in range(1000):
            count = 0
            ca= acorn + j*size/width
            cb = bcorn + k*size/height
            zx=0
            zy=0

            while count < 100 and (zx**2 + zy**2) <4:
                count +=1
                xtemp = zx**2 - zy**2
                zy = 2*zx*zy +cb
                zx= xtemp + ca
                image[k,j] = count
start_time = time.time()


# acorn = -2
# bcorn= -1.5
# size = 3
#Seahorse valley
acorn = -0.75
bcorn = 0.1
size = 0.02
showRegion(acorn,bcorn,size,image)
end_time = time.time()
print(end_time-start_time)
plt.imshow(image,origin='lower',cmap='magma')
plt.show()
# while True:
#     showRegion(acorn,bcorn,size)
#     plt.imshow(image,origin='lower')
#     plt.show()
#     pts = plt.ginput(1)
#     plt.close()
#     image = np.zeros((height,width))
#     if not pts:
#         break
#     x,y = pts[0]
#     size/=2
#     acorn = x-size/2
#     bcorn = y-size/2

