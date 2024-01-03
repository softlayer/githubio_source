---
title: "createObject"
description: "<style type='text/css'>.create_object > li > div { padding-top: .5em; padding-bottom: .5em}</style> This method will create a new SoftLayer_Account_Regional_Registry_Detail_Property object. 

<b>Input</b> - [SoftLayer_Account_Regional_Registry_Detail_Property](/reference/datatypes/SoftLayer_Account_Regional_Registry_Detail_Property) <ul class='create_object'> <li><code>registrationDetailId</code> <div>The numeric ID of the [SoftLayer_Account_Regional_Registry_Detail](/reference/datatypes/SoftLayer_Account_Regional_Registry_Detail) this property belongs to</div> <ul> <li><b>Required</b></li> <li><b>Type</b> - integer</li> </ul> </li> <li><code>propertyTypeId</code> <div> The numeric ID of the associated [SoftLayer_Account_Regional_Registry_Detail_Property_Type](/reference/datatypes/SoftLayer_Account_Regional_Registry_Detail_Property_Type) object </div> <ul> <li><b>Required</b></li> <li><b>Type</b> - integer</li> </ul> </li> <li><code>sequencePosition</code> <div> When more than one property of the same type exists on a detail object, this value determines the position in that collection. This can be thought of more as a sort order. </div> <ul> <li><b>Required</b></li> <li><b>Type</b> - integer</li> </ul> </li> <li><code>value</code> <div> The actual value of the property. </div> <ul> <li><b>Required</b></li> <li><b>Type</b> - string</li> </ul> </li> </ul> "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Regional_Registry_Detail_Property"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account_Regional_Registry_Detail_Property"
---

# [REST Example](#createObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#createObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Account_Regional_Registry_Detail_Property]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_Regional_Registry_Detail_Property/createObject'
```
