---
title: "createOriginPullMapping"
description: "With Origin Pull, content is pulled from your origin server as needed and then delivered to visitors. You do not need to... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_ContentDelivery_Account"
---
# SoftLayer_Network_ContentDelivery_Account::createOriginPullMapping
## Overview 
With Origin Pull, content is pulled from your origin server as needed and then delivered to visitors. You do not need to upload your files to the CDN FTP: you can utilize the files that currently exist on your origin server. It will take 10 to 15 minutes for this to take effect after you create an Origin Pull rule. Origin Pull is only supported for HTTP protocol and you would continue to use the CDN FTP for Flash and Windows Media streaming services. 

A valid origin host can include a directory information.  You may include an authentication username and password along with an origin host. If you set an authentication username and password, CDN servers will include "Authorization:" header in every request. You may use the "Authorization:" header to grant access to CDN servers or you may use it to distinguish CDN servers from normal visitors. Here is a list of valid origin hosts: 
* www.website.com
* www.website.com/cdn_content
* cdn_user:password@www.website.com
* cdn_user:password@www.website.com/images


An authentication username should be an alphanumeric string and allowed special characters are . - _<br /> An authentication password should be an alphanumeric string and allowed special characters are . - _ ! # $ % ^ & *<br /> Both username and password must be between 3 to 10 characters long. 

CDN nodes will cache your contents and you can control cache lifetime by modifying your web server's configuration. This method also creates a FTP directory restriction upon successful Origin Pull set up. You will not be able to access /media/http directory since contents will be pulled from your origin server. An origin domain must be a valid domain name and it can contain path information. This can help you organize contents on your origin server. For example, you could set an origin domain as: mydomain.com/cdn_contents 

A CNAME record allows you to have a customized URL. You can get rid of your CDN account name from the URL. A valid CNAME for the Origin Pull method must point to <CDN_AcccountName>.http.cdn.softlayer.net. 

There are 2 types of origin pull mappings.  The one with a CNAME record or the one without a CNAME record and they work very differently. 

gzip is supported if your web server sends a proper gzip header. For more details, visit our [http://knowledgelayer.softlayer.com/topic/cdn KnowledgeLayer] 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|mappingObject| <a href='/reference/datatypes/SoftLayer_Container_Network_ContentDelivery_OriginPull_Mapping'>SoftLayer_Container_Network_ContentDelivery_OriginPull_Mapping </a>| An origin pull mapping template object|


### Required Headers
* authenticate
* SoftLayer_Network_ContentDelivery_AccountInitParameters

### Optional Headers

### Return Values
boolean
