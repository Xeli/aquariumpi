#! /bin/sh
# AquariumPi

### BEGIN INIT INFO
# Provides: AquariumPi
# Required-Start: $remote_fs $syslog
# Required-Stop: $remote_fs $syslog
# Default-Start: 2 3 4 5
# Default-Stop: 0 1 6
# Short-Description: AquariumPi - monitoring your reefs
### END INIT INFO

AQUARIUM_DIR="/home/pi/aquariumpi"

case $1 in
    start)
        echo "Starting AquariumPi"
        $AQUARIUM_DIR/start
    ;;
esac
