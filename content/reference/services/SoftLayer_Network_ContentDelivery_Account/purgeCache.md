---
title: "purgeCache"
description: "CDN's cache mechanism works similar to that of web browsers. When CDN pulls a file from your origin server or from your... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_ContentDelivery_Account"
aliases:
    - "/reference/services/softlayer_network_contentdelivery_account/purgeCache"
---
# [SoftLayer_Network_ContentDelivery_Account](/reference/services/SoftLayer_Network_ContentDelivery_Account)::purgeCache

Purges content on POP


## Overview 
CDN's cache mechanism works similar to that of web browsers. When CDN pulls a file from your origin server or from your CDN FTP directory for the first time, it creates a cache file on itself. CDN re-uses cache files to save trips to the origin server and thus it speeds up delivering content to visitors. This method removes cached objects on every server in the CDN network. If you see a stale content or a file that send an incorrect header, purging cache will correct the issue. CDN will pull a fresh content from your origin server or your CDN FTP. 

This method takes an array of URLs. A URL must be exact as it is being requested by clients. An example URLs may look like this: 
* http://<your CDN username>.http.cdn.softlayer.net/mycdnname/some_file.txt


If you created a CNAME that points to CDN host, use your CNAME URL instead. 
* http://image.mydomain.com/some_file.txt


It takes approximately 3-5 minutes for the system to delete the requested object on every CDN server from submission . 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|objectUrls| array of strings| An array of URLs|


### Required Headers
* authenticate
* SoftLayer_Network_ContentDelivery_AccountInitParameters


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Network_ContentDelivery_PurgeService_Response'>SoftLayer_Container_Network_ContentDelivery_PurgeService_Response[] </a>




