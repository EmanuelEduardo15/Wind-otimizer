import openfast_toolkit as oft

def run_openfast_simulation(wind_speed, turbine_position):
    config = oft.load_config("turbine_config.yaml")
    config.wind_speed = wind_speed
    config.turbine_position = turbine_position
    result = oft.simulate(config)
    return result.power_output
