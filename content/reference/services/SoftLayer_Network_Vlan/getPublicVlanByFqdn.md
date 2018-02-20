---
title: "getPublicVlanByFqdn"
description: "Retrieve the VLAN that belongs to a server's public network interface, as described by a server's fully-qualified domain... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Vlan"
---
# SoftLayer_Network_Vlan::getPublicVlanByFqdn
## Overview 
Retrieve the VLAN that belongs to a server's public network interface, as described by a server's fully-qualified domain name. A server's ''FQDN'' is it's hostname, followed by a period then it's domain name. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|fqdn| string| The fully-qualified domain name of the server you wish to search for. This follows the naming convention "{hostname}.{domain}".|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Network_VlanObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan </a>
