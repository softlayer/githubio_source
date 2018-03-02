---
title: "SoftLayer_Virtual_Guest_Block_Device"
description: "The block device data type presents the structure in which all block devices will be presented. A block device attaches... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest_Block_Device"
---

# SoftLayer_Virtual_Guest_Block_Device
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device' >Datatype</a></li>
    </ul>
</div>

## Description 
The block device data type presents the structure in which all block devices will be presented. A block device attaches a disk image to a guest. Internally, the structure supports various virtualization platforms with no change to external interaction. 

A guest, also known as a virtual server, represents an allocation of resources on a virtual host. 





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
            <span class='views-field-title'><a href="#bootableFlag" name=bootableFlag>bootableFlag</a></span>
            <div class='views-field-body'>A flag indicating if a block device can be booted from.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#createDate" name=createDate>createDate</a></span>
            <div class='views-field-body'>The date a block device was created.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#device" name=device>device</a></span>
            <div class='views-field-body'>A name used to identify a block device.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#diskImageId" name=diskImageId>diskImageId</a></span>
            <div class='views-field-body'>A block device [[SoftLayer_Virtual_Disk_Image|disk image]]'s unique ID.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#guestId" name=guestId>guestId</a></span>
            <div class='views-field-body'>The [[SoftLayer_Virtual_Guest|computing instance]] that a block device is associated with.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#hotPlugFlag" name=hotPlugFlag>hotPlugFlag</a></span>
            <div class='views-field-body'>A flag indicating if a block device can be plugged into a computing instance without having to shut down the instance.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>A computing instance block device's unique ID.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#modifyDate" name=modifyDate>modifyDate</a></span>
            <div class='views-field-body'>The data a block device was last modified.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#mountMode" name=mountMode>mountMode</a></span>
            <div class='views-field-body'>The writing mode that a virtual block device is mounted as, either "RO" for read-only mode or "RW" for read and write mode.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#mountType" name=mountType>mountType</a></span>
            <div class='views-field-body'>The type of device that a virtual block device is mounted as, either "Disk" for a directly connected storage disk or "CD" for devices that are mounted as optical drives..  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#statusId" name=statusId>statusId</a></span>
            <div class='views-field-body'>The status of the device, either disconnected or connected  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#uuid" name=uuid>uuid</a></span>
            <div class='views-field-body'>A block device's unique ID on a virtualization platform.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#diskImage" name=diskImage>diskImage</a></span>
            <div class='views-field-body'>The disk image that a block device connects to in a computing instance. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Virtual_Disk_Image'>SoftLayer_Virtual_Disk_Image </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#guest" name=guest>guest</a></span>
            <div class='views-field-body'>The computing instance that this block device is attached to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#status" name=status>status</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Status'>SoftLayer_Virtual_Guest_Block_Device_Status </a></p></div>
        </div>
                <h2>Relational</h2>
            </div>
</div>


