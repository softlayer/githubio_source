---
title: "get_bandwidth_usage.py"
description: "get_bandwidth_usage.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "virtualserver"
---


```
"""
Get Bandwidth usage.

getCurrentBandwidthSummary: Retrieves an object that provides commonly used
bandwidth summary components for the current billing cycle.

getBandwidthDataByDate: Use this method when needing the metric data for
bandwidth for a single guest. It will gather the correct input parameters
based on the date ranges.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getBandwidthDataByDate
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getCurrentBandwidthSummary
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer
import datetime
from pprint import pprint as pp

# Your SoftLayer API username and key.
API_USERNAME = 'set me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set me'

# Set the server id that you wish to get bandwidth usage information.
serverId = 35747489

# Create a SoftLayer Client.
client = SoftLayer.create_client_from_env(
    username=API_USERNAME,
    api_key=API_KEY
)

# Getting Current Bandwidth Summary:
try:
    currentBandwidthSummary = client['Virtual_Guest'].getCurrentBandwidthSummary(id=serverId)
    pp(currentBandwidthSummary)

except SoftLayer.SoftLayerAPIError as e:
        pp('Unable to get Bandwidth Summary faultCode=%s, faultString=%s'
            % (e.faultCode, e.faultString))

# Getting the Bandwidth Data By Date:
try:
    endDate = datetime.datetime.today()
    timeRange = datetime.timedelta(days=1)
    startDate = endDate - timeRange

    startDate = startDate.isoformat()
    endDate = endDate.isoformat()

    objectTemplate = {
            'startDateTime': startDate,
            'endDateTime': endDate,
            'networkType': 'public'
        }

    bandwidthDataByDate = client['Virtual_Guest'].getBandwidthDataByDate(
                objectTemplate,
                id=serverId)
    pp(bandwidthDataByDate)

except SoftLayer.SoftLayerAPIError as e:
        pp('Unable to get Bandwidth usage information faultCode=%s, faultString=%s'
            % (e.faultCode, e.faultString))

```
