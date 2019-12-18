---
title: "SoftLayer_Layout_Profile"
description: "The SoftLayer_Layout_Profile contains the definition of the layout profile"
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Layout"
classes:
    - "SoftLayer_Layout_Profile"
---

# SoftLayer_Layout_Profile
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Layout_Profile' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Layout_Profile' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Layout_Profile contains the definition of the layout profile 





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
[activeFlag]: #activeflag
#### [activeFlag]
Active status of the layout profile  
<span class="type-label">Type: </span>**integer**

-----
[createDate]: #createdate
#### [createDate]
Timestamp of when the layout profile was created  
<span class="type-label">Type: </span>**dateTime**

-----
[id]: #id
#### [id]
The internal identifier of a layout profile  
<span class="type-label">Type: </span>**integer**

-----
[modifyDate]: #modifydate
#### [modifyDate]
Timestamp of when the layout profile was last updated  
<span class="type-label">Type: </span>**dateTime**

-----
[name]: #name
#### [name]
The friendly name of the layout profile  
<span class="type-label">Type: </span>**string**

-----
[userRecordId]: #userrecordid
#### [userRecordId]
The [SoftLayer_User_Customer]({{<ref "reference/datatypes/SoftLayer_User_Customer">}}) owning this layout profile  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[layoutContainers]: #layoutcontainers
#### [layoutContainers]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Layout_Container'>SoftLayer_Layout_Container[] </a>**

-----
[layoutPreferences]: #layoutpreferences
#### [layoutPreferences]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Layout_Profile_Preference'>SoftLayer_Layout_Profile_Preference[] </a>**


## Count

-----
[layoutContainerCount]: #layoutcontainercount
#### [layoutContainerCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[layoutPreferenceCount]: #layoutpreferencecount
#### [layoutPreferenceCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**

</div>


