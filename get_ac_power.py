#!/usr/bin/python3
# Requires use of Python3 API from https://github.com/markperdue/pyvesync
# Simply prints the power level of AC unit to stdout if it can find it, and returns 0
# Otherwise it prints an error to stderr and returns 1
import sys

from pyvesync import VeSync

# Log in
manager = VeSync("darthveder19@gmail.com", "MunOrBust17")
if manager.login() == False:
   sys.stderr.write("Failed to log in to VeSync API!")
   sys.exit(1)

# Get energy usage data
manager.update()
manager.update_energy()

# Make sure we're looking at the right switch
ac_outlet = manager.outlets[4]
name = str(ac_outlet).split(",")[0].split(":")[1].strip()
if name != "Chill Mode":
    sys.stderr.write("Got unexpected outlet name '%s'! Expected 'Chill Mode'" % ac_outlet.config.name)
    sys.exit(1)

# Get power value and print it
print("%.2f" % ac_outlet.power)

# indicate sucess
sys.exit(0)
