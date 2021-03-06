#!/bin/bash

export BASEDIR="/home/d3/Midem_2015"

echo "Midem hackday 2015"

echo "Running jack..."

/usr/bin/qjackctl -a $BASEDIR/Cannes.xml -s &

sleep 4

echo "Connecting pulseaudio..."

pactl load-module module-jack-sink channels=2
pacmd set-default-sink jack_out

echo "Activating rack FX..."

/usr/bin/jack-rack $BASEDIR/lowpass-kp+ &

echo "Running spotify..."

/usr/bin/spotify > /dev/null &

sleep 2

echo "Running main controller..."

./cannes.py
