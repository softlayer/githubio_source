---
title: "editRegistrationAttachedDetails"
description: "The subnet registration service has been deprecated. 

This method modifies a single registration by modifying the current [SoftLayer_Network_Subnet_Registration_Details](/reference/datatypes/SoftLayer_Network_Subnet_Registration_Details) objects that are linked to that registration. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet_Registration"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Subnet_Registration"
---

### [REST Example](#editRegistrationAttachedDetails-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#editRegistrationAttachedDetails-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_Subnet_Registration_Details, SoftLayer_Network_Subnet_Registration_Details]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Subnet_Registration/editRegistrationAttachedDetails'
```
