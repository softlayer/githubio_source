---
title: "createCustomerAccount"
description: "Create a new customer account record. By default, the newly created account will be associated to a platform (PaaS) account. To skip the automatic creation and linking to a new platform account, set the <em>bluemixLinkedFlag</em> to <strong>false</strong> on the account template. "
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

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Account, boolean]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Brand/createCustomerAccount'
```
