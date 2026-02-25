ASCII_COLORS = dict(
    white = "\x1b[37m",
    grey = "\x1b[38;5;247m",
    yellow = "\x1b[38;5;11m",
    bold_white = "\x1b[37;1m",
    bold_red = "\x1b[31;1m",
    reset = "\x1b[0m",
)


"""
IBM Design Language colors as simple Python constants and a flat dict.

Source: IBM Design Language – Color (Specifications section).[page:1]
"""

IBM_COLORS = {
    # Black and white
    "black": "#000000",
    "white": "#ffffff",

    # Red
    "red_100": "#2d0709",
    "red_90": "#520408",
    "red_80": "#750e13",
    "red_70": "#a2191f",
    "red_60": "#da1e28",
    "red_50": "#fa4d56",
    "red_40": "#ff8389",
    "red_30": "#ffb3b8",
    "red_20": "#ffd7d9",
    "red_10": "#fff1f1",

    # Magenta
    "magenta_100": "#2a0a18",
    "magenta_90": "#510224",
    "magenta_80": "#740937",
    "magenta_70": "#9f1853",
    "magenta_60": "#d02670",
    "magenta_50": "#ee5396",
    "magenta_40": "#ff7eb6",
    "magenta_30": "#ffafd2",
    "magenta_20": "#ffd6e8",
    "magenta_10": "#fff0f7",

    # Purple
    "purple_100": "#1c0f30",
    "purple_90": "#31135e",
    "purple_80": "#491d8b",
    "purple_70": "#6929c4",
    "purple_60": "#8a3ffc",
    "purple_50": "#a56eff",
    "purple_40": "#be95ff",
    "purple_30": "#d4bbff",
    "purple_20": "#e8daff",
    "purple_10": "#f6f2ff",

    # Blue
    "blue_100": "#001141",
    "blue_90": "#001d6c",
    "blue_80": "#002d9c",
    "blue_70": "#0043ce",
    "blue_60": "#0f62fe",
    "blue_50": "#4589ff",
    "blue_40": "#78a9ff",
    "blue_30": "#a6c8ff",
    "blue_20": "#d0e2ff",
    "blue_10": "#edf5ff",

    # Cyan
    "cyan_100": "#001627",
    "cyan_90": "#012749",
    "cyan_80": "#003a6d",
    "cyan_70": "#00539a",
    "cyan_60": "#0072c3",
    "cyan_50": "#1192e8",
    "cyan_40": "#33b1ff",
    "cyan_30": "#82cfff",
    "cyan_20": "#bae6ff",
    "cyan_10": "#e5f6ff",

    # Teal
    "teal_100": "#001a1c",
    "teal_90": "#022b30",
    "teal_80": "#004144",
       "teal_70": "#005d5d",
    "teal_60": "#007d79",
    "teal_50": "#009d9a",
    "teal_40": "#08bdba",
    "teal_30": "#3ddbd9",
    "teal_20": "#9ef0f0",
    "teal_10": "#d9fbfb",

    # Green
    "green_100": "#071908",
    "green_90": "#022d0d",
    "green_80": "#044317",
    "green_70": "#0e6027",
    "green_60": "#198038",
    "green_50": "#24a148",
    "green_40": "#42be65",
    "green_30": "#6fdc8c",
    "green_20": "#a7f0ba",
    "green_10": "#defbe6",

    # Cool gray
    "cool_gray_100": "#121619",
    "cool_gray_90": "#21272a",
    "cool_gray_80": "#343a3f",
    "cool_gray_70": "#4d5358",
    "cool_gray_60": "#697077",
    "cool_gray_50": "#878d96",
    "cool_gray_40": "#a2a9b0",
    "cool_gray_30": "#c1c7cd",
    "cool_gray_20": "#dde1e6",
    "cool_gray_10": "#f2f4f8",

    # Gray
    "gray_100": "#161616",
    "gray_90": "#262626",
    "gray_80": "#393939",
    "gray_70": "#525252",
    "gray_60": "#6f6f6f",
    "gray_50": "#8d8d8d",
    "gray_40": "#a8a8a8",
    "gray_30": "#c6c6c6",
    "gray_20": "#e0e0e0",
    "gray_10": "#f4f4f4",

    # Warm gray
    "warm_gray_100": "#171414",
    "warm_gray_90": "#272525",
    "warm_gray_80": "#3c3838",
    "warm_gray_70": "#565151",
    "warm_gray_60": "#726e6e",
    "warm_gray_50": "#8f8b8b",
    "warm_gray_40": "#ada8a8",
    "warm_gray_30": "#cac5c4",
    "warm_gray_20": "#e5e0df",
    "warm_gray_10": "#f7f3f2",
}

# Convenience: also expose families grouped
IBM_COLOR_FAMILIES = {
    "red": {k.split("_")[1]: v for k, v in IBM_COLORS.items() if k.startswith("red_")},
    "magenta": {k.split("_")[1]: v for k, v in IBM_COLORS.items() if k.startswith("magenta_")},
    "purple": {k.split("_")[1]: v for k, v in IBM_COLORS.items() if k.startswith("purple_")},
    "blue": {k.split("_")[1]: v for k, v in IBM_COLORS.items() if k.startswith("blue_")},
    "cyan": {k.split("_")[1]: v for k, v in IBM_COLORS.items() if k.startswith("cyan_")},
    "teal": {k.split("_")[1]: v for k, v in IBM_COLORS.items() if k.startswith("teal_")},
    "green": {k.split("_")[1]: v for k, v in IBM_COLORS.items() if k.startswith("green_")},
    "cool_gray": {k.split("_")[2]: v for k, v in IBM_COLORS.items() if k.startswith("cool_gray_")},
    "gray": {k.split("_")[1]: v for k, v in IBM_COLORS.items() if k.startswith("gray_")},
    "warm_gray": {k.split("_")[2]: v for k, v in IBM_COLORS.items() if k.startswith("warm_gray_")},
    "core": {"black": IBM_COLORS["black"], "white": IBM_COLORS["white"]},
}

