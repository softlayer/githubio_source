---
title: "SoftLayer_Workload_Citrix_Deployment_Resource"
description: "The SoftLayer_Workload_Citrix_Deployment_Resource type contains the information of the resource such as the Deployment I... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Workload"
classes:
    - "SoftLayer_Workload_Citrix_Deployment_Resource"
---

# SoftLayer_Workload_Citrix_Deployment_Resource
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Workload_Citrix_Deployment_Resource' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Workload_Citrix_Deployment_Resource' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_Workload_Citrix_Deployment_Resource type contains the information of the resource such as the Deployment ID, resource's Billing Item ID, Order ID and Role of the resource in the CVAD deployment. 





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
[billingItemId]: #billingitemid
#### [billingItemId]
Billing item ID of the resource  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
The point in time at which the resource was ordered.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[deploymentId]: #deploymentid
#### [deploymentId]
CVAD Deployment ID of the resource  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
Unique Identifier of the CVAD Deployment Resource  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
The last time when the resource was modified.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[orderId]: #orderid
#### [orderId]
Billing Order ID of the resource  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[orderedByCvad]: #orderedbycvad
#### [orderedByCvad]
This flag indicates that whether the CVAD APIs have control over this resource. This resource can be cancelled using CVAD cancellation APIs only if this flag is true.   
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[roleId]: #roleid
#### [roleId]
Role of the resource within the CVAD deployment. For example, a VSI can have different roles such as Proxy Server or DHCP Server.   
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[billingItem]: #billingitem
#### [billingItem]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a>**  



</div>
<div class="prop-row">

-----
[deployment]: #deployment
#### [deployment]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Workload_Citrix_Deployment'>SoftLayer_Workload_Citrix_Deployment </a>**  



</div>
<div class="prop-row">

-----
[order]: #order
#### [order]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Order'>SoftLayer_Billing_Order </a>**  



</div>
<div class="prop-row">

-----
[role]: #role
#### [role]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Workload_Citrix_Deployment_Resource_Role'>SoftLayer_Workload_Citrix_Deployment_Resource_Role </a>**  



</div>

## Count
</div>


