---
title: "getProvisionState"
description: "The getProvisionState method retrieves the provision state of the resource. The provision state may be used to determine... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Resource"
classes:
    - "SoftLayer_Resource_Metadata"
aliases:
    - "/reference/services/softlayer_resource_metadata/getProvisionState"
---
# [SoftLayer_Resource_Metadata](/reference/services/SoftLayer_Resource_Metadata)::getProvisionState

Obtain the provision state for a resource


## Overview 
The getProvisionState method retrieves the provision state of the resource. The provision state may be used to determine when it is considered safe to perform additional setup operations. The method returns 'PROCESSING' to indicate the provision is in progress and 'COMPLETE' when the provision is complete. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |


### Required Headers

### Optional Headers

### Return Values
string

