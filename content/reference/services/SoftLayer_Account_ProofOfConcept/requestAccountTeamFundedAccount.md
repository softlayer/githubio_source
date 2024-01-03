---
title: "requestAccountTeamFundedAccount"
description: "Allows authorized IBMer's to apply for a proof of concept account using account team funding. Requests will be reviewed by multiple internal teams before an account is created. 

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

# [REST Example](#requestAccountTeamFundedAccount-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#requestAccountTeamFundedAccount-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Container_Account_ProofOfConcept_Request_AccountFunded]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_ProofOfConcept/requestAccountTeamFundedAccount'
```
