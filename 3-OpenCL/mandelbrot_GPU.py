import pyopencl as cl
import numpy as np
import matplotlib.pyplot as plt
import time

width = 1000
height = 1000

# acorn = -2
# bcorn= -1.5
# size = 3

# acorn = 0.285
# bcorn = 0.01
# size = 0.01

#Elephant valley
# acorn = 0.285
# bcorn = 0.01
# size = 0.01

#Double spiral
# acorn = -0.743643887037151
# bcorn = 0.131825904205330
# size = 0.000014

#Satellite bulbs
# acorn = -1.25066
# bcorn = 0.02012
# size = 0.005

#Seahorse valley
# acorn = -0.75
# bcorn = 0.1
# size = 0.02

#Mini mandelbrot island
# acorn = -1.25066
# bcorn = 0.02012
# size = 0.005

#Valley of the flowers
# acorn = -1.37
# bcorn = 0.015
# size = 0.005

#Seahorse heart
# acorn = -0.74529
# bcorn = 0.113075
# size = 0.0005

#Satellite chain
acorn = -0.75
bcorn = 0.1
size = 0.02





ctx = cl.create_some_context()
queue = cl.CommandQueue(ctx)
image = np.zeros(height*width,dtype=np.float32 )
image_buf = cl.Buffer(ctx, cl.mem_flags.WRITE_ONLY, image.nbytes)
with open("mandelbrot.cl") as f:
    kernel_source = f.read()
program = cl.Program(ctx, kernel_source).build()

program.calc_pixel(
    queue,
    (width,height),
    None,
    image_buf,
    np.float32(acorn),
    np.float32(bcorn),
    np.float32(size),
    np.int32(width),
)
cl.enqueue_copy(queue, image, image_buf)
queue.finish()
image = image.reshape(height, width)
plt.imshow(image,origin='lower',cmap='cubehelix')
plt.show()
dev = ctx.devices[0]
print("Name:", dev.name)
print("Type:", cl.device_type.to_string(dev.type))   # 'GPU' or 'CPU'
print("Compute units:", dev.max_compute_units)