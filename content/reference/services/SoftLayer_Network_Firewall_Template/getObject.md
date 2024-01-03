---
title: "getObject"
description: "getObject returns a SoftLayer_Network_Firewall_Template object. You can retrieve all available firewall templates. getAllObjects returns an array of all available SoftLayer_Network_Firewall_Template objects. You can use these templates to generate a [[SoftLayer Network Firewall Update Request]]. 

@SLDNDocumentation Service See Also SoftLayer_Network_Firewall_Update_Request "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Firewall_Template"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Firewall_Template"
---

# [REST Example](#getObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Firewall_Template/{SoftLayer_Network_Firewall_TemplateID}/getObject'
```
