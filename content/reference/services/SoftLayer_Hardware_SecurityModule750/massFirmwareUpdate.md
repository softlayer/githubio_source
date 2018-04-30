---
title: "massFirmwareUpdate"
description: "You can launch firmware updates by selecting from your server list. It will bring your server offline for approximately... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_SecurityModule750"
aliases:
    - "/reference/services/softlayer_hardware_securitymodule750/massFirmwareUpdate"
---
# [SoftLayer_Hardware_SecurityModule750](/reference/services/SoftLayer_Hardware_SecurityModule750)::massFirmwareUpdate

Runs firmware updates on the servers components.


## Overview 
You can launch firmware updates by selecting from your server list. It will bring your server offline for approximately 20 minutes while the updates are in progress. 

In the event of a hardware failure during this test our datacenter engineers will be notified of the problem automatically. They will then replace any failed components to bring your server back online, and will be contacting you to ensure that impact on your server is minimal. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|hardwareIds| array of integers| List of hardware ids to have firmware updated.|
|ipmi| boolean| Flag to determine whether IPMI firmware update should occur.|
|raidController| boolean| Flag to determine whether raid controller firmware update should occur.|
|bios| boolean| Flag to determine whether BIOS firmware update should occur.|
|harddrive| boolean| Flag to determine whether hard drive firmware update should occur.|


### Required Headers
* authenticate

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Hardware_Server_Request'>SoftLayer_Container_Hardware_Server_Request[] </a>

