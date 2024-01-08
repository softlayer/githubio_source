---
title: "requestManualEnrollment"
description: ""
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Catalyst"
classes:
    - "SoftLayer_Catalyst_Enrollment"
type: "reference"
layout: "method"
mainService : "SoftLayer_Catalyst_Enrollment"
---

### [REST Example](#requestManualEnrollment-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#requestManualEnrollment-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Container_Catalyst_ManualEnrollmentRequest]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Catalyst_Enrollment/requestManualEnrollment'
```
