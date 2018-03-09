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
        <h2>Local</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#device" name=device>device</a>
            </span>
            <div class='views-field-body'>A name that identifies a block device template.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#diskImageId" name=diskImageId>diskImageId</a>
            </span>
            <div class='views-field-body'>A block device template's [[SoftLayer_Virtual_Disk_Image|disk image]] ID.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#diskSpace" name=diskSpace>diskSpace</a>
            </span>
            <div class='views-field-body'>The amount of disk space that a block device template is using.  Use this number along with the units property to obtain the correct space used.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>float</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#groupId" name=groupId>groupId</a>
            </span>
            <div class='views-field-body'>A block device template's [[SoftLayer_Virtual_Guest_Block_Device_Template_Group|group]] ID.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>A block device template's unique ID.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#units" name=units>units</a>
            </span>
            <div class='views-field-body'>The units that will be used with the disk space property to identify the amount of disk space used.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#diskImage" name=diskImage>diskImage</a>
            </span>
            <div class='views-field-body'>A block device template's disk image. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Virtual_Disk_Image'>SoftLayer_Virtual_Disk_Image </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#group" name=group>group</a>
            </span>
            <div class='views-field-body'>A block device template's group. Several block device templates can be combined together into a group for archiving purposes. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group'>SoftLayer_Virtual_Guest_Block_Device_Template_Group </a></p>
            </div>
        </div>
                <h2>Count</h2>
            </div>
</div>


