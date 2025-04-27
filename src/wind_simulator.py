import cupy as cp
from cupyx.scipy.fft import fft2, ifft2

class WindSimulatorGPU:
    def __init__(self, grid_size=1024):
        self.grid_size = grid_size
        self.wind_field = cp.random.rand(grid_size, grid_size)
    
    def simulate(self, steps=100, noise_intensity=0.1):
        for _ in range(steps):
            noise = cp.fft.fft2(cp.random.randn(self.grid_size, self.grid_size))
            self.wind_field += cp.real(ifft2(noise * noise_intensity))
        return cp.clip(self.wind_field, 0, 1).get()  # Retorna para CPU
