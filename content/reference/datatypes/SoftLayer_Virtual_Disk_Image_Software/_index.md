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

* [SoftLayer_Virtual_Disk_Image](/reference/datatypes/SoftLayer_Virtual_Disk_Image )


* [SoftLayer_Software_Description](/reference/services/SoftLayer_Software_Description )




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
        <h2>Local</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>The unique identifier of a virtual disk image to software relationship.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#softwareDescriptionId" name=softwareDescriptionId>softwareDescriptionId</a>
            </span>
            <div class='views-field-body'>The unique identifier of the software that a virtual disk image is associated with.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#diskImage" name=diskImage>diskImage</a>
            </span>
            <div class='views-field-body'>The virtual disk image that is associated with software. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Virtual_Disk_Image'>SoftLayer_Virtual_Disk_Image </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#passwords" name=passwords>passwords</a>
            </span>
            <div class='views-field-body'>Username/Password pairs used for access to a Software Installation. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Virtual_Disk_Image_Software_Password'>SoftLayer_Virtual_Disk_Image_Software_Password[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#softwareDescription" name=softwareDescription>softwareDescription</a>
            </span>
            <div class='views-field-body'>The software associated with a virtual disk image. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Software_Description'>SoftLayer_Software_Description </a></p>
            </div>
        </div>
                <h2>Count</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#passwordCount" name=passwordCount>passwordCount</a>
            </span>
            <div class='views-field-body'>A count of username/Password pairs used for access to a Software Installation. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
            </div>
</div>


