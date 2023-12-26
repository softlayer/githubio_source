---
title: "getEncryptionOptions"
description: "Encryption options available for both phases of the negotiation process. 

The valid encryption options are as follows: 
* DES
* 3DES
* AES128
* AES192
* AES256"
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Tunnel_Module_Context"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Tunnel_Module_Context"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Tunnel_Module_Context/getEncryptionOptions'
```
