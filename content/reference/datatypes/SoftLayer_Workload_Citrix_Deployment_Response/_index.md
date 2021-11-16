---
title: "SoftLayer_Workload_Citrix_Deployment_Response"
description: "The SoftLayer_Workload_Citrix_Deployment_Response constructs a response object for the [SoftLayer_Workload_Citrix_Deploy... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Workload"
classes:
    - "SoftLayer_Workload_Citrix_Deployment_Response"
---

# SoftLayer_Workload_Citrix_Deployment_Response
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Workload_Citrix_Deployment_Response' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Workload_Citrix_Deployment_Response constructs a response object for the [SoftLayer_Workload_Citrix_Deployment]({{<ref "reference/datatypes/SoftLayer_Workload_Citrix_Deployment">}}) that includes all resources, i.e., [SoftLayer_Workload_Citrix_Deployment_Resource]({{<ref "reference/datatypes/SoftLayer_Workload_Citrix_Deployment_Resource">}}). 





<!-- Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Filer END -->

<div id="properties" class="content">
<div id="localProperties" class="prop-content" >

## Local
<div class="prop-row">

-----
[accountId]: #accountid
#### [accountId]
The account ID to which the deployment belongs.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[activeDirectoryTopology]: #activedirectorytopology
#### [activeDirectoryTopology]
Topology used for the CVAD deployment  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
The date when this deployment was created.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
ID of the CVAD deployment.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date when this deployment was modified.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[resources]: #resources
#### [resources]
It is a collection of objects representing deployment resources such as VLAN, subnet, bare metal, proxy, DHCP, cloud connectors.   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Workload_Citrix_Deployment_Resource_Response'>SoftLayer_Workload_Citrix_Deployment_Resource_Response[] </a>**


</div>
<div class="prop-row">

-----
[type]: #type
#### [type]
Represents if the deployment is for Citrix Hypervisor or VMware  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Workload_Citrix_Deployment_Type'>SoftLayer_Workload_Citrix_Deployment_Type </a>**


</div>
<div class="prop-row">

-----
[userRecordId]: #userrecordid
#### [userRecordId]
The identifier for the customer who placed the CVAD order.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[vlanId]: #vlanid
#### [vlanId]
VLAN ID of the deployment.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[vmwareOrderId]: #vmwareorderid
#### [vmwareOrderId]
It is an internal identifier for the VMware solution. It gets set if the CVAD order is for VMware.   
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


