---
title: "requestGlobalFundedAccount"
description: "Allows authorized IBMer's to apply for a proof of concept account using global funding. Requests will be reviewed by multiple internal teams before an account is created. 

Note that the proof of concept system is for internal IBM employees only and is not applicable to users outside the IBM organization. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_ProofOfConcept"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account_ProofOfConcept"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Container_Account_ProofOfConcept_Request_GlobalFunded]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_ProofOfConcept/requestGlobalFundedAccount'
```
