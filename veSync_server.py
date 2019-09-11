#!/usr/bin/python
import datetime
import subprocess
import sys
import time

import db_connect as db

def fetch_AC_power():
    """
    Uses subprocess to call the script to get the AC power levels
    needed since API is python 3 and these are python2. 
    Returns float of power level if successful, otherwise returns False
    """
    p = subprocess.Popen("/home/cesahr/vesync/get_ac_power.py", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()
    stdout, stderr = p.communicate()
    
    if p.returncode != 0:
        print "Got error from VeSync API! '%s'" % stderr
        # TODO: notify someone or something
        return False
    else:
        try:
            rv = float(stdout)
        except ValueError: 
            print "Got bad value from VeSync API! '%s'" % stdout
            # TODO notify or something
    return rv

# Start infinite loop of getting the data about every 4min
print "Starting server to get veSync data about ever ~4min"

while True:
    print "Fetching new data @ ",
    timenow = datetime.datetime.now()
    print timenow, " ... ",
    
    ac_power = fetch_AC_power()
    if ac_power is False:
        # TODO: do something maybe?
        print "Failure from power fetch!"
        print "rv = %s" % ac_power
        time.sleep(240)
        continue
    else:
        print ac_power,
       
    # connect to database
    cnx, cur = db.connect_to_server()

    # current information 
    table = ("INSERT INTO `sensor_data`.`AC_power` "
            "(`reading_time` , `power_level`) "
            "VALUES ('%s', %f)")
    data = (timenow, ac_power)
    result = cur.execute(table % data)
    cnx.commit()

    # close connection
    db.close_connection(cnx,cur)
    
    print "  sleeping for 4m"
    time.sleep(240)

