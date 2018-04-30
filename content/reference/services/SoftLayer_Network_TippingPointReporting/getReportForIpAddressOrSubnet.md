---
title: "getReportForIpAddressOrSubnet"
description: "This method expands on the getSubnetReportForEntireAccount method by offering the ability to filter by subnet or IP addr... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_TippingPointReporting"
aliases:
    - "/reference/services/softlayer_network_tippingpointreporting/getReportForIpAddressOrSubnet"
---
# [SoftLayer_Network_TippingPointReporting](/reference/services/SoftLayer_Network_TippingPointReporting)::getReportForIpAddressOrSubnet

Returns a point-by-point breakdown of all attacks on a particular IP or subnet in the given time period.


## Overview 
This method expands on the getSubnetReportForEntireAccount method by offering the ability to filter by subnet or IP address. This method is identical to getSubnetReportForEntireAccount, but allows filtering by subnet.  Like in the getSubnetReportForEntireAccount method, CVE and BugTraq IDs are provided, if available. 

This method should be called once an attack has been identified using getSubnetReportForEntireAccount (in which case "All Subnets" is the subnet) or getReportForIpAddressOrSubnet. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|IpAddress| string| the IP address you wish to search on.  Passed as a dotted decimal string ("All Subnets" is also accepted).|
|subnetMask| integer| (optional) the number of bits that are set to 1 in the subnet mask.  If your subnet is 192.168.1.1/24, enter 24 here.  Default: 32|
|timeFrame| integer| (optional) number of minutes back to search from the present (default 60)|
|orderBy| string| (optional) valid values are AttackName, SourceIp, AttackCount, Classification, Protocol, Platform (default AttackCount)|
|orderDirection| string| (optional) either ASC or DESC (Default DESC)|


### Required Headers
* authenticate

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Network_IntrusionProtection_SubnetReport'>SoftLayer_Container_Network_IntrusionProtection_SubnetReport[] </a>

### External Links


* [http://www.securityfocus.com/vulnerabilities]()


* [http://cve.mitre.org/find/index.html]()


