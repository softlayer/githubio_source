---
title: "SoftLayer_Layout_Profile_Containers"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Layout"
classes:
    - "SoftLayer_Layout_Profile_Containers"
---

# SoftLayer_Layout_Profile_Containers
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Layout_Profile_Containers' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Layout_Profile_Containers' >Datatype</a></li>
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
[createDate]: #createdate
#### [createDate]
Timestamp of when the reference was created  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
The internal identifier of the container reference  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[layoutContainerId]: #layoutcontainerid
#### [layoutContainerId]
The id of the referenced [SoftLayer_Layout_Container]({{<ref "reference/datatypes/SoftLayer_Layout_Container">}})  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[layoutProfileId]: #layoutprofileid
#### [layoutProfileId]
The id of the referenced [SoftLayer_Layout_Profile]({{<ref "reference/datatypes/SoftLayer_Layout_Profile">}})  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
Timestamp of when the reference was last updated  
<span class="type-label">Type: </span>**dateTime**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[layoutContainerType]: #layoutcontainertype
#### [layoutContainerType]
The container to be contained  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Layout_Container'>SoftLayer_Layout_Container </a>**


</div>
<div class="prop-row">

-----
[layoutProfile]: #layoutprofile
#### [layoutProfile]
The profile containing this container  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Layout_Profile'>SoftLayer_Layout_Profile </a>**


</div>

## Count
</div>


