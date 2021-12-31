#!/usr/bin/env python
"""
Temperature from Temperature.nu for Domoticz
Author: Derenback
"""
"""
<plugin key="TEMPNU" name="Temperature.nu" version="0.0.1" author="Derenback">
    <params>
        <param field="Mode2" label="Location" width="300px" required="true" default="" />
        <param field="Mode4" label="Debug" width="75px">
            <options>
                <option label="On" value="Debug"/>
                <option label="Off" value="Off" default="true" />
            </options>
        </param>
    </params>
</plugin>
"""
import Domoticz
import requests

heartbeat_count = 0

def onStart():
    Domoticz.Log("Domoticz Temperature from Temperature.nu started")

    if (Parameters["Mode4"] == "Debug"):
        Domoticz.Log("TEMPNU Debug is On")
    
    if 1 not in Devices:
        if Parameters["Mode2"] != "":
            Domoticz.Device(Name=Parameters["Mode2"], Unit=1, Type=80, Subtype=5, Used=1).Create()

    # Just keeping the plugin alive. 
    Domoticz.Heartbeat(5) 

def onHeartbeat():
    global heartbeat_count
    # Heartbeat 5 s and update every 60 times give update interval of 5 min.
    if heartbeat_count % 60 == 0: 
        if (Parameters["Mode4"] == "Debug"):
            Domoticz.Log("TEMPNU Heartbeat")
        try:
            url = "https://www.temperatur.nu/termo/gettemp.php?stadname=" + Parameters["Mode2"] + "&what=temp"
            response = requests.get(url).content.decode('latin')
            value = str(round(float(response), 1))
            Devices[1].Update(nValue=1, sValue=value)
            Domoticz.Log("TEMPNU temperature at " + Parameters["Mode2"] + ": " + value)
        except:
            Domoticz.Log("TEMPNU Failed to get data")
            Domoticz.Log("TEMPNU Server response: " + str(response))
    
    heartbeat_count += 1

def onStop():
    Domoticz.Log("TEMPNU Stopped")