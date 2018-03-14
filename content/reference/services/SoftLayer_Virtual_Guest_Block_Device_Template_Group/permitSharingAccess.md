---
title: "permitSharingAccess"
description: "This method will permit another SoftLayer customer account access to provision CloudLayer Computing Instances from an im... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
aliases:
    - "/reference/services/softlayer_virtual_guest_block_device_template_group/permitSharingAccess"
---
# [SoftLayer_Virtual_Guest_Block_Device_Template_Group](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group)::permitSharingAccess

Permit another SoftLayer customer account access to provision CloudLayer Computing Instances from an image template group. Template access should only be given to the parent template group object, not the child. 


## Overview 
This method will permit another SoftLayer customer account access to provision CloudLayer Computing Instances from an image template group. Template access should only be given to the parent template group object, not the child. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|accountId| integer| The account id that you wish to share an image template group with.|


### Required Headers
* authenticate
* SoftLayer_Virtual_Guest_Block_Device_Template_GroupInitParameters

### Optional Headers

### Return Values
boolean

