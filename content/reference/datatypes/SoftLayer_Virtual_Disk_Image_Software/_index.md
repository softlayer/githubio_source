---
title: "SoftLayer_Virtual_Disk_Image_Software"
description: "A SoftLayer_Virtual_Disk_Image_Software record connects a computing instance's virtual disk images with software records... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Disk_Image_Software"
---

# SoftLayer_Virtual_Disk_Image_Software
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Virtual_Disk_Image_Software' >Datatype</a></li>
    </ul>
</div>

## Description 


A SoftLayer_Virtual_Disk_Image_Software record connects a computing instance's virtual disk images with software records. This can be useful if a disk image is directly associated with software such as operating systems. 



### seeAlso

* [SoftLayer_Virtual_Disk_Image](/reference/services/SoftLayer_Virtual_Disk_Image )


* [SoftLayer_Software_Description](/reference/services/SoftLayer_Software_Description )




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
The unique identifier of a virtual disk image to software relationship.   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[softwareDescriptionId]: #softwaredescriptionid
#### [softwareDescriptionId]
The unique identifier of the software that a virtual disk image is associated with.   
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[diskImage]: #diskimage
#### [diskImage]
The virtual disk image that is associated with software.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Disk_Image'>SoftLayer_Virtual_Disk_Image </a>**  



</div>
<div class="prop-row">

-----
[passwords]: #passwords
#### [passwords]
Username/Password pairs used for access to a Software Installation.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Disk_Image_Software_Password'>SoftLayer_Virtual_Disk_Image_Software_Password[] </a>**  



</div>
<div class="prop-row">

-----
[softwareDescription]: #softwaredescription
#### [softwareDescription]
The software associated with a virtual disk image.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Description'>SoftLayer_Software_Description </a>**  



</div>

## Count
<div class="prop-row">

-----
[passwordCount]: #passwordcount
#### [passwordCount]
A count of username/Password pairs used for access to a Software Installation.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>


