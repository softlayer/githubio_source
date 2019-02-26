---
title: "getTimedToken"
description: "This method returns an authentication token that expires after the seconds you specify. You can provide number of second... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_ContentDelivery_Authentication_Token"
aliases:
    - "/reference/services/softlayer_network_contentdelivery_authentication_token/getTimedToken"
---
# [SoftLayer_Network_ContentDelivery_Authentication_Token](/reference/services/SoftLayer_Network_ContentDelivery_Authentication_Token)::getTimedToken

Returns an authentication token that expires after a certain amount of time


## Overview 
This method returns an authentication token that expires after the seconds you specify. You can provide number of seconds to manage the token life.  This parameter sets the expiration time for a token. A valid life time must be an integer between 60 and 604800 (1 week). A customer can also provide client ip and (or) referrer information.  If used, a client from the same IP and referrer can view the protected contents. 

A valid IP address must be an IPv4 format or an IP block. if you want to block access from IP 211.37.0.0/16, you can enter "211.37." instead. IP blocks can be specified in the manner of "8bit times n". 

The referrer is the URL of the previous webpage from which a link was followed.  A referrer should not include "http://" prefix and it can be maximum of 30 characters. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|cdnAccountId| integer| a CDN account Id|
|tokenLife| integer| Number of seconds that determines how long a token will be valid.  This must be an integer between 60 and 604800.|
|clientIp| string| The client IP address (Optional). If supplied, token validation will match the client IP.|
|referrer| string| The referrer (Optional). If supplied, token validation will match the referrer.|
|mediaType| string| The media type of which your content will be authenticated. Valid types HTTP_LARGE, HTTP_SMALL, FLASH and WM|


### Required Headers
* authenticate


### Return Values
* string




