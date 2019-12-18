---
title: "SoftLayer_Virtual_PlacementGroup"
description: "This data type presents the structure for a virtual guest placement group. The data type contains relational properties... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_PlacementGroup"
---

# SoftLayer_Virtual_PlacementGroup
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Virtual_PlacementGroup' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Virtual_PlacementGroup' >Datatype</a></li>
    </ul>
</div>

## Description 
This data type presents the structure for a virtual guest placement group. The data type contains relational properties to the virtual guest placement group rule class. 





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
[accountId]: #accountid
#### [accountId]
The unique ID of the account that created the placement group.   
<span class="type-label">Type: </span>**integer**

-----
[backendRouterId]: #backendrouterid
#### [backendRouterId]
The placement group's backend router's associated unique ID.   
<span class="type-label">Type: </span>**integer**

-----
[createDate]: #createdate
#### [createDate]
The placement group's date of creation.   
<span class="type-label">Type: </span>**dateTime**

-----
[id]: #id
#### [id]
The placement group's associated unique ID.   
<span class="type-label">Type: </span>**integer**

-----
[modifyDate]: #modifydate
#### [modifyDate]
The placement group's date of most recent modification.   
<span class="type-label">Type: </span>**dateTime**

-----
[name]: #name
#### [name]
The placement group's name.   
<span class="type-label">Type: </span>**string**

-----
[ruleId]: #ruleid
#### [ruleId]
The associated unique ID of the placement group's rule.   
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
The account that the placement group is implemented on.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[backendRouter]: #backendrouter
#### [backendRouter]
The router the placement group is implemented on.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Router_Backend'>SoftLayer_Hardware_Router_Backend </a>**

-----
[guests]: #guests
#### [guests]
The virtual guests that are members of the placement group.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**

-----
[rule]: #rule
#### [rule]
The placement rule that the placement group is implementing.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_PlacementGroup_Rule'>SoftLayer_Virtual_PlacementGroup_Rule </a>**


## Count

-----
[guestCount]: #guestcount
#### [guestCount]
A count of the virtual guests that are members of the placement group.   
<span class="type-label">Type: </span>**unsigned long**

</div>


