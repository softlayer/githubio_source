---
title: "SoftLayer_Scale_Policy_Trigger"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Scale"
classes:
    - "SoftLayer_Scale_Policy_Trigger"
---

# SoftLayer_Scale_Policy_Trigger
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Scale_Policy_Trigger' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Scale_Policy_Trigger' >Datatype</a></li>
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
When this trigger was created.  
<span class="type-label">Type: </span>**dateTime**

-----
[deleteFlag]: #deleteflag
#### [deleteFlag]
When set and true any edit that happens on this object, be it calling edit on this directly or setting as a child while editing a parent object, will end up being a deletion.   
<span class="type-label">Type: </span>**boolean**

-----
[id]: #id
#### [id]
A trigger's internal identifier.  
<span class="type-label">Type: </span>**integer**

-----
[modifyDate]: #modifydate
#### [modifyDate]
When this trigger was last modified.  
<span class="type-label">Type: </span>**dateTime**

-----
[scalePolicyId]: #scalepolicyid
#### [scalePolicyId]
The policy this trigger is on.  
<span class="type-label">Type: </span>**integer**

-----
[typeId]: #typeid
#### [typeId]
The type of trigger this is.  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[scalePolicy]: #scalepolicy
#### [scalePolicy]
The policy this trigger is on.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Scale_Policy'>SoftLayer_Scale_Policy </a>**

-----
[type]: #type
#### [type]
The type of trigger.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Scale_Policy_Trigger_Type'>SoftLayer_Scale_Policy_Trigger_Type </a>**


## Count
</div>


