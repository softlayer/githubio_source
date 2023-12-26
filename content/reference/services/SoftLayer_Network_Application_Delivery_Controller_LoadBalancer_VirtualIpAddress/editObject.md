---
title: "editObject"
description: "Like any other API object, the load balancers can have their exposed properties edited by passing in a modified version of the object.  The load balancer object also can modify its services in this way.  Simply request the load balancer object you wish to edit, then modify the objects in the services array and pass the modified object to this function.  WARNING:  Services cannot be deleted in this manner, you must call deleteObject() on the service to physically remove them from the load balancer. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress/{SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddressID}/editObject'
```
