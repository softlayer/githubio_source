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
[id]: #id
#### [id]
A partition's id.  
<span class="type-label">Type: </span>**integer**

-----
[isGrow]: #isgrow
#### [isGrow]
A flag indication if a partition will be the grow partition.  The grow partition will have its size adjusted to fill all available space on a hard drive.   
<span class="type-label">Type: </span>**boolean**

-----
[partitionName]: #partitionname
#### [partitionName]
A partition's default name.  
<span class="type-label">Type: </span>**string**

-----
[partitionSize]: #partitionsize
#### [partitionSize]
A partition's default size.  
<span class="type-label">Type: </span>**decimal**

-----
[partitionTemplateId]: #partitiontemplateid
#### [partitionTemplateId]
A partition's associated [SoftLayer_Hardware_Component_Partition_Template]({{<ref "reference/datatypes/SoftLayer_Hardware_Component_Partition_Template">}}) Id.  
<span class="type-label">Type: </span>**integer**

-----
[volumeNumber]: #volumenumber
#### [volumeNumber]
The volume the partition will be put on  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[filesystemType]: #filesystemtype
#### [filesystemType]
The filesystem type of a partition  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Storage_Filesystem_Type'>SoftLayer_Configuration_Storage_Filesystem_Type </a>**

-----
[partitionTemplate]: #partitiontemplate
#### [partitionTemplate]
A partition's [SoftLayer_Hardware_Component_Partition_Template]({{<ref "reference/datatypes/SoftLayer_Hardware_Component_Partition_Template">}}).  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_Partition_Template'>SoftLayer_Hardware_Component_Partition_Template </a>**


## Count
</div>


