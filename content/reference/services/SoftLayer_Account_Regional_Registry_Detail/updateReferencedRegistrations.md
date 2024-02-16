---
title: "updateReferencedRegistrations"
description: "The subnet registration detail service has been deprecated. 

This method will create a bulk transaction to update any registrations that reference this detail object. It should only be called from a child class such as [SoftLayer_Account_Regional_Registry_Detail_Person](/reference/datatypes/SoftLayer_Account_Regional_Registry_Detail_Person) or [SoftLayer_Account_Regional_Registry_Detail_Network](/reference/datatypes/SoftLayer_Account_Regional_Registry_Detail_Network). The registrations should be in the Open or Registration_Complete status. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Regional_Registry_Detail"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account_Regional_Registry_Detail"
---

### [REST Example](#updateReferencedRegistrations-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#updateReferencedRegistrations-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_Regional_Registry_Detail/{SoftLayer_Account_Regional_Registry_DetailID}/updateReferencedRegistrations'
```
