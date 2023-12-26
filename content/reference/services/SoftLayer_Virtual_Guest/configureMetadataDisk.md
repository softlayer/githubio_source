---
title: "configureMetadataDisk"
description: "Creates a transaction to configure the guest's metadata disk. If the guest has user data associated with it, the transaction will create a small virtual drive and write the metadata to a file on the drive; if the drive already exists, the metadata will be rewritten. If the guest has no user data associated with it, the transaction will remove the virtual drive if it exists. 

WARNING: The transaction created by this service will shut down the guest while the metadata disk is configured. The guest will be turned back on once this process is complete. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
type: "reference"
layout: "method"
mainService : "SoftLayer_Virtual_Guest"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest/{SoftLayer_Virtual_GuestID}/configureMetadataDisk'
```
