---
title: "createObject"
description: "<style type='text/css'>.create_object > li > div { padding-top: .5em; padding-bottom: .5em}</style> This method will cre... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet_Registration"
---
# SoftLayer_Network_Subnet_Registration::createObject
## Overview 
<style type="text/css">.create_object > li > div { padding-top: .5em; padding-bottom: .5em}</style> This method will create a new SoftLayer_Network_Subnet_Registration object. 

<b>Input</b> - [[SoftLayer_Network_Subnet_Registration (type)|SoftLayer_Network_Subnet_Registration]] <ul class="create_object"> <li><code>networkIdentifier</code> <div> The base address of the [[SoftLayer_Network_Subnet|subnet]] being registered. This can be derived directly from the SoftLayer_Network_Subnet object's networkIdentifier property. </div> <ul> <li><b>Required</b></li> <li><b>Type</b> - string</li> </ul> </li> <li><code>cidr</code> <div> The CIDR prefix of the [[SoftLayer_Network_Subnet|subnet]] being registered. This can be derived directly from the SoftLayer_Network_Subnet object's cidr property. </div> <ul> <li><b>Required</b></li> <li><b>Type</b> - integer</li> </ul> </li> </ul> 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObject| <a href='/reference/datatypes/SoftLayer_Network_Subnet_Registration'>SoftLayer_Network_Subnet_Registration </a>| The SoftLayer_Network_Subnet_Registration object that you wish to create.|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Network_Subnet_RegistrationObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Network_Subnet_Registration'>SoftLayer_Network_Subnet_Registration </a>

