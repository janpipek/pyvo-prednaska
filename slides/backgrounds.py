from physt import h2, h1
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)


def multicenter_data(xs, ys, counts, radii):
    for x, y, count, radius in zip(xs, ys, counts, radii):
        yield np.random.normal(x, radius, count), np.random.normal(y, radius, count)

def save_only_axis(ax, path, **kwargs):
    extent = ax.get_window_extent().transformed(plt.gcf().dpi_scale_trans.inverted())
    ax.figure.savefig(path, bbox_inches=extent, **kwargs)

def vignette_histogram(path, width=1920, height=1280, grid=32, jitter=1, **kwargs):
    histogram = h2(None, None, "fixed_width", grid, range=((0, width), (0, height)))

    xs = [0, width, width, 0, width / 2]
    ys = [0, 0, height, height, height / 2]
    count = int((height / grid) ** 2 / jitter)
    counts = [count] * 4 + [count / 4]
    radii = [height / 4] * 5

    for xs, ys in multicenter_data(xs, ys, counts, radii):
        fill_data = np.concatenate([xs[:, np.newaxis], ys[:, np.newaxis]], axis=1)
        histogram.fill_n(fill_data)

    dpi = 100
    fig, ax = plt.subplots(figsize=(width / dpi, height / dpi))
    histogram.plot("image", ax=ax, show_colorbar=False, cmap_max=histogram.frequencies.max(), cmap_min=-0.3 * histogram.frequencies.max(), **kwargs)
    ax.set_axis_off()
    save_only_axis(ax, path, dpi=dpi)

def stair_histogram(path, width=1920, height=1280, bar=128, jitter=.1, **kwargs):
    histogram = h1(None, "fixed_width", bar, range=(0, width))
    data = np.random.normal(width, width, int(1000 / jitter))
    histogram.fill_n(data)
    dpi = 100
    fig, ax = plt.subplots(figsize=(width / dpi, height / dpi))
    histogram.plot("fill", ax=ax, color="red", **kwargs)
    ax.set_axis_off()
    save_only_axis(ax, path, dpi=dpi)


if __name__ == "__main__":
    vignette_histogram("background.png", grid=64, alpha=0.4)
    stair_histogram("stairs.png", bar=256, alpha=1, lw=10, edgecolor="red")
