---
title: "SoftLayer_Scale_Policy_Trigger_Repeating"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Scale"
classes:
    - "SoftLayer_Scale_Policy_Trigger_Repeating"
---

# SoftLayer_Scale_Policy_Trigger_Repeating
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Scale_Policy_Trigger_Repeating' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Scale_Policy_Trigger_Repeating' >Datatype</a></li>
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
When this trigger was created.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[deleteFlag]: #deleteflag
#### [deleteFlag]
When set and true any edit that happens on this object, be it calling edit on this directly or setting as a child while editing a parent object, will end up being a deletion.   
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A trigger's internal identifier.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
When this trigger was last modified.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[scalePolicyId]: #scalepolicyid
#### [scalePolicyId]
The policy this trigger is on.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[schedule]: #schedule
#### [schedule]
The cron-formatted schedule. This is run in the UTC timezone.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[typeId]: #typeid
#### [typeId]
The type of trigger this is.  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[scalePolicy]: #scalepolicy
#### [scalePolicy]
The policy this trigger is on.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Scale_Policy'>SoftLayer_Scale_Policy </a>**  



</div>
<div class="prop-row">

-----
[type]: #type
#### [type]
The type of trigger.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Scale_Policy_Trigger_Type'>SoftLayer_Scale_Policy_Trigger_Type </a>**  



</div>

## Count
</div>


