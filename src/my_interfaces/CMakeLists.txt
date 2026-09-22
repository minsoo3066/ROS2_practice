cmake_minimum_required(VERSION 3.8)
project(my_interfaces)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(geometry_msgs REQUIRED)
# Interface 생성 도구 가져오는 부분

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/RobotStatus.msg"
  "msg/RobotCommand.msg"
  "srv/SetTarget.srv"
  "action/MoveRobot.action"

  DEPENDENCIES
  geometry_msgs
)
# 실 .msg파일 생성하라 명령하는 부분

ament_package()