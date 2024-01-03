---
title: "getObject"
description: "getObject retrieves the SoftLayer_Network_Application_Delivery_Controller object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_Network_Application_Delivery_Controller service. You can only retrieve application delivery controllers that are associated with your SoftLayer customer account. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Application_Delivery_Controller"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Application_Delivery_Controller"
---

# [REST Example](#getObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Application_Delivery_Controller/{SoftLayer_Network_Application_Delivery_ControllerID}/getObject'
```
