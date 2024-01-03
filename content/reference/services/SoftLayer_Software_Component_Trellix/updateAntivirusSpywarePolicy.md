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
    - "SoftLayer_Software_Component_Trellix"
type: "reference"
layout: "method"
mainService : "SoftLayer_Software_Component_Trellix"
---

# [REST Example](#updateAntivirusSpywarePolicy-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#updateAntivirusSpywarePolicy-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, boolean]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Software_Component_Trellix/{SoftLayer_Software_Component_TrellixID}/updateAntivirusSpywarePolicy'
```
