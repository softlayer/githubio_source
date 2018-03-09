---
title: "drillDownAttack"
description: "This method, when given an attack signature ID (available in the return values of getReportForIpAddressOrSubnet and  get... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_TippingPointReporting"
---
# [SoftLayer_Network_TippingPointReporting](/reference/services/SoftLayer_Network_TippingPointReporting)::drillDownAttack

Allows for attack-specific drill downs.  Available only in ascending time order.


## Overview 
This method, when given an attack signature ID (available in the return values of getReportForIpAddressOrSubnet and  getSubnetReportForEntireAccount) and an IP Address and subnet mask, returns all attacks for that subnet in the specified time frame and direction.  Once the results have been filtered, additional data is available, including starting and ending times for the attack, originating IP address and port, and destination IP address and port. 

CVE and Bugtraq information is not available at this level. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|signatureId| string| The unique ID for this attack signature.  SignatureId is a part of the data returned by getReportForIpAddressOrSubnet and getSubnetReportForEntireAccount on this service|
|IpAddress| string| in dotted decimal format|
|subnetMask| integer| (optional) the number of bits that are set to 1 in the subnet mask.  If your subnet is 192.168.1.1/24, enter 24 here.  Default: 32|
|timeFrame| integer| (optional) number of minutes back to search from the present (default 60)|
|direction| string| (optional) Either 'Inbound' or 'Outbound', determines which direction you would like to search.  Default: Inbound|


### Required Headers
* authenticate

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Network_IntrusionProtection_SubnetReport'>SoftLayer_Container_Network_IntrusionProtection_SubnetReport </a>

