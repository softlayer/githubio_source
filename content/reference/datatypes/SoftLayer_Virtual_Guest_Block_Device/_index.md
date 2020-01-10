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
[bootableFlag]: #bootableflag
#### [bootableFlag]
A flag indicating if a block device can be booted from.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
The date a block device was created.   
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[device]: #device
#### [device]
A name used to identify a block device.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[diskImageId]: #diskimageid
#### [diskImageId]
A block device [SoftLayer_Virtual_Disk_Image]({{<ref "reference/datatypes/SoftLayer_Virtual_Disk_Image">}})'s unique ID.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[guestId]: #guestid
#### [guestId]
The [SoftLayer_Virtual_Guest]({{<ref "reference/datatypes/SoftLayer_Virtual_Guest">}}) that a block device is associated with.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[hotPlugFlag]: #hotplugflag
#### [hotPlugFlag]
A flag indicating if a block device can be plugged into a computing instance without having to shut down the instance.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A computing instance block device's unique ID.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
The data a block device was last modified.   
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[mountMode]: #mountmode
#### [mountMode]
The writing mode that a virtual block device is mounted as, either "RO" for read-only mode or "RW" for read and write mode.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[mountType]: #mounttype
#### [mountType]
The type of device that a virtual block device is mounted as, either "Disk" for a directly connected storage disk or "CD" for devices that are mounted as optical drives..   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[statusId]: #statusid
#### [statusId]
The status of the device, either disconnected or connected   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[uuid]: #uuid
#### [uuid]
A block device's unique ID on a virtualization platform.   
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[diskImage]: #diskimage
#### [diskImage]
The disk image that a block device connects to in a computing instance.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Disk_Image'>SoftLayer_Virtual_Disk_Image </a>**


</div>
<div class="prop-row">

-----
[guest]: #guest
#### [guest]
The computing instance that this block device is attached to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest </a>**


</div>
<div class="prop-row">

-----
[status]: #status
#### [status]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Status'>SoftLayer_Virtual_Guest_Block_Device_Status </a>**


</div>

## Count
</div>


