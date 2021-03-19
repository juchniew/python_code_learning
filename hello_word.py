import matplotlib.pyplot as plt
import numpy as np

freq = 2e6
t_symbol = 1e-6
n_symbols = 2
sampling_rate = 1e8

n_samples = sampling_rate * t_symbol * n_symbols
dt = 1/sampling_rate
t = np.linspace(0, dt * (n_samples - 1), n_samples)
y = np.sin(2 * np.pi * freq * t )

plt.plot(t, y)
plt.show()
