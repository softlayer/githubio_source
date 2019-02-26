---
title: "editObject"
description: "Edit the properties of a global load balancer account by passing in a modified instance of the object. The global load b... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LoadBalancer_Global_Account"
aliases:
    - "/reference/services/softlayer_network_loadbalancer_global_account/editObject"
---
# [SoftLayer_Network_LoadBalancer_Global_Account](/reference/services/SoftLayer_Network_LoadBalancer_Global_Account)::editObject

Edit a global load balancer account and the hosts that make up the load balancing pool.


## Overview 
Edit the properties of a global load balancer account by passing in a modified instance of the object. The global load balancer account properties you are able to edit are: fallback ip, load balance type id, and notes. Hosts that belong to your SoftLayer global load balancer account are created and modified through this method. An example templateObject that updates global load balancer account properties, updates the properties of a host, and adds a new host is shown below: 


* id: 2
* loadBalanceTypeId: 2
* notes: Notes updated
* fallbackIp: 1.1.1.1
* hosts:
** id: 19
** destinationIp: 2.2.2.2
** weight: 25
** healthCheck: http
** destinationPort: 80
** enabled: 1<br /><br />
** destinationIp: 3.3.3.3
** weight: 25
** healthCheck: http
** destinationPort: 80
** enabled: 1




The first section contains the properties of the global load balancer account that will be updated, while the second section contains the elements of the 'hosts' property of the global load balancer account.  The first host listed will have its properties updated because the 'id' property of the host is set, meaning the global load balancer host with an id of 19 will be updated. The second host listed will be created because it lacks the 'id' property. 

There is a limit to the maximum number of hosts that you are allowed to add, and is defined by the allowedNumberOfHosts property on the global load balancer account.  The destination IP address of a host must be an IP address that belongs to your SoftLayer Account, or a local load balancer virtual IP address that belongs to your account.  The destination IP address and destination port are required and must be provided when creating a host. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Network_LoadBalancer_Global_Account'>SoftLayer_Network_LoadBalancer_Global_Account </a>| A skeleton SoftLayer_Network_LoadBalancer_Global_Account object with only the properties defined that you wish to change. Unchanged properties are left alone.|


### Required Headers
* authenticate
* SoftLayer_Network_LoadBalancer_Global_AccountInitParameters


### Return Values
* boolean



### Error Handling

* SoftLayer_Exception_Public 

> Throw the exception "You are not allowed to change the hostname of this account." when trying to edit the hostname property of a global load balancer account. 

* SoftLayer_Exception_Public 

> Throw the exception "You are not allowed to change the load balancer id." when trying to edit the loadBalancerId property of a global load balancer account. 

* SoftLayer_Exception_Public 

> Throw the exception "You are not allowed to change the number of hosts." when trying to edit the allowedNumberOfHosts property of a global load balancer account. 

* SoftLayer_Exception_Public 

> Throw the exception "You are not allowed to change the connections per second." when trying to edit the connectionsPerSecond property of a global load balancer account. 

* SoftLayer_Exception_Public 

> Throw the exception "You are not allowed to change the average connections per second." when trying to edit the averageConnectionsPerSecond property of a global load balancer account. 

* SoftLayer_Exception_Public 

> Throw the exception "You have already reached the maximum allowed hosts for this account." when trying to add a new when you have already reached the maximum allowed number of hosts limit. 

* SoftLayer_Exception_Public 

> Throw the exception "The IP address you supplied does not belong to your account or a local load balancer." when trying to add or edit a host whose destination ip does not belong to your softlayer customer account, or a local load balancer virtual ip that belongs to your account. 

* SoftLayer_Exception_Public 

> Throw the exception "The host could not be created on the global load balancers." when adding a new host and the global load balancers return an error. 

* SoftLayer_Exception_Public 

> Throw the exception "The host could not be updated on the global load balancers." when editing a host and the global load balancers return an error. 

* SoftLayer_Exception_Public 

> Throw the exception "The host could not be removed from the global load balancers." when deleteing a host and the global load balancers return an error. 

* SoftLayer_Exception_Public 

> Throw the exception "A location could not be determined for the given ip: <destination ip>." when adding a new host that does not have a valid location. 

* SoftLayer_Exception_Public 

> Throw the exception "The health check type only accepts the folowing values: none, http, or tcp." when changing the health check type of a host. 

* SoftLayer_Exception_Public 

> Throw the exception "The destination IP and port are required and can not be null." when creating or editing a host with a blank destination ip or destination port. 



