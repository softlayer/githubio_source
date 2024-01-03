---
title: "getFullyQualifiedDomainName"
description: "The getFullyQualifiedDomainName method provides the user with a combined return which includes the hostname and domain for the resource. Because this method returns multiple pieces of information, it avoids the need to use multiple methods to return the desired information. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Resource"
classes:
    - "SoftLayer_Resource_Metadata"
type: "reference"
layout: "method"
mainService : "SoftLayer_Resource_Metadata"
---

# [REST Example](#getFullyQualifiedDomainName-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getFullyQualifiedDomainName-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Resource_Metadata/{SoftLayer_Resource_MetadataID}/getFullyQualifiedDomainName'
```
