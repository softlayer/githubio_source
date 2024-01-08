---
title: "lockDomain"
description: "The lockDomain method locks a domain to prevent unauthorized, unwanted or accidental changes to the domain name. When set, the following actions are prohibited: 
* Transferring of the domain name
* Deletion of the domain name"
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

### [REST Example](#lockDomain-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#lockDomain-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Dns_Domain_Registration/{SoftLayer_Dns_Domain_RegistrationID}/lockDomain'
```
