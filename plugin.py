#!/usr/bin/env python
"""
Temperature from Temperature.nu for Domoticz
Author: Derenback
"""
"""
<plugin key="TEMPNU" name="Temperature.nu" version="0.0.3" author="Derenback">
    <description>
        <h2>Temperature.nu plugin</h2><br/>
        <h3>Locations</h3><br/>
        Add locations separated by a comma ",".<br/>
        Ex. "mosas,salen_by"<br/>
        A list of locations can be found here: <A Href="https://www.temperatur.nu/matplatser" Target="_blank">www.temperatur.nu/matplatser</A><br/>
        Note that adding many locations might violate the terms.<br/>
        Read more here: <A Href="https://www.temperatur.nu/" Target="_blank">www.temperatur.nu/</A><br/>
    </description>
    <params>
        <param field="Mode2" label="Locations" width="300px" required="true" default="" />
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

class BasePlugin:
    heartbeat_count = 0
    locations = []

    def onStart(self):
        Domoticz.Log("Domoticz Temperature from Temperature.nu started")

        if (Parameters["Mode4"] == "Debug"):
            Domoticz.Log("TEMPNU Debug is On")

        self.locations = Parameters["Mode2"].split(",")
        for index, location in enumerate(self.locations, start=1):
            if index not in Devices:
                Domoticz.Device(Name=location, Unit=index, Type=80, Subtype=5, Used=1).Create()

        # Just keeping the plugin alive. 
        Domoticz.Heartbeat(5) 

    def onStop(self):
        Domoticz.Log("TEMPNU Stopped")

    def onHeartbeat(self):
        global heartbeat_count
        if (Parameters["Mode4"] == "Debug"):
            Domoticz.Log("TEMPNU Heartbeat")
        # Heartbeat 5 s and update every 60 times give update interval of 5 min.
        if self.heartbeat_count % 60 == 0:
            for index, location in enumerate(self.locations, start=1):
                try:
                    url = "https://www.temperatur.nu/termo/gettemp.php?stadname=" + location.strip() + "&what=temp"
                    response = requests.get(url).content.decode('latin')
                    value = str(round(float(response), 1))
                    Devices[index].Update(nValue=1, sValue=value)
                    if (Parameters["Mode4"] == "Debug"):
                        Domoticz.Log(f"TEMPNU Temperature at {location.strip()} is {value} C°")
                except:
                    Domoticz.Log(f"TEMPNU Failed to get data for location {location}")
                    Domoticz.Log(f"TEMPNU Server response: {str(response)}")
        
        self.heartbeat_count += 1
        

global _plugin
_plugin = BasePlugin()

def onStart():
    global _plugin
    _plugin.onStart()

def onStop():
    global _plugin
    _plugin.onStop()

def onHeartbeat():
    global _plugin
    _plugin.onHeartbeat()

