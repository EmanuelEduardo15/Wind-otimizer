import pytest
from src.wind_simulator import WindSimulator

def test_simulation():
    simulator = WindSimulator(grid_size=100)
    result = simulator.simulate(steps=10)
    assert result.shape == (100, 100), "Dimensões incorretas"
    assert 0 <= result.min() <= result.max() <= 1, "Valores fora do intervalo"
