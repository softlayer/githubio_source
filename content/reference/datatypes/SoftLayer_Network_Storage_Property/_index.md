---
title: "SoftLayer_Network_Storage_Property"
description: "A property provides additional information about a volume which it is assigned to. This information can range from 'Moun... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Property"
---

# SoftLayer_Network_Storage_Property
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Storage_Property' >Datatype</a></li>
    </ul>
</div>

## Description 
A property provides additional information about a volume which it is assigned to. This information can range from "Mountable" flags to utilized snapshot space. 





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
[createDate]: #createdate
#### [createDate]
The date a property was created.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date a property was last modified;  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[value]: #value
#### [value]
The value of a property.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[volumeId]: #volumeid
#### [volumeId]
The volume id which a property is associated with.  
<span class="type-label">Type: </span>**integer**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[type]: #type
#### [type]
The type provides a standardized definition for a property.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Property_Type'>SoftLayer_Network_Storage_Property_Type </a>**


</div>
<div class="prop-row">

-----
[volume]: #volume
#### [volume]
The associated volume for a property.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage </a>**


</div>

## Count
</div>


