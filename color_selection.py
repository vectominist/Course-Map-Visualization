import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

COLORS = mcolors.CSS4_COLORS
DEFAULT_COLORS = [
    'indianred', 
    'coral',
    'orange',
    'gold',
    'lightgreen',
    'limegreen',
    'mediumturquoise',
    'deepskyblue',
    'royalblue',
    'mediumblue',
    'mediumorchid',
    'violet',
    'hotpink',
    'crimson'
]

def get_color(ratio, c_type='default', cmap_type='rainbow'):
    if c_type == 'default':
        return COLORS[DEFAULT_COLORS[int(np.around(ratio * len(DEFAULT_COLORS)))]]
    elif c_type == 'cmap':
        cmap = plt.get_cmap(cmap_type)
        return mcolors.to_hex(cmap(ratio))
    else:
        raise NotImplementedError('Color type {} is invalid.'.format(c_type))

def show_colors(colors):
    x_size = 10
    fig, ax = plt.subplots(figsize=(x_size, 1))
    ax.yaxis.set_visible(False)
    ax.xaxis.set_visible(False)
    ax.set_axis_off()
    for i, c in enumerate(colors):
        x_start = i * (x_size / len(colors))
        x_end = (i + 1) * (x_size / len(colors))
        ax.hlines(1, x_start, x_end, color=COLORS[c], linewidth=50)
    plt.tight_layout()
    plt.show()

def show_color_map(cmap_type):
    x_size = 10
    fig, ax = plt.subplots(figsize=(x_size, 1))
    ax.yaxis.set_visible(False)
    ax.xaxis.set_visible(False)
    ax.set_axis_off()
    grad = np.linspace(0, 1, 256)
    grad = np.vstack((grad, grad))
    ax.imshow(grad, aspect='auto', cmap=plt.get_cmap(cmap_type))
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    show_colors(DEFAULT_COLORS)
    show_color_map('rainbow')
