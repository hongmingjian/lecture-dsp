import numpy as np
import matplotlib.pyplot as plt

t=np.linspace(-np.pi, np.pi, 100)


fig = plt.figure()

y = 1 - np.exp(-1j*t)

ax = fig.add_subplot(2, 2, 1)
ax.plot(t, np.abs(y))
ax.spines.left.set_position('zero')
ax.spines.right.set_color('none')
ax.spines.bottom.set_position('zero')
ax.spines.top.set_color('none')
ax.set_xlabel(r'$\omega$', loc='right')
ax.set_ylabel(r'$|H(j\omega)|$', loc='top')
ax.set_xticks([-np.pi, 0, np.pi])
ax.set_xticklabels([r'$-\pi$', '0', r'$\pi$'])
ax.set_yticks([])
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_label_coords(1.06, 0.07)

ax = fig.add_subplot(2, 2, 2)
ax.plot(t, np.angle(y))
ax.spines.left.set_position('zero')
ax.spines.right.set_color('none')
ax.spines.bottom.set_position('zero')
ax.spines.top.set_color('none')
ax.set_xlabel(r'$\omega$', loc='right')
ax.set_ylabel(r'$\sphericalangle H(j\omega)$', loc='top')
ax.set_xticks([-np.pi, 0, np.pi])
ax.set_xticklabels([r'$-\pi$', '0', r'$\pi$'])
ax.set_yticks([])
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_label_coords(1.06, 0.53)

M = 5
y=[np.sum([np.exp(-1j*k*_) for k in range(M)]) for _ in t]

ax = fig.add_subplot(2, 2, 3)
ax.plot(t, np.abs(y))
ax.spines.left.set_position('zero')
ax.spines.right.set_color('none')
ax.spines.bottom.set_position('zero')
ax.spines.top.set_color('none')
ax.set_xlabel(r'$\omega$', loc='right')
ax.set_ylabel(r'$|H(j\omega)|$', loc='top')
ax.set_xticks([-np.pi, 0, np.pi])
ax.set_xticklabels([r'$-\pi$', '0', r'$\pi$'])
ax.set_yticks([])
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_label_coords(1.06, 0.07)

ax = fig.add_subplot(2, 2, 4)
ax.plot(t, np.angle(y))
ax.spines.left.set_position('zero')
ax.spines.right.set_color('none')
ax.spines.bottom.set_position('zero')
ax.spines.top.set_color('none')
ax.set_xlabel(r'$\omega$', loc='right')
ax.set_ylabel(r'$\sphericalangle H(j\omega)$', loc='top')
ax.set_xticks([-np.pi, 0, np.pi])
ax.set_xticklabels([r'$-\pi$', '0', r'$\pi$'])
ax.set_yticks([])
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_label_coords(1.06, 0.53)

plt.show()
