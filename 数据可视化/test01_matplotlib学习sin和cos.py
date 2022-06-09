import numpy as np
from matplotlib import pyplot as plt

# 画画sin和cos线
x = np.linspace(-np.pi, np.pi, 256)

cos = np.cos(x)
sin = np.sin(x)

plt.plot(x, cos, '--', linewidth=2)
plt.plot(x, sin)

plt.show()
