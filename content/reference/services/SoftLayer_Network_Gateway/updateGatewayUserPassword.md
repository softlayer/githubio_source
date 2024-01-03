---
title: "updateGatewayUserPassword"
description: "The method updates the Gateway password for the provided username.  It does not perform any synchronization with the Gateway to update the credentials.  The method only updates the IMS db with the username / password record for the Gateway. 

The 'username' and 'password' in the record template are required. 'username' must not be blank and must exist in the Gateway password records 'password' must not be blank 

Returns true if password change is successful, false if not successful 

"
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Gateway"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Gateway"
---

# [REST Example](#updateGatewayUserPassword-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#updateGatewayUserPassword-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_Gateway_Member_Passwords]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Gateway/{SoftLayer_Network_GatewayID}/updateGatewayUserPassword'
```
