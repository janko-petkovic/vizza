"""
IBM Design Language colormaps for matplotlib/seaborn.

Requires: matplotlib, ibm_colormaps

Usage:
    import matplotlib.pyplot as plt
    from ibm_matplotlib_cmaps import IBMCOLORMAPS

    plt.cm.register_cmap(name="ibm_blue", cmap=IBMCOLORMAPS["blue"])
    plt.imshow(data, cmap="ibm_blue")  # Now works!
"""

import matplotlib.colors as mcolors
from vizza.colors.ibm_colormaps import IBMCOLORMAPS

# Register all as named colormaps (use plt.cm.get_cmap("ibm_red"))
IBMCOLORMAPS = {}
for name, hexes in IBMCOLORMAPS.items():
    cmap = mcolors.ListedColormap(hexes)
    IBMCOLORMAPS[name] = cmap
    # Auto-register prefixed names for easy access
    mcolors.ListedColormap.colors.register(name=f"ibm_{name}", cmap=cmap)

# Convenience dict for quick lookup without registration
# IBMCOLORMAPS["blue"] → ListedColormap object

# Example: all family sequential scales
FAMILY_CMAPS = {
    k: IBMCOLORMAPS[k] for k in ["red", "magenta", "purple", "blue", "cyan", "teal", "green"]
}

