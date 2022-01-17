---
title: "Event Logs"
description: "Some examples of Event Log, with pagination support"
date: "2018-05-18"
classes: 
    - "SoftLayer_Event_Log"
tags:
    - "objectfilter"
    - "resultlimit"
---


This example deals with a few ways of pulling data from `SoftLayer_Event_Log`. There can ben quite a few Logs here, so I recommend using a filter like in the `recentLogs` function to limit how far back you search for Events, otherwise you will be paging through Events for a long time.

```python
"""
@author Christopher Gallo
"""
import datetime
import SoftLayer

class example():

    def __init__(self):

        self.client = SoftLayer.Client()
        debugger = SoftLayer.DebugTransport(self.client.transport)
        self.client.transport = debugger

    def recentLogs(self):
        """REST API CALL
        'https://api.softlayer.com/rest/v3.1/SoftLayer_Event_Log/getAllObjects.json?
            resultLimit=0,50&
            objectFilter={"eventCreateDate":{"operation":"greaterThanDate","options":[{"name":"date","value":["2018-04-18T00:00:00.0000-06:00"]}]}}'
        """
        _filter = {
            'eventCreateDate': { 
                'operation': 'greaterThanDate', 
                'options': [
                    {'name': 'date', 'value': [getDateString(30)]}
                ]
            }
        }
        for event in self.getAllObjects(_filter):
            printLogs(event)

    def systemLogs(self):
        """REST API CALL
        'https://api.softlayer.com/rest/v3.1/SoftLayer_Event_Log/getAllObjects.json?
            resultLimit=0,50&
            objectFilter={"userType":{"operation":"SYSTEM"}}'
        """
        _filter = {'userType': {'operation': 'SYSTEM'}}
        for event in self.getAllObjects(_filter):
            printLogs(event)

    def loginLogs(self):
        """REST API CALL
        https://api.softlayer.com/rest/v3.1/SoftLayer_Event_Log/getAllObjects.json?
            resultLimit=0,50&
            objectFilter={"eventName":{"operation":"^= Login"}}'
        """
        _filter = {
            'eventName': {
                'operation': '^= Login'
            }
        }
        for event in self.getAllObjects(_filter):
            printLogs(event)

    def allLogs(self):
        """REST API CALL
        'https://api.softlayer.com/rest/v3.1/SoftLayer_Event_Log/getAllObjects.json?resultLimit=0,50'
        """
        for event in self.getAllObjects(None):
            printLogs(event)
        

    def getAllObjects(self, _filter, limit=50, offset=0):
        """Pages through all results from the Event_Log. This might take long time."""
        notDone = True
        while notDone:
            events = self.client.call('SoftLayer_Event_Log', 'getAllObjects', filter=_filter, limit=limit, offset=offset)
            print("%s from getAllObjects, offset = %s" % (len(events), offset))

            for event in events:
                yield event
            if len(events) < limit:
                notDone = False
            offset = offset + limit
            notDone = False

    def debug(self):
        for call in self.client.transport.get_last_calls():
            print(self.client.transport.print_reproduceable(call))


def getDateString(self, delta=30):
    date_object = datetime.date.today() - datetime.timedelta(days=delta)
    return date_object.strftime("%Y-%m-%dT00:00:00.0000-06:00")

def printLogs(log):
    print("%s - %s - %s" % (log['eventName'],log['eventCreateDate'], log['userType']))

if __name__ == "__main__":
    main = example()
    main.allLogs()
    main.debug()





```