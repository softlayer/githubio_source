---
title: "manageLicenses"
description: "Used to manage gateway require and add on licenses.  If license request is valid for the gateway type a Gateway License Manage process will be created if licenses need to be adjusted on the gateway. 

requiredItemKeyname - Item Key Name of the required license to be used on the gateway addOnLicenses - Json string containing an Add On license Item Key Name and requested total quantity to exist on each gateway member.  Item Key Name must be associated with an Add On license product item and Item Key Name can only exist once in the json structure. 

Example : {'ADD_ON_ITEM_KEYNAME_TYPE1':3,'ADD_ON_ITEM_KEYNAME_TYPE2':4} 

Note, the quantity is not the requested change but total licences.  For example, if current licenses for an Add On e.g. Remote VPN is 3 and the request is to add 1 more license then the quantity would be 4.  If the request was to remove 1 license then the quantity would be 2. 

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

### [REST Example](#manageLicenses-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#manageLicenses-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Gateway/{SoftLayer_Network_GatewayID}/manageLicenses'
```
