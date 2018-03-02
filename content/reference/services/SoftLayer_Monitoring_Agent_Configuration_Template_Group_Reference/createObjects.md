---
title: "createObjects"
description: "This method creates monitoring agent configuration template group references by passing in an array of objects with the... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Monitoring"
classes:
    - "SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference"
---
# SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference::createObjects
## Overview 
This method creates monitoring agent configuration template group references by passing in an array of objects with the SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference structure as the $templateObjects parameter. Setting the $bulkCommit parameter to true will commit the changes in one transaction, false will commit after each object is created. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObjects| <a href='/reference/datatypes/SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference'>SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference[] </a>| An array of SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference objects that you wish to create.|


### Required Headers
* authenticate

### Optional Headers

### Return Values
boolean


### associatedMethods

*  [SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference::createObject ](/reference/services/SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference/createObject  )
*  [SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference::getObject ](/reference/services/SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference/getObject  )
*  [SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference::getAllObjects ](/reference/services/SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference/getAllObjects  )
*  [SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference::editObject ](/reference/services/SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference/editObject  )
*  [SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference::editObjects ](/reference/services/SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference/editObjects  )

