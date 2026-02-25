import matplotlib.pyplot as plt
plt.style.use("vizza.mplstyles.texstyle")
import numpy as np

from vizza.colormaps.ibm import cbf
plt.colormaps.register(name='ibm_cbf', cmap=cbf)
plt.rcParams['image.cmap'] = 'ibm_cbf'


ys = np.random.uniform(size=(10,10))

fig, ax = plt.subplots(1,1)
ax.pcolormesh(ys)
plt.show()



