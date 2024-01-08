---
title: "createObject"
description: "<style type='text/css'>.create_object > li > div { padding-top: .5em; padding-bottom: .5em}</style> This method will create a new SoftLayer_Network_Subnet_Registration_Details object. 

<b>Input</b> - [SoftLayer_Network_Subnet_Registration_Details](/reference/datatypes/SoftLayer_Network_Subnet_Registration_Details) <ul class='create_object'> <li><code>detailId</code> <div> The numeric ID of the [SoftLayer_Account_Regional_Registry_Detail](/reference/datatypes/SoftLayer_Account_Regional_Registry_Detail) object to relate. </div> <ul> <li><b>Required</b></li> <li><b>Type</b> - integer</li> </ul> </li> <li><code>registrationId</code> <div> The numeric ID of the [SoftLayer_Network_Subnet_Registration](/reference/datatypes/SoftLayer_Network_Subnet_Registration) object to relate. </div> <ul> <li><b>Required</b></li> <li><b>Type</b> - integer</li> </ul> </li> </ul> "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet_Registration_Details"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Subnet_Registration_Details"
---

### [REST Example](#createObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#createObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_Subnet_Registration_Details]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Subnet_Registration_Details/createObject'
```
