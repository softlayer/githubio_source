---
title: "getCustomGraphData"
description: "An example of how to use getCustomGraphData"
date: "2015-10-11"
classes: ["SoftLayer_Metric_Tracking_Object"]
tags:
    - "getCustomGraphData"
    - "getSummaryData"
    - "getBandwidthData"
---



```python

import SoftLayer
from pprint import pprint as pp

class example():

    def __init__(self):
        self.client = SoftLayer.Client()

    def main(self):

        client = SoftLayer.Client()
        result = client['SoftLayer_Metric_Tracking_Object'].getBandwidthData('2015-10-01','2015-11-31','public',600,id=10413573)
        result = client['SoftLayer_Metric_Tracking_Object'].getSummaryData('2015-11-01','2015-11-02',[{'keyName':'PUBLICIN','summaryType':'counter','name':'vif_1_rx'}],600,id=10413573)
        args = {
            'startDateTime' : '2015-11-01',
            'endDateTime':'2015-11-02',
            'metrics': [{'keyName':'PUBLICIN','summaryType':'counter','name':'vif_1_rx'}],
            'interval':600,
            'returnImage': False
        }
        result = client['SoftLayer_Metric_Tracking_Object'].getCustomGraphData(args,id=10413573)
        pp(result)

if __name__ == "__main__":
    main = example()
    main.main()

```
