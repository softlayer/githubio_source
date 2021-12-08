---
title: "clearRoute"
description: "This interface allows you to remove the route of your Account Owned subnets. The result will be a subnet that is no long... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet"
aliases:
    - "/reference/services/softlayer_network_subnet/clearRoute"
---
# [SoftLayer_Network_Subnet](/reference/services/SoftLayer_Network_Subnet)::clearRoute





## Overview 
This interface allows you to remove the route of your Account Owned subnets. The result will be a subnet that is no longer routed on the network. Remove the route of subnets you are not actively using, as it will make it easier to identify available subnets later. 

'''Important:''' When removing the route of ''Portable'' subnets, know that any subnet depending on an IP address provided by the Portable subnet will also have their routes removed! 

To review what subnets are routed to IP addresses provided by a ''Portable'' subnet, you can utilize the following object mask: 'mask[ipAddresses[endpointSubnets]]'. Any subnet present in conjunction with ''endpointSubnets'' is a subnet which depends on the respective IP address. 

The behavior of this interface is such that either true or false is returned. A result of false can be interpreted as the clear route request having already been completed. In contrast, a result of true means the subnet is currently routed and will be transitioned. This route change is asynchronous to the request. A response of true does not mean the subnet's route has changed, but simply that it will change. In order to monitor for the completion of the change, you may either attempt a clear route again until the result is false, or monitor one or more SoftLayer_Network_Subnet properties: subnetType, networkVlanId, and or endPointIpAddress to determine if routing of the subnet has been removed. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_SubnetInitParameters


### Return Values
* boolean



### Error Handling

* SoftLayer_Exception_AccessDenied 

> If the user lacks permissions for route manipulation. 

* SoftLayer_Exception_Unavailable 

> If the subnet is not eligible for route manipulation. 

* SoftLayer_Exception_NotReady 

> If another route request is in progress for the subnet. 



