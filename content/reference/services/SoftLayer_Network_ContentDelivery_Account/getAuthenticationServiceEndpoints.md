---
title: "getAuthenticationServiceEndpoints"
description: "CDN servers will invoke a Web Service method to validate a content authentication token. This method returns all token v... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_ContentDelivery_Account"
---
# SoftLayer_Network_ContentDelivery_Account::getAuthenticationServiceEndpoints
## Overview 
CDN servers will invoke a Web Service method to validate a content authentication token. This method returns all token validation web service endpoints set for a CDN account. You can override the default web service by calling [[SoftLayer_Network_ContentDelivery_Authentication_Token|setContentAuthenticationWsdl setContentAuthenticationWsdl]] method. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Network_ContentDelivery_AccountInitParameters

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Network_ContentDelivery_Authentication_ServiceEndpoint'>SoftLayer_Container_Network_ContentDelivery_Authentication_ServiceEndpoint[] </a>
