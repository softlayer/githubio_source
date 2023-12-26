---
title: "getBandwidthImage"
description: "This method recurses through all servers on a Bandwidth Pool for a given snapshot range, gathers the necessary parameters, and then calls the bandwidth graphing server.  The return result is a container that includes the min and max dates for all servers to be used in the query, as well as an image in PNG format.  This method uses the new and improved drawing routines which should return in a reasonable time frame now that the new backend data warehouse is used. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Bandwidth_Version1_Allotment"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Bandwidth_Version1_Allotment"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [enum, enum, boolean, dateTime, dateTime]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Bandwidth_Version1_Allotment/{SoftLayer_Network_Bandwidth_Version1_AllotmentID}/getBandwidthImage'
```
