---
title: "getTopTenSyslogEventsByDestinationPortOneDay"
description: "Top Ten network datacenter syslog events, grouped by destination port, for the last 24 hours"
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet_IpAddress"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Subnet_IpAddress"
---

# [REST Example](#getTopTenSyslogEventsByDestinationPortOneDay-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getTopTenSyslogEventsByDestinationPortOneDay-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Subnet_IpAddress/{SoftLayer_Network_Subnet_IpAddressID}/getTopTenSyslogEventsByDestinationPortOneDay'
```
