uint8 MODE_IDLE=0
uint8 MODE_MOVING=1
uint8 MODE_ERROR=2

string robot_name
geometry_msgs/Pose target_pose
float64 speed
bool enable
float64[6] joint_angles
uint8 mode