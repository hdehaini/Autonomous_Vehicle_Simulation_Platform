import pybullet as p
import pybullet_data

def load_object(urdf_path, position, orientation=[0, 0, 0, 1]):
    """Load an object into the simulation environment."""
    obj_id = p.loadURDF(urdf_path, position, p.getQuaternionFromEuler(orientation))
    return obj_id

def init_environment():
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.setGravity(0, 0, -10)
    planeId = p.loadURDF("plane.urdf")
    
    # Load walls
    wall_positions = [[2, 0, 1], [-3, 0, 1], [0, 3, 1], [0, -3, 1]]  # Example positions
    for pos in wall_positions:
        load_object("../urdf/wall.urdf", pos, [0, 0, 0])
    
    # Load lanes
    lane_positions = [[0, 0, 0.01]]  # Example position
    for pos in lane_positions:
        load_object("../urdf/lane.urdf", pos, [0, 0, 90])  # Rotated 90 degrees on Z-axis if needed

# Ensure you call `init_environment()` in your main simulation loop
