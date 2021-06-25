import numpy as np


def masgen():
    x = np.array([20, 31, 42, 52])
    print(x)
    print(np.min(x))
    print(np.max(x))
    print(x)
    imin, imax=np.argmin(x), np.argmax(x)
    vmin, vmax=np.min(x), np.max(x)
    x.flat[imin], x.flat[imax]=vmax, vmin
    print(x)


if __name__ == '__main__':
    print(masgen())
