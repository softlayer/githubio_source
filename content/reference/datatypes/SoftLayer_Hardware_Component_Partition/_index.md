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
[diskNumber]: #disknumber
#### [diskNumber]
A hardware component partition's order in the [SoftLayer_Hardware_Server]({{<ref "reference/datatypes/SoftLayer_Hardware_Server">}}).  
<span class="type-label">Type: </span>**integer**

-----
[grow]: #grow
#### [grow]
A flag indicating if a partition is the grow partition. The grow partition will grow to fill all remaining space on a disk.  There can only be one.   
<span class="type-label">Type: </span>**integer**

-----
[hardwareComponentId]: #hardwarecomponentid
#### [hardwareComponentId]
A hardware component partition's associated [SoftLayer_Hardware_Component]({{<ref "reference/datatypes/SoftLayer_Hardware_Component">}}) Id.  
<span class="type-label">Type: </span>**integer**

-----
[minimumSize]: #minimumsize
#### [minimumSize]
A hardware component partition's minimum size(GB).  
<span class="type-label">Type: </span>**decimal**

-----
[name]: #name
#### [name]
A hardware component partition's name. On a server with windows this may be 'C' and on Linux this may be '/var'   
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[hardwareComponent]: #hardwarecomponent
#### [hardwareComponent]
A hardware component partitions's associated [SoftLayer_Hardware_Component]({{<ref "reference/datatypes/SoftLayer_Hardware_Component">}})  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component </a>**


## Count
</div>


