---
title: "SoftLayer_Layout_Profile_Customer"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Layout"
classes:
    - "SoftLayer_Layout_Profile_Customer"
---

# SoftLayer_Layout_Profile_Customer
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Layout_Profile_Customer' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Layout_Profile_Customer' >Datatype</a></li>
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
[activeFlag]: #activeflag
#### [activeFlag]
Active status of the layout profile  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
Timestamp of when the layout profile was created  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
The internal identifier of a layout profile  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
Timestamp of when the layout profile was last updated  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
The friendly name of the layout profile  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[userRecordId]: #userrecordid
#### [userRecordId]
The [SoftLayer_User_Customer]({{<ref "reference/datatypes/SoftLayer_User_Customer">}}) owning this layout profile  
<span class="type-label">Type: </span>**integer**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[layoutContainers]: #layoutcontainers
#### [layoutContainers]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Layout_Container'>SoftLayer_Layout_Container[] </a>**


</div>
<div class="prop-row">

-----
[layoutPreferences]: #layoutpreferences
#### [layoutPreferences]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Layout_Profile_Preference'>SoftLayer_Layout_Profile_Preference[] </a>**


</div>
<div class="prop-row">

-----
[userRecord]: #userrecord
#### [userRecord]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**


</div>

## Count
<div class="prop-row">

-----
[layoutContainerCount]: #layoutcontainercount
#### [layoutContainerCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[layoutPreferenceCount]: #layoutpreferencecount
#### [layoutPreferenceCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


