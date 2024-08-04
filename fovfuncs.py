import numpy as np
import skimage as ski

def gaussian(shape, position, amplitude, sigma):

    x = np.linspace(0, shape[1], shape[1])
    y = np.linspace(0, shape[0], shape[0])

    Xs, Ys = np.meshgrid(x,y)

    return amplitude*np.exp(-((position[0]-Xs)**2/sigma+(position[1]-Ys)**2/sigma))

def fov_generator(fov_shape, emitter_amt, sigma, amp, save):

    fov = np.zeros(fov_shape)

    for i in range(emitter_amt):

        pos = (np.random.randint(low=0, high=fov_shape[0]), np.random.randint(low=0, high=fov_shape[1]))

        fov += gaussian(fov_shape, pos, amp, sigma)

    if save == True: 

        ski.io.imsave("HERE_GOES_YOUR_PATH/Simulated_FOV.tif", fov)

    return fov

def blinkingStack(fov_shape, frames, emitter_amt, sigma, amp, burst, save):

    stack = np.zeros((frames, fov_shape[0], fov_shape[1]))

    for i in range(emitter_amt):

        print("Simulating Emitter: " + str(i))
        
        pos = (np.random.randint(low=0, high=fov_shape[0]), np.random.randint(low=0, high=fov_shape[1]))

        for i2 in range(len(stack)):

            print("Simulating Frame: " + str(i2))

            new_amp = np.random.randint(low=0, high=amp)

            if burst == True: 

                if np.random.randint(low=0, high=30) > 28:

                    new_amp += amp*100

                    print("bursting!!!!")

            stack[i2] += gaussian(fov_shape, pos, new_amp, sigma)
    
    if save == True: 

        ski.io.imsave("HERE_GOES_YOUR_PATH/Simulated_Stack.tif", stack)

    return stack