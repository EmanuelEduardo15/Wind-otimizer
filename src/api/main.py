from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from .schemas import SimulationRequest

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/simulate")
async def simulate(request: SimulationRequest):
    simulator = WindSimulator(request.grid_size)
    wind_field = simulator.simulate(request.steps, request.noise)
    return {"status": "success", "data": wind_field.tolist()}
