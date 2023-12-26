---
title: "getObject"
description: "getObject method retrieves the SoftLayer_Network_Media_Transcode_Account object whose ID number corresponds to the ID number of the initial parameter passed to the SoftLayer_Network_Media_Transcode_Account service. You can only retrieve a Transcode account assigned to your SoftLayer customer account. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Media_Transcode_Account"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Media_Transcode_Account"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Media_Transcode_Account/{SoftLayer_Network_Media_Transcode_AccountID}/getObject'
```
