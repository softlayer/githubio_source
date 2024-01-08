---
title: "updateNetScalerLicense"
description: "Update the NetScaler VPX License. 

This service will create a transaction to update a NetScaler VPX License.  After the license is updated the load balancer will reboot in order to apply the newly issued license 

The load balancer will be unavailable during the reboot. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Application_Delivery_Controller"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Application_Delivery_Controller"
---

### [REST Example](#updateNetScalerLicense-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#updateNetScalerLicense-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Application_Delivery_Controller/{SoftLayer_Network_Application_Delivery_ControllerID}/updateNetScalerLicense'
```
