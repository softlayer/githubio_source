---
title: "Server Bandwidth"
description: "A handy script to get and print relevant server bandwidth details"
date: "2015-06-15"
classes: 
    - "SoftLayer_Metric_Tracking_Object"
    - "SoftLayer_Hardware_Server"
tags:
    - "server"
    - "bandwidth"
---

```python

import SoftLayer
from pprint import pprint as pp

class example():

    def __init__(self):
        self.client = SoftLayer.Client()

    def main(self, tracking_id):

        tracking_service = self.client['SoftLayer_Metric_Tracking_Object']
        bw_result = tracking_service.getBandwidthData('2015-10-01', '2015-11-31', 'public', 600, id=tracking_id)
        object_type = [{'keyName':'PUBLICIN','summaryType':'counter','name':'vif_1_rx'}]
        summary_result = tracking_service.getSummaryData('2015-11-01','2015-11-02', object_type, 600, id=tracking_id)
        args = {
            'startDateTime' : '2015-11-01',
            'endDateTime':'2015-11-02',
            'metrics': [{'keyName':'PUBLICIN','summaryType':'counter','name':'vif_1_rx'}],
            'interval':600,
            'returnImage': False
        }
        custom_result = tracking_service.getCustomGraphData(args,id=tracking_id)
        pp(custom_result)

    # For use with a virtual Guest, just change
    # SoftLayer_Hardware_Server here with SoftLayer_Virtual_Guest
    def getTrackingId(self, server_id):
        tracking_id = self.client['SoftLayer_Hardware_Server'].getMetricTrackingObjectId(id=server_id)
        return tracking_id

if __name__ == "__main__":
    main = example()
    # CHANGE THIS
    my_server_id = 12345
    tracking_id = main.getTrackingId(my_server_id)
    main.main(tracking_id)
```