---
title: "updateReferencedRegistrations"
description: "This method will create a bulk transaction to update any registrations that reference this detail object. It should only... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Regional_Registry_Detail"
aliases:
    - "/reference/services/softlayer_account_regional_registry_detail/updateReferencedRegistrations"
---
# [SoftLayer_Account_Regional_Registry_Detail](/reference/services/SoftLayer_Account_Regional_Registry_Detail)::updateReferencedRegistrations

Create a transaction to update the registrations that reference this detail object.


## Overview 
This method will create a bulk transaction to update any registrations that reference this detail object. It should only be called from a child class such as [[SoftLayer_Account_Regional_Registry_Detail_Person]] or [[SoftLayer_Account_Regional_Registry_Detail_Network]]. The registrations should be in the Open or Registration_Complete status. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Account_Regional_Registry_DetailInitParameters


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Network_Subnet_Registration_TransactionDetails'>SoftLayer_Container_Network_Subnet_Registration_TransactionDetails </a>




