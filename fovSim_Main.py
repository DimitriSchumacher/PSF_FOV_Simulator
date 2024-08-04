import fovfuncs as ff
from matplotlib import pyplot as plt

fov = ff.fov_generator(fov_shape=(512, 512), emitter_amt=10, sigma=50, amp=100, save=True)

stack = ff.blinkingStack(fov_shape=(512, 512), frames=25, emitter_amt=10, sigma=50, amp=100, burst=False, save=True)

print("Finished")