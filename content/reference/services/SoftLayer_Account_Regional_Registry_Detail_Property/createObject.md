---
title: "createObject"
description: "<style type='text/css'>.create_object > li > div { padding-top: .5em; padding-bottom: .5em}</style> This method will cre... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Regional_Registry_Detail_Property"
aliases:
    - "/reference/services/softlayer_account_regional_registry_detail_property/createObject"
---
# [SoftLayer_Account_Regional_Registry_Detail_Property](/reference/services/SoftLayer_Account_Regional_Registry_Detail_Property)::createObject

Create a new property object


## Overview 
<style type="text/css">.create_object > li > div { padding-top: .5em; padding-bottom: .5em}</style> This method will create a new SoftLayer_Account_Regional_Registry_Detail_Property object. 

<b>Input</b> - [[SoftLayer_Account_Regional_Registry_Detail_Property (type)|SoftLayer_Account_Regional_Registry_Detail_Property]] <ul class="create_object"> <li><code>registrationDetailId</code> <div>The numeric ID of the [[SoftLayer_Account_Regional_Registry_Detail|detail object]] this property belongs to</div> <ul> <li><b>Required</b></li> <li><b>Type</b> - integer</li> </ul> </li> <li><code>propertyTypeId</code> <div> The numeric ID of the associated [[SoftLayer_Account_Regional_Registry_Detail_Property_Type]] object </div> <ul> <li><b>Required</b></li> <li><b>Type</b> - integer</li> </ul> </li> <li><code>sequencePosition</code> <div> When more than one property of the same type exists on a detail object, this value determines the position in that collection. This can be thought of more as a sort order. </div> <ul> <li><b>Required</b></li> <li><b>Type</b> - integer</li> </ul> </li> <li><code>value</code> <div> The actual value of the property. </div> <ul> <li><b>Required</b></li> <li><b>Type</b> - string</li> </ul> </li> </ul> 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Account_Regional_Registry_Detail_Property'>SoftLayer_Account_Regional_Registry_Detail_Property </a>| The SoftLayer_Account_Regional_Registry_Detail_Property object that you wish to create.|


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_Account_Regional_Registry_Detail_PropertyObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Account_Regional_Registry_Detail_Property'>SoftLayer_Account_Regional_Registry_Detail_Property </a>




