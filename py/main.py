from environment import init_environment
from vehicle_model import load_vehicle
from sensors import simulate_lidar
from controller import avoid_obstacles
import pybullet as p
import time

def run_simulation():
    init_environment()
    carStartPos = [0, 0, 0.1]
    carStartOrientation = p.getQuaternionFromEuler([0, 0, 0])
    carId = load_vehicle(carStartPos, carStartOrientation)
    
    while True:
        lidarData = simulate_lidar(carId)
        avoid_obstacles(carId, lidarData)
        p.stepSimulation()
        time.sleep(1./240.)

if __name__ == "__main__":
    run_simulation()
