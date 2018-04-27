---
title: "requestGlobalFundedAccount"
description: "Allows authorized IBMer's to apply for a proof of concept account using global funding. Requests will be reviewed by mul... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_ProofOfConcept"
aliases:
    - "/reference/services/softlayer_account_proofofconcept/requestGlobalFundedAccount"
---
# [SoftLayer_Account_ProofOfConcept](/reference/services/SoftLayer_Account_ProofOfConcept)::requestGlobalFundedAccount

Accepts new proof of concept requests


## Overview 
Allows authorized IBMer's to apply for a proof of concept account using global funding. Requests will be reviewed by multiple internal teams before an account is created. 

Note that the proof of concept system is for internal IBM employees only and is not applicable to users outside the IBM organization. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|request| <a href='/reference/datatypes/SoftLayer_Container_Account_ProofOfConcept_Request_GlobalFunded'>SoftLayer_Container_Account_ProofOfConcept_Request_GlobalFunded </a>| |


### Required Headers
* authenticate

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Account_ProofOfConcept_Review_Summary'>SoftLayer_Container_Account_ProofOfConcept_Review_Summary </a>

