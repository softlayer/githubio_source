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

-----

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


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Network_IntrusionProtection_SubnetReport'>SoftLayer_Container_Network_IntrusionProtection_SubnetReport[] </a>

### External Links


* [http://www.securityfocus.com/vulnerabilities]()


* [http://cve.mitre.org/find/index.html]()




### Error Handling

* SoftLayer_Exception_Public 

> Throw the exception "Parameter 'OrderBy' not valid in SoftLayer_Network_TippingPointReporting getReportForIpAddressOrSubnet.  Valid values are AttackName, SourceIp, AttackCount, Classification, Protocol, Platform" If an invalid argument was passed for the "OrderBy" value 

* SoftLayer_Exception_Public 

> Throw the exception "Parameter 'OrderDirection' not valid in SoftLayer_Network_TippingPointReporting getReportForIpAddressOrSubnet.  Valid values are ASC, DESC" If an invalid argument was passed for the "OrderDirection" value 

* SoftLayer_Exception_Public 

> Throw the exception "Parameter 'timeFrame' not valid in SoftLayer_Network_TippingPointReporting getReportForIpAddressOrSubnet.  Valid values are positive integers less than or equal to 1440" If an invalid  argument was passed for the "timeFrame" value 

* SoftLayer_Exception_Public 

> Throw the exception "IP address not assigned to this account: {Address}" If the supplied IP or subnet does not belong to this account 

* SoftLayer_Exception_Public 

> Throw the exception "Invalid IP Address: {Address}" If the supplied IP or subnet was not formatted correctly. 

* SoftLayer_Exception_Public 

> Throw the exception "There was a problem with the IP address you entered {Address}.  Make sure the IP entered belongs to the current account." If there was an unrecoverable error with the passed IP Address 



