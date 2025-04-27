from pydantic import BaseModel

class SimulationRequest(BaseModel):
    grid_size: int = 512
    steps: int = 100
    noise: float = 0.1
