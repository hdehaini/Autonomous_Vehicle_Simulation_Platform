import pybullet as p

def load_vehicle(start_position, start_orientation):
    carId = p.loadURDF("racecar/racecar.urdf", start_position, start_orientation)
    return carId
