---
title: "authenticateResourceRequest"
description: "Internap servers attempts to validate a token before serving a protected content. SoftLayer customer does not need to in... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_ContentDelivery_Account"
---
# [SoftLayer_Network_ContentDelivery_Account](/reference/services/SoftLayer_Network_ContentDelivery_Account)::authenticateResourceRequest

Validates an authentication token


## Overview 
Internap servers attempts to validate a token before serving a protected content. SoftLayer customer does not need to invoke this method.  Please refer to [[SoftLayer_Network_ContentDelivery_Authentication_Token|Authentication Token]] object for more details on Content Authentication Service. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|parameter| <a href='/reference/datatypes/SoftLayer_Container_Network_ContentDelivery_Authentication_Parameter'>SoftLayer_Container_Network_ContentDelivery_Authentication_Parameter </a>| The parameter object contains content authentication token information.|


### Required Headers
* authenticate

### Optional Headers

### Return Values
boolean

