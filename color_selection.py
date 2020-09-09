import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

COLORS = mcolors.CSS4_COLORS
# print(COLORS)
DEFAULT_COLORS = [
    'indianred', 
    'coral',
    'orange',
    'gold',
    'lawngreen',
    'limegreen',
    'mediumturquoise',
    'deepskyblue',
    'royalblue',
    'mediumblue',
    'mediumslateblue',
    'mediumorchid',
    'violet',
    'hotpink',
    'crimson'
]

def show_colors(colors):
    x_size = 10
    fig, ax = plt.subplots(figsize=(x_size, 1))
    ax.yaxis.set_visible(False)
    ax.xaxis.set_visible(False)
    ax.set_axis_off()
    for i, c in enumerate(colors):
        x_start = i * (x_size / len(colors))
        x_end = (i + 1) * (x_size / len(colors))
        ax.hlines(1, x_start, x_end, color=COLORS[c], linewidth=20)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    show_colors(DEFAULT_COLORS)
