---
title: "SoftLayer_Workload_Citrix_Deployment"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Workload"
classes:
    - "SoftLayer_Workload_Citrix_Deployment"
---

# SoftLayer_Workload_Citrix_Deployment
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Workload_Citrix_Deployment' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Workload_Citrix_Deployment' >Datatype</a></li>
    </ul>
</div>

## Description 






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
Topology used for the Citrix Virtual Apps And  Desktop deployment.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
The date when this record was created.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
It is the unique identifier for the deployment.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date when this record was last modified.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[typeId]: #typeid
#### [typeId]
The [SoftLayer_Workload_Citrix_Deployment_Type]({{<ref "reference/datatypes/SoftLayer_Workload_Citrix_Deployment_Type">}}) of the deployment.  
<span class="type-label">Type: </span>**integer**


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

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[account]: #account
#### [account]
The [SoftLayer_Account]({{<ref "reference/datatypes/SoftLayer_Account">}}) to which the deployment belongs.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**


</div>
<div class="prop-row">

-----
[resources]: #resources
#### [resources]
It contains a collection of items under the CVAD deployment.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Workload_Citrix_Deployment_Resource'>SoftLayer_Workload_Citrix_Deployment_Resource[] </a>**


</div>
<div class="prop-row">

-----
[type]: #type
#### [type]
It shows if the deployment is for Citrix Hypervisor or VMware.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Workload_Citrix_Deployment_Type'>SoftLayer_Workload_Citrix_Deployment_Type </a>**


</div>
<div class="prop-row">

-----
[user]: #user
#### [user]
It is the [SoftLayer_User_Customer]({{<ref "reference/datatypes/SoftLayer_User_Customer">}}) who placed the order for CVAD.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**


</div>
<div class="prop-row">

-----
[vlan]: #vlan
#### [vlan]
It is the VLAN resource for the CVAD deployment.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan </a>**


</div>

## Count
<div class="prop-row">

-----
[resourceCount]: #resourcecount
#### [resourceCount]
A count of it contains a collection of items under the CVAD deployment.   
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


