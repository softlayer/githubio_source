---
title: "deleteObject"
description: "Delete a VeriSign external binding.  The only VeriSign external binding that can be deleted through this method is the free VeriSign external binding for the master user of a SoftLayer account. All other external bindings must be canceled using the SoftLayer service cancellation form. 

When a VeriSign external binding is deleted the credential is deactivated in VeriSign's system for use on the SoftLayer site and the $0 billing item associated with the free VeriSign external binding is cancelled. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_External_Binding_Verisign"
type: "reference"
layout: "method"
mainService : "SoftLayer_User_Customer_External_Binding_Verisign"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_External_Binding_Verisign/{SoftLayer_User_Customer_External_Binding_VerisignID}/deleteObject'
```
