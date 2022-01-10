---
title: "SoftLayer_Configuration_Storage_Group_Template_Group"
description: "Single storage group(array) used in a storage group template. 

If a server configuration requires a raid configuration... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Configuration"
classes:
    - "SoftLayer_Configuration_Storage_Group_Template_Group"
---

# SoftLayer_Configuration_Storage_Group_Template_Group
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Configuration_Storage_Group_Template_Group' >Datatype</a></li>
    </ul>
</div>

## Description 


Single storage group(array) used in a storage group template. 

If a server configuration requires a raid configuration this object will describe a single array to be configured. 





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
[diskControllerIndex]: #diskcontrollerindex
#### [diskControllerIndex]
The disk controller for the array.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[grow]: #grow
#### [grow]
Flag to use all available space.  
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[hardDrivesString]: #harddrivesstring
#### [hardDrivesString]
Comma delimited integers of drive indexes for the array. This can also be the string 'all' to specify all drives in the server   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[hotSpareDrivesString]: #hotsparedrivesstring
#### [hotSpareDrivesString]
Comma delimited integers of drive indexes for hot spares on the array.   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[orderIndex]: #orderindex
#### [orderIndex]
The order of the arrays in the template.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[size]: #size
#### [size]
Size of array. Must be within limitations of the smallest drive and raid mode  
<span class="type-label">Type: </span>**decimal**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[type]: #type
#### [type]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Storage_Group_Array_Type'>SoftLayer_Configuration_Storage_Group_Array_Type </a>**  



</div>

## Count
</div>


