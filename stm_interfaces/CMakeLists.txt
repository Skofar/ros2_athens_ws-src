cmake_minimum_required(VERSION 3.8)
project(stm_interfaces)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()


# find dependencies
find_package(ament_cmake REQUIRED)
find_package(std_msgs REQUIRED)

find_package(rosidl_default_generators REQUIRED)

set(serial_state_file
  "msg/STMState.msg"
)

set(serial_control_file
  "msg/STMControl.msg"
)

set(set_control_type_service
    "srv/STMSetControlType.srv"
)

rosidl_generate_interfaces(${PROJECT_NAME}
  ${serial_state_file}
  ${serial_control_file}
  ${set_control_type_service}
  DEPENDENCIES std_msgs

)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_export_dependencies(rosidl_default_runtime)
ament_package()
