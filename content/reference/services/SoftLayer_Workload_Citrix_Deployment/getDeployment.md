---
title: "getDeployment"
description: "Returns a response object [SoftLayer_Workload_Citrix_Deployment_Response]({{<ref 'reference/datatypes/SoftLayer_Workload... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "Workload"
classes:
    - "SoftLayer_Workload_Citrix_Deployment"
aliases:
    - "/reference/services/softlayer_workload_citrix_deployment/getDeployment"
---
# [SoftLayer_Workload_Citrix_Deployment](/reference/services/SoftLayer_Workload_Citrix_Deployment)::getDeployment





## Overview 
Returns a response object [SoftLayer_Workload_Citrix_Deployment_Response]({{<ref "reference/datatypes/SoftLayer_Workload_Citrix_Deployment_Response">}}) which represents the CVAD deployment [SoftLayer_Workload_Citrix_Deployment]({{<ref "reference/datatypes/SoftLayer_Workload_Citrix_Deployment">}}) together with all the resources ordered under the CVAD order. 

The deployment resources are represented by object [SoftLayer_Workload_Citrix_Deployment_Resource_Response]({{<ref "reference/datatypes/SoftLayer_Workload_Citrix_Deployment_Resource_Response">}}). 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|deploymentId| integer| |


### Required Headers
* authenticate


### Optional Headers
* SoftLayer_Workload_Citrix_DeploymentObjectMask
* SoftLayer_ObjectMask

### Return Values
* <a href='/reference/datatypes/SoftLayer_Workload_Citrix_Deployment_Response'>SoftLayer_Workload_Citrix_Deployment_Response </a>




