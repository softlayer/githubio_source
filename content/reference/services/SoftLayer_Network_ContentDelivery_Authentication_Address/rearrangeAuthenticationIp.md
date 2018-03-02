---
title: "rearrangeAuthenticationIp"
description: "The authentication IP address match occurs from the higher priority IP to the lower. This method will be helpful if you... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_ContentDelivery_Authentication_Address"
---
# SoftLayer_Network_ContentDelivery_Authentication_Address::rearrangeAuthenticationIp
## Overview 
The authentication IP address match occurs from the higher priority IP to the lower. This method will be helpful if you want to modify the order (priority) of the authentication IP addresses. You can use this method instead of editing individual authentication IP addresses. 

You can retrieve authentication IP address using [[SoftLayer_Network_ContentDelivery_Account::getAuthenticationIpAddresses|getAuthenticationIpAddresses]] method. Then, rearrange the authentication IP addresses and pass them to this method. When creating template objects as parameter, make sure to include the id of each authentication IP addresses. You must provide every authentication IP address.  New priorities will be assigned to each authentication IP addresses in the order of they are passed. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|cdnAccountId| integer| A CDN account id|
|templateObjects| <a href='/reference/datatypes/SoftLayer_Network_ContentDelivery_Authentication_Address'>SoftLayer_Network_ContentDelivery_Authentication_Address[] </a>| An array of authentication IP address objects|


### Required Headers
* authenticate

### Optional Headers

### Return Values
boolean

