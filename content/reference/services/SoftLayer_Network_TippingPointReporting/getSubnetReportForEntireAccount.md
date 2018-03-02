---
title: "getSubnetReportForEntireAccount"
description: "This method returns specific attacks by name for all subnets on the current user's account. 

The data returned is store... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_TippingPointReporting"
---
# SoftLayer_Network_TippingPointReporting::getSubnetReportForEntireAccount
## Overview 
This method returns specific attacks by name for all subnets on the current user's account. 

The data returned is stored in SoftLayer_Container_Network_IntrusionProtection_SubnetReport objects, with the "subnet" value set to "All Subnets" 

The data is separated into "Inbound" and "Outbound" traffic.  A significant amount of outbound attack traffic could indicate that your servers have been compromised. 

The data returned includes Attack Count, attack name, extended attack description, and IDs that correspond with the BugTraq or CVE databases. BugTraq can be accessed at [http://www.securityfocus.com/vulnerabilities] The CVE database is located at [http://cve.mitre.org/find/index.html] 

For more detailed information, use the getReportForIpAddressOrSubnet method 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|timeFrame| integer| (optional) number of minutes back to search from the present (default 60)|
|orderBy| string| (optional) valid values are AttackName, SourceIp, AttackCount, Classification, Protocol, Platform (default AttackCount)|
|orderDirection| string| (optional) either ASC or DESC (Default DESC)|
|returnSubnetGroups| boolean| (optional) Set to true if you want individual subnet groups in addition to the "all subnets" group.|


### Required Headers
* authenticate

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Network_IntrusionProtection_SubnetReport'>SoftLayer_Container_Network_IntrusionProtection_SubnetReport[] </a>

### External Links


* [The Security focus (BugTraq) database](http://www.securityfocus.com/vulnerabilities)


* [The MITRE (CVE) database](http://cve.mitre.org/find/index.html)


