import matplotlib.pyplot as plt
plt.style.use("vizza.mplstyles.texstyle")


fig, axs = plt.subplots(2,2)
axs[0, 0].scatter((1,2,3,4),(6,2,6,3), label='Plot 1')
axs[0, 0].scatter((1,2,3,4),(4,4,5,1), label='Plot 2')
axs[0, 1].scatter((1,2,3,4),(6,2,6,3), label='Plot 1')
axs[0, 1].scatter((1,2,3,4),(4,4,5,1), label='Plot 2')
axs[1, 0].scatter((1,2,3,4),(6,2,6,3), label='Plot 1')
axs[1, 0].scatter((1,2,3,4),(4,4,5,1), label='Plot 2')
axs[1, 1].scatter((1,2,3,4),(6,2,6,3), label='Plot 1')
axs[1, 1].scatter((1,2,3,4),(4,4,5,1), label='Plot 2')

for ax in axs.flatten():
    ax.set_xlabel(r'First axis $x$')
    ax.set_ylabel(r'First axis $y$')
    ax.legend()

plt.show()

