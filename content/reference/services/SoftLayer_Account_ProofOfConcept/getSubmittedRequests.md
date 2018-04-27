---
title: "getSubmittedRequests"
description: "Allows authorized IBMer to retrieve a list summarizing all previously submitted proof of concept requests. 

Note that t... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_ProofOfConcept"
aliases:
    - "/reference/services/softlayer_account_proofofconcept/getSubmittedRequests"
---
# [SoftLayer_Account_ProofOfConcept](/reference/services/SoftLayer_Account_ProofOfConcept)::getSubmittedRequests

Retrieves a summary of proof of concept requests submitted by an IBMer.


## Overview 
Allows authorized IBMer to retrieve a list summarizing all previously submitted proof of concept requests. 

Note that the proof of concept system is for internal IBM employees only and is not applicable to users outside the IBM organization. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|email| string| |
|sortOrder| string| |


### Required Headers
* authenticate

### Optional Headers
* resultLimit

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Account_ProofOfConcept_Review_Summary'>SoftLayer_Container_Account_ProofOfConcept_Review_Summary[] </a>

