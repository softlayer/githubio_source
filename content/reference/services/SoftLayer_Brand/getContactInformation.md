---
title: "getContactInformation"
description: "Retrieve the contact information for the brand such as the corporate or support contact.  This will include the contact name, telephone number, fax number, email address, and mailing address of the contact. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Brand"
classes:
    - "SoftLayer_Brand"
type: "reference"
layout: "method"
mainService : "SoftLayer_Brand"
---

### [REST Example](#getContactInformation-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getContactInformation-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Brand/{SoftLayer_BrandID}/getContactInformation'
```
