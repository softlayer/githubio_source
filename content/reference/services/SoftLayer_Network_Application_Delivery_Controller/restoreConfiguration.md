---
title: "restoreConfiguration"
description: "Restore an application delivery controller's configuration state."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Application_Delivery_Controller"
---
# SoftLayer_Network_Application_Delivery_Controller::restoreConfiguration
## Overview 
Restore an application delivery controller's configuration state. 

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|configurationHistoryId| integer| The id of a SoftLayer_Network_Application_Delivery_Controller_Configuration_History record to restore.|


### Required Headers
* authenticate
* SoftLayer_Network_Application_Delivery_ControllerInitParameters

### Optional Headers

### Return Values
boolean


### associatedMethods

*  [SoftLayer_Network_Application_Delivery_Controller::getConfigurationHistory](/reference/services/SoftLayer_Network_Application_Delivery_Controller/getConfigurationHistory )
*  [SoftLayer_Network_Application_Delivery_Controller::saveCurrentConfiguration](/reference/services/SoftLayer_Network_Application_Delivery_Controller/saveCurrentConfiguration )
*  [SoftLayer_Network_Application_Delivery_Controller::restoreBaseConfiguration](/reference/services/SoftLayer_Network_Application_Delivery_Controller/restoreBaseConfiguration )

