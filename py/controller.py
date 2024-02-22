import pybullet as p

def avoid_obstacles(carId, lidarData):
    """Enhanced obstacle avoidance logic."""
    threshold = 1.5  # Distance to react to obstacles
    safe_distance = min(lidarData)
    
    if safe_distance < threshold:
        # Obstacle detected within threshold distance
        obstacle_index = lidarData.index(safe_distance)
        num_rays = len(lidarData)
        turn_intensity = (obstacle_index - (num_rays / 2)) / (num_rays / 2)
        turn_direction = -1 if turn_intensity > 0 else 1  # Determine turn direction
        turn_magnitude = min(abs(turn_intensity), 1)  # Ensure turn magnitude is between 0 and 1
        steering_angle = turn_direction * turn_magnitude * 0.3  # Adjust steering based on obstacle position
    else:
        # No obstacle detected within threshold distance, move forward
        steering_angle = 0

    # Apply steering and move forward
    p.setJointMotorControl2(carId, 0, p.POSITION_CONTROL, targetPosition=steering_angle)
    p.setJointMotorControl2(carId, 2, p.VELOCITY_CONTROL, targetVelocity=10)  # Adjust speed as needed
    p.setJointMotorControl2(carId, 3, p.VELOCITY_CONTROL, targetVelocity=10)
