#!/bin/bash

source /opt/ros/noetic/setup.bash
pwd
roscore &
sleep 5
cd src
python3 -m logger.logger_node &
python3 -m listener.listener_node &

# Wait for any process to exit
wait -n

exit $?