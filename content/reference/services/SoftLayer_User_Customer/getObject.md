---
title: "getObject"
description: "getObject retrieves the SoftLayer_User_Customer object whose ID number corresponds to the ID number of the init parameter passed to the SoftLayer_User_Customer service. You can only retrieve users that are assigned to the customer account belonging to the user making the API call. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer"
type: "reference"
layout: "method"
mainService : "SoftLayer_User_Customer"
---

# [REST Example](#getObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer/{SoftLayer_User_CustomerID}/getObject'
```
