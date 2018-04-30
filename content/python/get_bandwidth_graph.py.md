---
title: "get_bandwidth_graph.py"
description: "get_bandwidth_graph.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Container_Bandwidth_GraphOutputs"
    - "SoftLayer_Account"
    - "SoftLayer_Metric_Tracking_Object"
    - "SoftLayer_Hardware_Server"
tags:
    - "baremetalservers"
---


```
"""
Retrieve a bandwidth graph for a single server.

Retrieve a bandwidth graph for a single server for an arbitrary start and
end date, specifying graph size and other graphing options. We can do this
with two calls to the SoftLayer API.

Counter data such as bandwidth counters and VSI resource use are stored in
a server's metric tracking object. Our first call retrieves that server's
tracking object record. The second call is to the tracking object service
which will generate a PNG image of our bandwidth graph.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/getObject
http://sldn.softlayer.com/reference/services/SoftLayer_Metric_Tracking_Object/getBandwidthGraph
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Bandwidth_GraphOutputs

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer.API

# Your SoftLayer API username and key.
API_USERNAME = 'set-me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set-me'

"""
The id number of the server whose graph you wish to retrieve. Call the
getHardware() method in the SoftLayer_Account API service to retrieve a list
of the servers on your account.
"""
serverID = 309098
# The date at which you wish to start graphing bandwidth.
startDate = '2017-10-6'
# The date at which you wish to end graphing bandwidth.
endDate = '2017-10-8'
# Whether to get a graph for 'public' or 'private' bandwidth usage.
graphType = 'public'
# The height of the text in the bandwidth graph in pixels.
fontSize = 8
# The width of the graph to retrieve in pixels.
graphWidth = 827
graphHeight = 273
hideTimeZone = True

# Declaring the API client
client = SoftLayer.create_client_from_env(username=API_USERNAME, api_key=API_KEY)
hardwareService = client['SoftLayer_Hardware_Server']
metricTrackingObject = client['SoftLayer_Metric_Tracking_Object']

try:
    trackingObject = hardwareService.getMetricTrackingObject(id=serverID)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to retrieve the metric tracking object: \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))

try:
    """
    getBandwidthGraph() returns a SoftLayer_Container_Bandwidth_GraphOutputs
    object. The contents of the bandwidth image is in $image->graphImage.
    From here you can write it to the file system, display it to a web
    browser, or run other functions on it.
    """
    image = metricTrackingObject.getBandwidthGraph(startDate, endDate, graphType, fontSize,
                                                   graphWidth, graphHeight, hideTimeZone, id=trackingObject['id'])
    print("Image retrieved!")
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to retrieve bandwidth image. \nfaultCode= %s, \nfaultString= %s"
          % (e.faultCode, e.faultString))

```
