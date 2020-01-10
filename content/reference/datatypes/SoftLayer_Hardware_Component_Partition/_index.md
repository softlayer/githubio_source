---
title: "SoftLayer_Hardware_Component_Partition"
description: "The SoftLayer_Hardware_Component_Partition data type contains general information relating to a single hard drive partit... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Component_Partition"
---

# SoftLayer_Hardware_Component_Partition
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Hardware_Component_Partition' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Hardware_Component_Partition data type contains general information relating to a single hard drive partition. 





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
[diskNumber]: #disknumber
#### [diskNumber]
A hardware component partition's order in the [SoftLayer_Hardware_Server]({{<ref "reference/datatypes/SoftLayer_Hardware_Server">}}).  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[grow]: #grow
#### [grow]
A flag indicating if a partition is the grow partition. The grow partition will grow to fill all remaining space on a disk.  There can only be one.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[hardwareComponentId]: #hardwarecomponentid
#### [hardwareComponentId]
A hardware component partition's associated [SoftLayer_Hardware_Component]({{<ref "reference/datatypes/SoftLayer_Hardware_Component">}}) Id.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[minimumSize]: #minimumsize
#### [minimumSize]
A hardware component partition's minimum size(GB).  
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
A hardware component partition's name. On a server with windows this may be 'C' and on Linux this may be '/var'   
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[hardwareComponent]: #hardwarecomponent
#### [hardwareComponent]
A hardware component partitions's associated [SoftLayer_Hardware_Component]({{<ref "reference/datatypes/SoftLayer_Hardware_Component">}})  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component </a>**


</div>

## Count
</div>


