---
title: "SoftLayer_Scale_Policy_Action_Scale"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Scale"
classes:
    - "SoftLayer_Scale_Policy_Action_Scale"
---

# SoftLayer_Scale_Policy_Action_Scale
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Scale_Policy_Action_Scale' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Scale_Policy_Action_Scale' >Datatype</a></li>
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
[amount]: #amount
#### [amount]
The number to scale by. This number has different meanings based on type.  
<span class="type-label">Type: </span>**integer**

-----
[createDate]: #createdate
#### [createDate]
When this action was created.  
<span class="type-label">Type: </span>**dateTime**

-----
[deleteFlag]: #deleteflag
#### [deleteFlag]
When set and true any edit that happens on this object, be it calling edit on this directly or setting as a child while editing a parent object, will end up being a deletion.   
<span class="type-label">Type: </span>**boolean**

-----
[id]: #id
#### [id]
An action's internal identifier.  
<span class="type-label">Type: </span>**integer**

-----
[modifyDate]: #modifydate
#### [modifyDate]
Then this action was last modified.  
<span class="type-label">Type: </span>**dateTime**

-----
[scalePolicyId]: #scalepolicyid
#### [scalePolicyId]
The policy this action is on.  
<span class="type-label">Type: </span>**integer**

-----
[scaleType]: #scaletype
#### [scaleType]
The type of scale to perform. Possible values: 


* ABSOLUTE - Force the group to be set at a specific number of group members. This may include scaling up or
down or not at all. If the amount is outside of the min/max range of the group, an error occurs. 
* PERCENT - Scale the group up or down based on the positive or negative percentage given in amount. The
number is a percent of the current group member count. Any extra percent after the decimal point is always ignored. If the resulting amount is zero, -1 or 1 is used depending upon whether the percentage was negative or positive respectively. 
* RELATIVE - Scale the group up or down by the positive or negative value given in amount.  
<span class="type-label">Type: </span>**string**

-----
[typeId]: #typeid
#### [typeId]
The identifier of this action's type.  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[scalePolicy]: #scalepolicy
#### [scalePolicy]
The policy this action is on.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Scale_Policy'>SoftLayer_Scale_Policy </a>**

-----
[type]: #type
#### [type]
The type of action.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Scale_Policy_Action_Type'>SoftLayer_Scale_Policy_Action_Type </a>**


## Count
</div>


