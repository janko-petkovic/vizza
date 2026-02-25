"""
IBM Design Language color palettes / colormaps.

Palettes are simple ordered lists of hex strings suitable for use in plotting
libraries (matplotlib, seaborn, etc.).

Source: IBM Design Language – Color (Specifications and Color in UI sections).[page:1]
"""

from vizza.colors._color_data import IBM_COLORS

# Helper to build a sequential family colormap from 10→100
def _family_scale(family: str):
    grades = ["10", "20", "30", "40", "50", "60", "70", "80", "90", "100"]
    return [IBM_COLORS[f"{family}_{g}"] for g in grades]


IBMCOLORMAPS = {
    # Single-hue sequential scales
    "red": _family_scale("red"),
    "magenta": _family_scale("magenta"),
    "purple": _family_scale("purple"),
    "blue": _family_scale("blue"),
    "cyan": _family_scale("cyan"),
    "teal": _family_scale("teal"),
    "green": _family_scale("green"),
    "gray": _family_scale("gray"),
    "cool_gray": _family_scale("cool_gray"),
    "warm_gray": _family_scale("warm_gray"),

    # Core UI neutrals: from white to gray 100.[page:1]
    "ui_neutral": [
        IBM_COLORS["white"],
        IBM_COLORS["gray_10"],
        IBM_COLORS["gray_20"],
        IBM_COLORS["gray_30"],
        IBM_COLORS["gray_40"],
        IBM_COLORS["gray_50"],
        IBM_COLORS["gray_60"],
        IBM_COLORS["gray_70"],
        IBM_COLORS["gray_80"],
        IBM_COLORS["gray_90"],
        IBM_COLORS["gray_100"],
        IBM_COLORS["black"],
    ],

    # Core blue accent scale used across IBM products.[page:1]
    "core_blue": _family_scale("blue"),

    # Example 4-color “families” including core blue.[page:1]
    # These follow the idea of mixing within families at mid grades for gradients.
    "family_cool": [
        IBM_COLORS["blue_50"],
        IBM_COLORS["cyan_50"],
        IBM_COLORS["teal_50"],
        IBM_COLORS["green_50"],
    ],
    "family_warm": [
        IBM_COLORS["blue_50"],
        IBM_COLORS["purple_50"],
        IBM_COLORS["magenta_50"],
        IBM_COLORS["red_50"],
    ],

    # Data-viz friendly diverging-ish sets around blue.[page:1]
    "diverging_blue_red": [
        IBM_COLORS["red_70"],
        IBM_COLORS["red_40"],
        IBM_COLORS["blue_20"],
        IBM_COLORS["blue_50"],
        IBM_COLORS["blue_80"],
    ],
    "diverging_green_magenta": [
        IBM_COLORS["green_70"],
        IBM_COLORS["green_40"],
        IBM_COLORS["blue_20"],
        IBM_COLORS["magenta_40"],
        IBM_COLORS["magenta_70"],
    ],
}

# Convenience: direct accessors for matplotlib-style usage
def get_colormap(name: str):
    """
    Return the list of hex colors for the given colormap name.

    Example:
        from ibm_colormaps import get_colormap
        cmap = get_colormap("core_blue")
    """
    return IBMCOLORMAPS[name]

