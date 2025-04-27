# %% [markdown]
# ## 🌪️ Simulação de Turbulência - WindOptimizer
# Gera um GIF da evolução do campo de vento offshore.

# %% [code]
!pip install imageio matplotlib numpy > /dev/null
import numpy as np
import matplotlib.pyplot as plt
import imageio
import os
from IPython.display import Image

# Configuração do ambiente
os.makedirs("/content/temp", exist_ok=True)

# Simulação Fractal
class WindSimulator:
    def __init__(self, grid_size=256):
        self.grid_size = grid_size
        self.wind_field = np.random.rand(grid_size, grid_size)
        
    def simulate(self, steps=10, noise=0.1):
        for _ in range(steps):
            freq_noise = np.fft.fft2(np.random.randn(self.grid_size, self.grid_size))
            self.wind_field += np.real(np.fft.ifft2(freq_noise * noise))
        return np.clip(self.wind_field, 0, 1)

# Criação do GIF
filenames = []
simulator = WindSimulator()

for i in range(30):
    simulator.simulate(steps=5)
    plt.figure(figsize=(6,6))
    plt.imshow(simulator.wind_field, cmap='viridis', vmin=0, vmax=1)
    plt.title(f"Passo {i*5}")
    plt.axis('off')
    filename = f"/content/temp/frame_{i:03d}.png"
    plt.savefig(filename, dpi=100, bbox_inches='tight')
    plt.close()
    filenames.append(filename)

# Combina em GIF
with imageio.get_writer('/content/wind_simulation.gif', mode='I', duration=0.2) as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)

# Mostra resultado
Image(filename='/content/wind_simulation.gif')
