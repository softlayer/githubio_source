---
title: "getRegistrantVerificationStatusDetail"
description: "When a domain is registered or transferred, or when the registrant contact information is changed, the registrant must reply to an email requesting them to confirm that the submitted contact information is correct. This method returns the current state of the verification request. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Dns"
classes:
    - "SoftLayer_Dns_Domain_Registration"
type: "reference"
layout: "method"
mainService : "SoftLayer_Dns_Domain_Registration"
---

### [REST Example](#getRegistrantVerificationStatusDetail-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getRegistrantVerificationStatusDetail-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Dns_Domain_Registration/{SoftLayer_Dns_Domain_RegistrationID}/getRegistrantVerificationStatusDetail'
```
