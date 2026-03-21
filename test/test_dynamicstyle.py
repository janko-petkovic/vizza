import random

import matplotlib
import matplotlib.pyplot as plt

from vizza.dynamicstyle import get_rcParams

small_figsize = (5,5)
big_figsize = (10,10)
data = [1 + random.random() for _ in range(100)]

matplotlib.rcParams.update(get_rcParams(small_figsize, caption_fontsize=14))

small_fig, small_ax = plt.subplots(figsize = small_figsize)
small_ax.plot(data, 'o')
small_ax.axhline(1.5, color='tab:red', label='average')
small_ax.set_ylim(0,3)
small_ax.set_xlabel('sample')
small_ax.set_ylabel('value')
small_ax.legend()

matplotlib.rcParams.update(get_rcParams(big_figsize, caption_fontsize=22))
big_fig, big_ax = plt.subplots(figsize = big_figsize)
big_ax.plot(data, 'o')
big_ax.axhline(1.5, color='tab:red', label='average')
big_ax.set_ylim(0,3)
big_ax.set_xlabel('sample')
big_ax.set_ylabel('value')
big_ax.legend()

plt.show()
