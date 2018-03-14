---
title: "setAuthenticationServiceEndpoint"
description: "CDN servers will invoke a Web Service method to validate a content authentication token. CDN uses the default Web Servic... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_ContentDelivery_Account"
aliases:
    - "/reference/services/softlayer_network_contentdelivery_account/setAuthenticationServiceEndpoint"
---
# [SoftLayer_Network_ContentDelivery_Account](/reference/services/SoftLayer_Network_ContentDelivery_Account)::setAuthenticationServiceEndpoint

Sets the token validation web service endpoint


## Overview 
CDN servers will invoke a Web Service method to validate a content authentication token. CDN uses the default Web Service provided by SoftLayer to validate a token. A customer can use their own implementation of the token authentication Web Service. A valid SOAP WSDL will look similar [https://manage.softlayer.com/CdnService/authenticationWsdlExample/wsdl this]. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|webserviceEndpoint| string| The content authentication web service endpoint that CDN server will use.  For example, "http://mysite.com/Authentication.asmx"|
|protocol| string| The protocol that the WSDL will be used for. "ALL", "FLASH", "WINDOWSMEDIA", or "HTTP" are supported.|


### Required Headers
* authenticate
* SoftLayer_Network_ContentDelivery_AccountInitParameters

### Optional Headers

### Return Values
boolean

