---
title: "SoftLayer_Scale_Asset_Virtual_Guest"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Scale"
classes:
    - "SoftLayer_Scale_Asset_Virtual_Guest"
---

# SoftLayer_Scale_Asset_Virtual_Guest
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Scale_Asset_Virtual_Guest' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Scale_Asset_Virtual_Guest' >Datatype</a></li>
    </ul>
</div>

## Description 






<!-- Service Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Method Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Service Filer END -->

<div id="properties" class="content">
<div id="localProperties" class="prop-content" >

## Local
-----
[createDate]: #createdate
#### [createDate]
When this asset was created.  
<span class="type-label">Type: </span>**dateTime**

-----
[deleteFlag]: #deleteflag
#### [deleteFlag]
When set and true any edit that happens on this object, be it calling edit on this directly or setting as a child while editing a parent object, will end up being a deletion.   
<span class="type-label">Type: </span>**boolean**

-----
[id]: #id
#### [id]
An asset's internal identifier.  
<span class="type-label">Type: </span>**integer**

-----
[scaleGroupId]: #scalegroupid
#### [scaleGroupId]
The identifier of the group this asset belongs to.  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[scaleGroup]: #scalegroup
#### [scaleGroup]
The group this asset belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Scale_Group'>SoftLayer_Scale_Group </a>**

-----
[virtualGuest]: #virtualguest
#### [virtualGuest]
The guest for this asset.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest </a>**

-----
[virtualGuestId]: #virtualguestid
#### [virtualGuestId]
The identifier of the guest for this asset.  
<span class="type-label">Type: </span>**integer**


## Count
</div>


