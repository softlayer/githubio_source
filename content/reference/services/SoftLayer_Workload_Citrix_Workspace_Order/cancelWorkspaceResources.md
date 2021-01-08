---
title: "cancelWorkspaceResources"
description: "This method will cancel the resources associated with the provided VLAN and have a 'cvad' tag reference."
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Workload"
classes:
    - "SoftLayer_Workload_Citrix_Workspace_Order"
aliases:
    - "/reference/services/softlayer_workload_citrix_workspace_order/cancelWorkspaceResources"
---
# [SoftLayer_Workload_Citrix_Workspace_Order](/reference/services/SoftLayer_Workload_Citrix_Workspace_Order)::cancelWorkspaceResources

Cancel the orders associated with resources on the provided VLAN


## Overview 
This method will cancel the resources associated with the provided VLAN and have a 'cvad' tag reference. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|vlanIdentifier| string| The name, id or identifier (mex09.bcr22.1157) for the vlan.|
|cancelImmediately| boolean| This will trigger an immediate cancellation with a reclaim of the resource.|
|customerNote| string| Tracks any additional information that the customer wanted to provide.|


### Required Headers
* authenticate


### Return Values
* <a href='/reference/datatypes/SoftLayer_Workload_Citrix_Workspace_Response_Result'>SoftLayer_Workload_Citrix_Workspace_Response_Result </a>




