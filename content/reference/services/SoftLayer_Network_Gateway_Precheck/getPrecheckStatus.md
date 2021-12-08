---
title: "getPrecheckStatus"
description: "Get the precheck status for all Juniper Gateway Action categories which require a readiness check before executing. Refe... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Gateway_Precheck"
aliases:
    - "/reference/services/softlayer_network_gateway_precheck/getPrecheckStatus"
---
# [SoftLayer_Network_Gateway_Precheck](/reference/services/SoftLayer_Network_Gateway_Precheck)::getPrecheckStatus


Get Precheck status for Gateway


## Overview 
Get the precheck status for all Juniper Gateway Action categories which require a readiness check before executing. Reference cloud.ibm.com documentation for more details. 

Possible precheck readiness values include: 

Ready (0): The member or Gateway category is ready. The only state that will be allowed to execute the Action. Not Ready (1): The member or Gateway category is not ready. This could occur because of several reasons. Either a precheck error occur, or the precheck has not run within the precheck timeout window. Check the returnCode for details on the specific error. Reference the cloud.ibm.com documentation for recovery details. Running (2): The precheck is currently running with no errors. Incomplete (3): The other member in the Gateway failed, therefore the current member could not complete it's precheck. Unsupported (4): The category is unsupported for the given member or Gateway. Expired (5) : The precheck record has expired so will need to be run again. Unchecked (6) : The precheck for the category has never been run. Current (7) : The gateway state is current so running precheck is not required.  This commonly relates to version upgrade if gateway is in most update version. 

Return Values: Array of objects 

Object Definition: 

category : String : The precheck category which corresponds to one or more executeable actions. 

Current categories include: upgrade_precheck : Required for major and minor upgrade version actions. license_precheck : Required for license upgrade and downgrade actions. reload_precheck : Required for OS Reload action. rollback_precheck : Optional and related to upgrade_precheck.  Only returned if getRollbackPrecheck is provided and set to True (1). 



memberId : Integer : The softlayer member id. memberReadinessValue : String : The precheck readiness state for the member. See possible readiness values above. gatewayReadinessValue : String : The precheck readiness state for the gateway : See possible readiness values above. returnCode : Integer : The return code. 0 if no error. Reference cloud.ibm.com documentation for details. 



-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|gatewayId| integer| Id of Gateway for the precheck request.|
|getRollbackPrecheck| boolean| [optional] [default false] If true, then rollback precheck will be included in returned data.|


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_Network_Gateway_PrecheckObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Network_Gateway_Precheck'>SoftLayer_Network_Gateway_Precheck[] </a>




