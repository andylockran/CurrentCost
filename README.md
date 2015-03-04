# CurrentCost

This is a simple python script to upload the output of your EDF Energy Monitor up to opensensors.io.

You'll need to buy the datacable, but once you've plugged into your raspberry pi it's all good to go.

I used sysvinit to make the process respawn by adding the following to the end of my /etc/inittab file:

A1:2345:respawn:/usr/bin/python /home/pi/Code/current.py

