#!/usr/bin/env python
"""
Temperature from Temperature.nu for Domoticz
Author: Derenback
"""
"""
<plugin key="TEMPNU" name="Temperature.nu" version="0.0.2" author="Derenback">
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

class BasePlugin:
    heartbeat_count = 0

    def onStart(self):
        Domoticz.Log("Domoticz Temperature from Temperature.nu started")

        if (Parameters["Mode4"] == "Debug"):
            Domoticz.Log("TEMPNU Debug is On")
        
        if 1 not in Devices:
            if Parameters["Mode2"] != "":
                Domoticz.Device(Name=Parameters["Mode2"], Unit=1, Type=80, Subtype=5, Used=1).Create()

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
            try:
                url = "https://www.temperatur.nu/termo/gettemp.php?stadname=" + Parameters["Mode2"].strip() + "&what=temp"
                response = requests.get(url).content.decode('latin')
                value = str(round(float(response), 1))
                Devices[1].Update(nValue=1, sValue=value)
                Domoticz.Log("TEMPNU temperature at " + Parameters["Mode2"] + ": " + value)
            except:
                Domoticz.Log("TEMPNU Failed to get data")
                Domoticz.Log("TEMPNU Server response: " + str(response))
        
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

