import pybullet as p
import pybullet_data
import time
from environment import init_environment
from vehicle_model import load_vehicle
from sensors import simulate_lidar
from controller import avoid_obstacles

def run_simulation():
    # Initialize PyBullet simulation
    physicsClient = p.connect(p.GUI)  # Connect to PyBullet
    p.setAdditionalSearchPath(pybullet_data.getDataPath())  # For accessing the built-in URDFs
    
    # Set up the environment and the vehicle
    init_environment()  # Load your environment (ground, walls, etc.)

    
    carStartPos = [0, 0, 0.1]  # Starting position of the car
    carStartOrientation = p.getQuaternionFromEuler([0, 0, 0])  # Starting orientation
    carId = load_vehicle(carStartPos, carStartOrientation)  # Load the car model
    
    # Main simulation loop
    for i in range(5000):  # Run for a set number of iterations, or use a condition to run indefinitely
        lidarData = simulate_lidar(carId)  # Get LIDAR data for obstacle detection
        avoid_obstacles(carId, lidarData)  # Use LIDAR data to avoid obstacles
        p.stepSimulation()  # Step the simulation
        time.sleep(1./240.)  # Sleep to simulate real-time; adjust as needed for your simulation speed
        
    p.disconnect()  # Disconnect from the PyBullet server when done

if __name__ == "__main__":
    run_simulation()