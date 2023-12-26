---
title: "updateReferencedRegistrations"
description: "This method will create a bulk transaction to update any registrations that reference this detail object. It should only be called from a child class such as [SoftLayer_Account_Regional_Registry_Detail_Person](/reference/datatypes/SoftLayer_Account_Regional_Registry_Detail_Person) or [SoftLayer_Account_Regional_Registry_Detail_Network](/reference/datatypes/SoftLayer_Account_Regional_Registry_Detail_Network). The registrations should be in the Open or Registration_Complete status. "
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_Regional_Registry_Detail/{SoftLayer_Account_Regional_Registry_DetailID}/updateReferencedRegistrations'
```
