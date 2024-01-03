---
title: "setAuthenticationCode"
description: "The setAuthenticationCode method sets the authentication code for the domain. The authentication code is a transfer key and provides an extra level of security, safeguarding domain names from unauthorized transfers. "
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

# [REST Example](#setAuthenticationCode-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#setAuthenticationCode-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Dns_Domain_Registration/{SoftLayer_Dns_Domain_RegistrationID}/setAuthenticationCode'
```
