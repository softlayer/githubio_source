---
title: "deleteObject"
description: "Delete an external authentication binding.  If the external binding currently has an active billing item associated you will be prevented from deleting the binding.  The alternative method to remove an external authentication binding is to use the service cancellation form. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_External_Binding"
type: "reference"
layout: "method"
mainService : "SoftLayer_User_Customer_External_Binding"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_External_Binding/{SoftLayer_User_Customer_External_BindingID}/deleteObject'
```
