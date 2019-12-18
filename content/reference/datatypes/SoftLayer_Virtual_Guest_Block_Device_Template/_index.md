---
title: "SoftLayer_Virtual_Guest_Block_Device_Template"
description: "The virtual block device template data type presents the structure in which all archived image templates are presented.... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest_Block_Device_Template"
---

# SoftLayer_Virtual_Guest_Block_Device_Template
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template' >Datatype</a></li>
    </ul>
</div>

## Description 
The virtual block device template data type presents the structure in which all archived image templates are presented. 

A virtual block device template, also known as a image template, represents the image of a virtual guest instance. 





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
[device]: #device
#### [device]
A name that identifies a block device template.   
<span class="type-label">Type: </span>**string**

-----
[diskImageId]: #diskimageid
#### [diskImageId]
A block device template's [SoftLayer_Virtual_Disk_Image]({{<ref "reference/datatypes/SoftLayer_Virtual_Disk_Image">}}) ID.   
<span class="type-label">Type: </span>**integer**

-----
[diskSpace]: #diskspace
#### [diskSpace]
The amount of disk space that a block device template is using.  Use this number along with the units property to obtain the correct space used.   
<span class="type-label">Type: </span>**float**

-----
[groupId]: #groupid
#### [groupId]
A block device template's [SoftLayer_Virtual_Guest_Block_Device_Template_Group]({{<ref "reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group">}}) ID.   
<span class="type-label">Type: </span>**integer**

-----
[id]: #id
#### [id]
A block device template's unique ID.   
<span class="type-label">Type: </span>**integer**

-----
[units]: #units
#### [units]
The units that will be used with the disk space property to identify the amount of disk space used.   
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[diskImage]: #diskimage
#### [diskImage]
A block device template's disk image.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Disk_Image'>SoftLayer_Virtual_Disk_Image </a>**

-----
[group]: #group
#### [group]
A block device template's group. Several block device templates can be combined together into a group for archiving purposes.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group'>SoftLayer_Virtual_Guest_Block_Device_Template_Group </a>**


## Count
</div>


