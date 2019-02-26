---
title: "editObjects"
description: "This method updates a set of SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference records by passing in an... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Monitoring"
classes:
    - "SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference"
aliases:
    - "/reference/services/softlayer_monitoring_agent_configuration_template_group_reference/editObjects"
---
# [SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference](/reference/services/SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference)::editObjects

Update template group references by passing in an array of modified instances of the objects. 


## Overview 
This method updates a set of SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference records by passing in an array of modified instances of the objects. Setting the $bulkCommit parameter to true will commit the changes in one transaction, false will commit after each object is updated. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObjects| <a href='/reference/datatypes/SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference'>SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference[] </a>| An array of skeleton SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference objects with only the properties defined that you wish to change. Unchanged properties are left alone.|


### Required Headers
* authenticate


### Return Values
* boolean


### Associated Methods

*  [SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference::createObject ](/reference/services/SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference/createObject  )
*  [SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference::createObjects ](/reference/services/SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference/createObjects  )
*  [SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference::getObject ](/reference/services/SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference/getObject  )
*  [SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference::getAllObjects ](/reference/services/SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference/getAllObjects  )
*  [SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference::editObject ](/reference/services/SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference/editObject  )




