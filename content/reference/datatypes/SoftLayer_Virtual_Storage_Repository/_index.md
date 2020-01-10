---
title: "SoftLayer_Virtual_Storage_Repository"
description: "The SoftLayer_Virtual_Storage_Repository represents a web based storage system that can be accessed through many types o... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Storage_Repository"
---

# SoftLayer_Virtual_Storage_Repository
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Virtual_Storage_Repository' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Virtual_Storage_Repository' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Virtual_Storage_Repository represents a web based storage system that can be accessed through many types of devices, interfaces, and other resources. 





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
[capacity]: #capacity
#### [capacity]
A storage repositories capacity measured in Giga-Bytes (GB)   
<span class="type-label">Type: </span>**float**


</div>
<div class="prop-row">

-----
[description]: #description
#### [description]
A storage repositories description that describes its purpose or contents   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
Unique ID for a storage repository.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
A storage repositories name that describes its purpose or contents   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[publicFlag]: #publicflag
#### [publicFlag]
  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[typeId]: #typeid
#### [typeId]
A storage repositories [SoftLayer_Virtual_Storage_Repository_Type]({{<ref "reference/datatypes/SoftLayer_Virtual_Storage_Repository_Type">}}) ID   
<span class="type-label">Type: </span>**integer**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[account]: #account
#### [account]
The [SoftLayer_Account]({{<ref "reference/datatypes/SoftLayer_Account">}}) that a storage repository belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**


</div>
<div class="prop-row">

-----
[billingItem]: #billingitem
#### [billingItem]
The current billing item for a storage repository.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a>**


</div>
<div class="prop-row">

-----
[datacenter]: #datacenter
#### [datacenter]
The datacenter that a virtual storage repository resides in.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**


</div>
<div class="prop-row">

-----
[diskImages]: #diskimages
#### [diskImages]
The [SoftLayer_Virtual_Disk_Image]({{<ref "reference/datatypes/SoftLayer_Virtual_Disk_Image">}}) that are in a storage repository. Disk images are the virtual hard drives for a virtual guest.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Disk_Image'>SoftLayer_Virtual_Disk_Image[] </a>**


</div>
<div class="prop-row">

-----
[guests]: #guests
#### [guests]
The computing instances that have disk images in a storage repository.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**


</div>
<div class="prop-row">

-----
[metricTrackingObject]: #metrictrackingobject
#### [metricTrackingObject]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object_Virtual_Storage_Repository'>SoftLayer_Metric_Tracking_Object_Virtual_Storage_Repository </a>**


</div>
<div class="prop-row">

-----
[publicImageBillingItem]: #publicimagebillingitem
#### [publicImageBillingItem]
The current billing item for a public storage repository.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a>**


</div>
<div class="prop-row">

-----
[type]: #type
#### [type]
A storage repository's [SoftLayer_Virtual_Storage_Repository_Type]({{<ref "reference/datatypes/SoftLayer_Virtual_Storage_Repository_Type">}}).  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Storage_Repository_Type'>SoftLayer_Virtual_Storage_Repository_Type </a>**


</div>

## Count
<div class="prop-row">

-----
[diskImageCount]: #diskimagecount
#### [diskImageCount]
A count of the [SoftLayer_Virtual_Disk_Image]({{<ref "reference/datatypes/SoftLayer_Virtual_Disk_Image">}}) that are in a storage repository. Disk images are the virtual hard drives for a virtual guest.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[guestCount]: #guestcount
#### [guestCount]
A count of the computing instances that have disk images in a storage repository.   
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


