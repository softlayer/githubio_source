---
title: "nsLookup"
description: "A method used to return the nameserver information for a given address"
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Utility"
classes:
    - "SoftLayer_Utility_Network"
---
# SoftLayer_Utility_Network::nsLookup
## Overview 
A method used to return the nameserver information for a given address

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|address| string| An IP address or hostname to nslookup.|
|type| string| The type of record to return A, MX, NS, CNAME, TXT.|


### Required Headers
* authenticate

### Optional Headers

### Return Values
string
