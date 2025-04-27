import numpy as np
from scipy.fft import fft2, ifft2

class WindSimulator:
    def __init__(self, grid_size=512):
        self.grid_size = grid_size
        self.wind_field = np.random.rand(grid_size, grid_size)
        
    def simulate(self, steps=100, noise_intensity=0.1):
        for _ in range(steps):
            noise = np.fft.fft2(np.random.randn(self.grid_size, self.grid_size))
            self.wind_field += np.real(ifft2(noise * noise_intensity))
        return np.clip(self.wind_field, 0, 1)
    
    def save_to_csv(self, filename="wind_field.csv"):
        np.savetxt(filename, self.wind_field, delimiter=",")
