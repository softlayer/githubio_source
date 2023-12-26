---
title: "activatePublicPort"
description: "Activate a server's public network interface to the maximum available speed. This operation is an alias for [SoftLayer_Hardware_Server::setPublicNetworkInterfaceSpeed](/reference/services/SoftLayer_Hardware_Server/setPublicNetworkInterfaceSpeed) with a $newSpeed of -1 and a $redundancy of 'redundant' or unspecified (which results in the best available redundancy state). 

Receipt of a response does not indicate completion of the configuration change. Any subsequent attempts to request the interface change speed or state, while changes are pending, will result in a busy error. 

A response of true indicates a change was required to activate the interface; thus changes are pending. A response of false indicates the interface was already active, and thus no changes are pending. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Server"
type: "reference"
layout: "method"
mainService : "SoftLayer_Hardware_Server"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_Server/{SoftLayer_Hardware_ServerID}/activatePublicPort'
```
