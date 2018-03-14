---
title: "getConfigurationGroups"
description: "This method retrieves an array of SoftLayer_Monitoring_Agent_Configuration_Template_Group objects that are available to... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Monitoring"
classes:
    - "SoftLayer_Monitoring_Agent_Configuration_Template_Group"
aliases:
    - "/reference/services/softlayer_monitoring_agent_configuration_template_group/getConfigurationGroups"
---
# [SoftLayer_Monitoring_Agent_Configuration_Template_Group](/reference/services/SoftLayer_Monitoring_Agent_Configuration_Template_Group)::getConfigurationGroups

retrieves agent package configuration templates available to your account.


## Overview 
This method retrieves an array of SoftLayer_Monitoring_Agent_Configuration_Template_Group objects that are available to the active user's account. The packageId parameter is not currently used. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|packageId| integer| Internal identifier of a monitoring package product.|


### Required Headers
* authenticate

### Optional Headers
* SoftLayer_Monitoring_Agent_Configuration_Template_GroupObjectMask
* SoftLayer_ObjectMask

### Return Values
<a href='/reference/datatypes/SoftLayer_Monitoring_Agent_Configuration_Template_Group'>SoftLayer_Monitoring_Agent_Configuration_Template_Group[] </a>


### associatedMethods

*  [SoftLayer_Monitoring_Agent_Configuration_Template_Group::getObject](/reference/services/SoftLayer_Monitoring_Agent_Configuration_Template_Group/getObject )
*  [SoftLayer_Monitoring_Agent_Configuration_Template_Group::getAllObjects ](/reference/services/SoftLayer_Monitoring_Agent_Configuration_Template_Group/getAllObjects  )
*  [SoftLayer_Monitoring_Agent_Configuration_Template_Group::createObject](/reference/services/SoftLayer_Monitoring_Agent_Configuration_Template_Group/createObject )
*  [SoftLayer_Monitoring_Agent_Configuration_Template_Group::editObject](/reference/services/SoftLayer_Monitoring_Agent_Configuration_Template_Group/editObject )

