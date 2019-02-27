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
aliases:
    - "/reference/services/softlayer_network_tippingpointreporting/drillDownAttack"
---
# [SoftLayer_Network_TippingPointReporting](/reference/services/SoftLayer_Network_TippingPointReporting)::drillDownAttack

Allows for attack-specific drill downs.  Available only in ascending time order.


## Overview 
This method, when given an attack signature ID (available in the return values of getReportForIpAddressOrSubnet and  getSubnetReportForEntireAccount) and an IP Address and subnet mask, returns all attacks for that subnet in the specified time frame and direction.  Once the results have been filtered, additional data is available, including starting and ending times for the attack, originating IP address and port, and destination IP address and port. 

CVE and Bugtraq information is not available at this level. 

-----

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


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Network_IntrusionProtection_SubnetReport'>SoftLayer_Container_Network_IntrusionProtection_SubnetReport </a>



### Error Handling

* SoftLayer_Exception_Public 

> Throw the exception "Parameter 'timeFrame' not valid in SoftLayer_Network_TippingPointReporting getReportForIpAddressOrSubnet.  Valid values are positive integers less than or equal to 1440" If an invalid  argument was passed for the "timeFrame" value 

* SoftLayer_Exception_Public 

> Throw the exception "Parameter 'direction' not valid in SoftLayer_Network_TippingPointReporting getReportForIpAddressOrSubnet.  Valid values are Inbound, Outbound" If an invalid attack direction has been specified 

* SoftLayer_Exception_Public 

> Throw the exception "IP address not assigned to this account: {Address}" If the supplied IP or subnet does not belong to this account 

* SoftLayer_Exception_Public 

> Throw the exception "Invalid IP Address: {Address}" If the supplied IP or subnet was not formatted correctly. 

* SoftLayer_Exception_Public 

> Throw the exception "There was a problem with the IP address you entered {Address}.  Make sure the IP entered belongs to the current account." If there was an unrecoverable error with the passed IP Address 



