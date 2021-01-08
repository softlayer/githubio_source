---
title: "getWorkspaceResources"
description: "This method will return the list of resources which could be cancelled using cancelWorkspaceResources"
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Workload"
classes:
    - "SoftLayer_Workload_Citrix_Workspace_Order"
aliases:
    - "/reference/services/softlayer_workload_citrix_workspace_order/getWorkspaceResources"
---
# [SoftLayer_Workload_Citrix_Workspace_Order](/reference/services/SoftLayer_Workload_Citrix_Workspace_Order)::getWorkspaceResources

List the orders associated with resources on the provided VLAN


## Overview 
This method will return the list of resources which could be cancelled using cancelWorkspaceResources 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|vlanIdentifier| string| The name, id or identifier (e.g. mex09.bcr22.1157) for the vlan.|


### Required Headers
* authenticate


### Return Values
* <a href='/reference/datatypes/SoftLayer_Workload_Citrix_Workspace_Response_Result'>SoftLayer_Workload_Citrix_Workspace_Response_Result </a>




