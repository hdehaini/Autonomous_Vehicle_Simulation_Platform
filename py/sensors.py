import pybullet as p
import math

def simulate_lidar(carId, numRays=36, maxDistance=10):
    """Simulate a LIDAR sensor by casting rays in all directions around the car."""
    lidarData = []
    carPos, carOri = p.getBasePositionAndOrientation(carId)
    
    for i in range(numRays):
        angle = (i / numRays) * 2. * math.pi
        # Calculate the rayTo point correctly using sine and cosine for direction
        rayFrom = carPos
        rayTo = [carPos[0] + maxDistance * math.sin(angle), carPos[1] + maxDistance * math.cos(angle), carPos[2]]
        rayResults = p.rayTest(rayFrom, rayTo)[0]
        distance = rayResults[2]
        if distance == 0:
            distance = maxDistance  # No obstacle detected within maxDistance
        lidarData.append(distance)
    return lidarData
