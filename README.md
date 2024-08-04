---PSF_FOV_Simulator Readme---

Python program to simulate a basic microscopy image of emitters on a field of view (FOV). The emitters are assumed to have a gaussian point-spread-function (PSF). 

The size of the FOV, emitter amount, magnification (sigma) and the intensity amplitude of the emitters can be specified. The script can simulate single FOV images or stacks of a specified frame number with random intensity fluctuations. For stack simulations, a "burst" mode can be specified, where random bursts will appear in the signal of the emitters.

IMPORTANT: To save the simulated images, please specify your path of choice in the fovfuncs.py file!

Required Python packages: 
matplotlib
numpy
skimage
