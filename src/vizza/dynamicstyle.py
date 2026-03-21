def get_rcParams(
    figsize : tuple[float, float],
    caption_fontsize : float,
    scale : float = 3.5/5,
    usetex : bool = False
) -> dict[str, float | str | bool] :
    """
    Generate a dictionary of Matplotlib rcParams for consistent figure styling.

    The parameters are scaled based on the figure size and a base caption
    font size. This allows line widths, marker sizes, and font sizes to
    scale proportionally across figures of different sizes.

    Parameters
    ----------
    figsize : tuple of float
        Figure size (width, height) in inches.

    caption_fontsize : float
        Base font size used for axis labels and titles.
        It is called caption_fontsize, because it is good practice to use the same fontsize for axis labels and caption of the figure.

    scale : float, optional
        Scaling factor applied to line widths and marker sizes.
        Default is 2 (for figure of 5x5 inches use a linewidth of 10 pts).

    usetex : bool, optional
        Whether to render text using LaTeX. Default is False.
        It looks elegant, but it slows down a lot making the figure.

    Returns
    -------
    dict
        Dictionary containing rcParams configuration values that can be
        passed to ``matplotlib.rcParams.update()``.
    """

    BFS = caption_fontsize # base fontsize
    BLW = max(*figsize)*scale # base linewidth

    conf = {}

    conf['text.usetex'] = usetex

    ### TEXT ###
    conf['font.family'] = 'sans-serif'
    conf['font.sans-serif'] = 'Arial'
    conf['mathtext.fontset'] = 'dejavusans'

    conf['axes.labelsize'] = BFS
    conf['legend.fontsize'] = BFS*0.9
    conf['xtick.labelsize'] = BFS*0.8
    conf['ytick.labelsize'] = BFS*0.8

    conf['axes.titlesize'] = BFS
    conf['axes.titleweight'] = 1

    ### LINES ###
    conf['lines.linewidth'] = BLW # not in inches, but in POINTS (1/72 inches)
    conf['lines.markersize'] = BLW*2
    conf['axes.linewidth'] = BLW*0.2
    conf['grid.linewidth'] = BLW*0.5

    conf['xtick.major.size'] = BLW*1.5
    conf['xtick.major.width'] = BLW*0.25
    conf['xtick.minor.size'] = BLW*1.5/2
    conf['xtick.minor.width'] = BLW*0.25

    conf['ytick.major.size'] = BLW*1.5
    conf['ytick.major.width'] = BLW*0.25
    conf['ytick.minor.size'] = BLW*1.5/2
    conf['ytick.minor.width'] = BLW*0.25


    ### DESIGN ###
    conf['xtick.direction'] = 'in'
    conf['ytick.direction'] = 'in'
    conf['ytick.minor.visible'] = True
    conf['xtick.minor.visible'] = True

    conf['legend.frameon'] = 'False' # legend frame is ugly

    return conf
