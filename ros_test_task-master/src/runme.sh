#!/bin/bash

pwd
./src/logger/logger.py &
./src/listener/listener.py &

# Wait for any process to exit
wait -n

exit $?