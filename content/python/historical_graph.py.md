---
title: "historical_graph.py"
description: "historical_graph.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
tags:
    - "graphs"
---


```
"""
Get Historical Bandwidth

The script makes a single call to Softlayer_Account::getHistoricalBandwidthGraph method
to display the historical bandwidth graph.
For more information see below

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getHistoricalBandwidthGraph
http://sldn.softlayer.com/reference/services/SoftLayer_Account

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer

"""
Your SoftLayer API username and key.

Generate an API key at the SoftLayer Customer Portal:
https://manage.softlayer.com/Administrative/apiKeychain
"""
USERNAME = 'set me'
API_KEY = 'set me'

startDate = '2014-9-8'
endDate = '2014-9-18'

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)

try:
    graph = client['Account'].getHistoricalBandwidthGraph(startDate, endDate)
    print(graph)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get the historical bandwidth graph faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
