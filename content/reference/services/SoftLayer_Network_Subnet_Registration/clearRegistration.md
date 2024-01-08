---
title: "clearRegistration"
description: "This method will initiate the removal of a subnet registration. "
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

### [REST Example](#clearRegistration-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#clearRegistration-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Subnet_Registration/{SoftLayer_Network_Subnet_RegistrationID}/clearRegistration'
```
