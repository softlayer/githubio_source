---
title: "getFlexibleCreditProgramInfo"
description: "This method will return a [[SoftLayer_Container_Account_Discount_Program]] object containing the Flexible Credit Program... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
---
# SoftLayer_Account::getFlexibleCreditProgramInfo
## Overview 
This method will return a [[SoftLayer_Container_Account_Discount_Program]] object containing the Flexible Credit Program information for this account. To be considered an active participant, the account must have an enrollment record with a monthly credit amount set and the current date must be within the range defined by the enrollment and graduation date. The forNextBillCycle parameter can be set to true to return a SoftLayer_Container_Account_Discount_Program object with information with relation to the next bill cycle. The forNextBillCycle parameter defaults to false. Please note that all discount amount entries are reported as pre-tax amounts and the legacy tax fields in the [[SoftLayer_Container_Account_Discount_Program]] are deprecated. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|forNextBillCycle| boolean| <<< EOT|


### Required Headers
* authenticate

### Optional Headers

### Return Values
<a href='/reference/datatypes/SoftLayer_Container_Account_Discount_Program'>SoftLayer_Container_Account_Discount_Program </a>


### associatedMethods

*  [SoftLayer_Product_Order::verifyOrder](/reference/services/SoftLayer_Product_Order/verifyOrder )

