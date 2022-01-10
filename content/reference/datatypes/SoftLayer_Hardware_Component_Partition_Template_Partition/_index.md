---
title: "SoftLayer_Hardware_Component_Partition_Template_Partition"
description: "The SoftLayer_Hardware_Component_Partition_Template_Partition data type contains general information relating to a singl... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Component_Partition_Template_Partition"
---

# SoftLayer_Hardware_Component_Partition_Template_Partition
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Hardware_Component_Partition_Template_Partition' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_Hardware_Component_Partition_Template_Partition data type contains general information relating to a single SoftLayer Template Partition. 





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
[id]: #id
#### [id]
A partition's id.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[isGrow]: #isgrow
#### [isGrow]
A flag indication if a partition will be the grow partition.  The grow partition will have its size adjusted to fill all available space on a hard drive.   
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[partitionName]: #partitionname
#### [partitionName]
A partition's default name.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[partitionSize]: #partitionsize
#### [partitionSize]
A partition's default size.  
<span class="type-label">Type: </span>**decimal**  



</div>
<div class="prop-row">

-----
[partitionTemplateId]: #partitiontemplateid
#### [partitionTemplateId]
A partition's associated [SoftLayer_Hardware_Component_Partition_Template]({{<ref "reference/datatypes/SoftLayer_Hardware_Component_Partition_Template">}}) Id.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[volumeNumber]: #volumenumber
#### [volumeNumber]
The volume the partition will be put on  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[filesystemType]: #filesystemtype
#### [filesystemType]
The filesystem type of a partition  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Storage_Filesystem_Type'>SoftLayer_Configuration_Storage_Filesystem_Type </a>**  



</div>
<div class="prop-row">

-----
[partitionTemplate]: #partitiontemplate
#### [partitionTemplate]
A partition's [SoftLayer_Hardware_Component_Partition_Template]({{<ref "reference/datatypes/SoftLayer_Hardware_Component_Partition_Template">}}).  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_Partition_Template'>SoftLayer_Hardware_Component_Partition_Template </a>**  



</div>

## Count
</div>


