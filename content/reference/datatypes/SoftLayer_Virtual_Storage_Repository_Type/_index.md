---
title: "SoftLayer_Virtual_Storage_Repository_Type"
description: "SoftLayer employs many different types of repositories that computing instances use as their storage volume. SoftLayer_V... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Storage_Repository_Type"
---

# SoftLayer_Virtual_Storage_Repository_Type
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Virtual_Storage_Repository_Type' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer employs many different types of repositories that computing instances use as their storage volume. SoftLayer_Virtual_Storage_Repository_Type models a single storage type. Common types of storage repositories include networked file systems, logical volume management, and local disk volumes for swap and page file management. 





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
[description]: #description
#### [description]
A brief description os a storage repository type.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
A storage repository type's name.  
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[storageRepositories]: #storagerepositories
#### [storageRepositories]
The storage repositories on a SoftLayer customer account that belong to this type.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Storage_Repository'>SoftLayer_Virtual_Storage_Repository[] </a>**


</div>

## Count
<div class="prop-row">

-----
[storageRepositoryCount]: #storagerepositorycount
#### [storageRepositoryCount]
A count of the storage repositories on a SoftLayer customer account that belong to this type.   
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


