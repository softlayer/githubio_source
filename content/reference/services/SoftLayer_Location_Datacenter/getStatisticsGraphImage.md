---
title: "getStatisticsGraphImage"
description: "Retrieve a graph of a SoftLayer datacenter's last 48 hours of network activity. Statistics graphs show traffic outbound from a datacenter on top and inbound traffic on the bottom followed by a legend of the network services tracked in the graph. getStatisticsGraphImage returns a PNG image of variable width and height depending on the number of services reported in the image. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Location"
classes:
    - "SoftLayer_Location_Datacenter"
type: "reference"
layout: "method"
mainService : "SoftLayer_Location_Datacenter"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Location_Datacenter/{SoftLayer_Location_DatacenterID}/getStatisticsGraphImage'
```
