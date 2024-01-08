---
title: "createObject"
description: "<style type='text/css'>.create_object > li > div { padding-top: .5em; padding-bottom: .5em}</style> This method will create a new SoftLayer_Account_Regional_Registry_Detail object. 

<b>Input</b> - [SoftLayer_Account_Regional_Registry_Detail](/reference/datatypes/SoftLayer_Account_Regional_Registry_Detail) <ul class='create_object'> <li><code>detailTypeId</code> <div>The [SoftLayer_Account_Regional_Registry_Detail_Type](/reference/datatypes/SoftLayer_Account_Regional_Registry_Detail_Type) of this detail object</div> <ul> <li><b>Required</b></li> <li><b>Type</b> - integer</li> </ul> </li> <li><code>regionalInternetRegistryHandleId</code> <div> The id of the [SoftLayer_Account_Rwhois_Handle](/reference/datatypes/SoftLayer_Account_Rwhois_Handle) object. This is only to be used for detailed registrations, where a subnet is registered to an organization. The associated handle will be required to be a valid organization object id at the relevant registry. In this case, the detail object will only be valid for the registry the organization belongs to. </div> <ul> <li><b>Optional</b></li> <li><b>Type</b> - integer</li> </ul> </li> </ul> "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Regional_Registry_Detail"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account_Regional_Registry_Detail"
---

### [REST Example](#createObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#createObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Account_Regional_Registry_Detail]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_Regional_Registry_Detail/createObject'
```
