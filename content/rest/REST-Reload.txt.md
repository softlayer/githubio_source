---
title: "REST-Reload.txt"
description: "REST-Reload.txt"
date: "2017-11-23"
classes: 
    - "SoftLayer_Hardware_Server"
tags:
    - "baremetalservers"
---


```
URL : https://$USERNAME:$APIKEY@api.softlayer.com/rest/v3/SoftLayer_Hardware_Server/$ServerID/reloadOperatingSystem.json

Method: POST

JSON: {
    "parameters": [
        "FORCE",
        {
            "itemPrices": [
                {
                    "id": $OSPriceID
                }
            ]
        }
    ]
}
```
