---
title: "getFlexibleCreditProgramsInfo"
description: "This method will return a [SoftLayer_Container_Account_Discount_Program_Collection]({{<ref 'reference/datatypes/SoftLaye... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
aliases:
    - "/reference/services/softlayer_account/getFlexibleCreditProgramsInfo"
---
# [SoftLayer_Account](/reference/services/SoftLayer_Account)::getFlexibleCreditProgramsInfo

This method retrieves information on all of your Flexible Credit Program enrollments for your account. 


## Overview 
This method will return a [SoftLayer_Container_Account_Discount_Program_Collection]({{<ref "reference/datatypes/SoftLayer_Container_Account_Discount_Program_Collection">}}) object containing information on all of the Flexible Credit Programs your account is enrolled in. To be considered an active participant, the account must have at least one enrollment record with a monthly credit amount set and the current date must be within the range defined by the enrollment and graduation date. The forNextBillCycle parameter can be set to true to return a SoftLayer_Container_Account_Discount_Program_Collection object with information with relation to the next bill cycle. The forNextBillCycle parameter defaults to false. Please note that all discount amount entries are reported as pre-tax amounts. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|nextBillingCycleFlag| boolean| Flag indicating whether the information in the container should be in the next bill cycle.|


### Required Headers
* authenticate


### Return Values
* <a href='/reference/datatypes/SoftLayer_Container_Account_Discount_Program_Collection'>SoftLayer_Container_Account_Discount_Program_Collection </a>


### Associated Methods

*  [SoftLayer_Product_Order::verifyOrder](/reference/services/SoftLayer_Product_Order/verifyOrder )




