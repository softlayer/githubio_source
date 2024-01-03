---
title: "shutdownPrivatePort"
description: "Disconnect a server's private network interface. This operation is an alias for calling [SoftLayer_Hardware_Server::setPrivateNetworkInterfaceSpeed](/reference/services/SoftLayer_Hardware_Server/setPrivateNetworkInterfaceSpeed) with a $newSpeed of 0 and unspecified $redundancy. 

Receipt of a response does not indicate completion of the configuration change. Any subsequent attempts to request the interface change speed or state, while changes are pending, will result in a busy error. 

A response of true indicates a change was required to disconnect the interface; thus changes are pending. A response of false indicates the interface was already disconnected, and thus no changes are pending. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule"
type: "reference"
layout: "method"
mainService : "SoftLayer_Hardware_SecurityModule"
---

# [REST Example](#shutdownPrivatePort-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#shutdownPrivatePort-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Hardware_SecurityModule/{SoftLayer_Hardware_SecurityModuleID}/shutdownPrivatePort'
```
