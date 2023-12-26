---
title: "updateAntivirusSpywarePolicy"
description: "Update an anti-virus/spyware policy. The policy options that it accepts are the following: 
*1 - Minimal
*2 - Relaxed
*3 - Default
*4 - High
*5 - Ultimate"
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Software"
classes:
    - "SoftLayer_Software_Component_AntivirusSpyware"
type: "reference"
layout: "method"
mainService : "SoftLayer_Software_Component_AntivirusSpyware"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, boolean]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Software_Component_AntivirusSpyware/{SoftLayer_Software_Component_AntivirusSpywareID}/updateAntivirusSpywarePolicy'
```
