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
---
# SoftLayer_Account_Regional_Registry_Detail::updateReferencedRegistrations
## Overview 
This method will create a bulk transaction to update any registrations that reference this detail object. It should only be called from a child class such as [[SoftLayer_Account_Regional_Registry_Detail_Person]] or [[SoftLayer_Account_Regional_Registry_Detail_Network]]. The registrations should be in the Open or Registration_Complete status. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers
* authenticate
* SoftLayer_Account_Regional_Registry_DetailInitParameters

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Network_Subnet_Registration_TransactionDetails'>SoftLayer_Container_Network_Subnet_Registration_TransactionDetails </a>
