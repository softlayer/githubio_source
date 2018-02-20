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
---
# SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference::editObjects
## Overview 
This method updates a set of SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference records by passing in an array of modified instances of the objects. Setting the $bulkCommit parameter to true will commit the changes in one transaction, false will commit after each object is updated. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|templateObjects| <a href='/reference/datatypes/SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference'>SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference[] </a>| An array of skeleton SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference objects with only the properties defined that you wish to change. Unchanged properties are left alone.|


### Required Headers
* authenticate

### Optional Headers

### Return Values
boolean
