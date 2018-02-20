---
title: "SoftLayer_Virtual_Disk_Image"
description: "The virtual disk image data type presents the structure in which a virtual disk image will be presented. 

Virtual block... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Disk_Image"
---

# SoftLayer_Virtual_Disk_Image
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Virtual_Disk_Image' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Virtual_Disk_Image' >Datatype</a></li>
    </ul>
</div>

## Description 
The virtual disk image data type presents the structure in which a virtual disk image will be presented. 

Virtual block devices are assigned to disk images. 
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
            <span class='views-field-title'><a href="#capacity" name=capacity>capacity</a></span>
            <div class='views-field-body'>A disk image's size measured in gigabytes.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#checksum" name=checksum>checksum</a></span>
            <div class='views-field-body'>A disk image's unique md5 checksum.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#createDate" name=createDate>createDate</a></span>
            <div class='views-field-body'>The date a disk image was created.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#description" name=description>description</a></span>
            <div class='views-field-body'>A brief description of a virtual disk image.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>A disk image's unique ID.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#modifyDate" name=modifyDate>modifyDate</a></span>
            <div class='views-field-body'>The date a disk image was last modified.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#name" name=name>name</a></span>
            <div class='views-field-body'>A descriptive name used to identify a disk image to a user.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#parentId" name=parentId>parentId</a></span>
            <div class='views-field-body'>The ID of the the disk image that this disk image is based on, if applicable.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#storageRepositoryId" name=storageRepositoryId>storageRepositoryId</a></span>
            <div class='views-field-body'>The [[SoftLayer_Virtual_Storage_Repository|storage repository]] that a disk image is in.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#typeId" name=typeId>typeId</a></span>
            <div class='views-field-body'>A disk image's [[SoftLayer_Virtual_Disk_Image_Type|type]] ID  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#units" name=units>units</a></span>
            <div class='views-field-body'>The unit of storage in which the size of the image is measured. Defaults to "GB" for gigabytes.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#uuid" name=uuid>uuid</a></span>
            <div class='views-field-body'>A disk image's unique ID on a virtualization platform.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#billingItem" name=billingItem>billingItem</a></span>
            <div class='views-field-body'>The billing item for a virtual disk image. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Billing_Item_Virtual_Disk_Image'>SoftLayer_Billing_Item_Virtual_Disk_Image </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#blockDevices" name=blockDevices>blockDevices</a></span>
            <div class='views-field-body'>The block devices that a disk image is attached to. Block devices connect computing instances to disk images. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device'>SoftLayer_Virtual_Guest_Block_Device[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#bootableVolumeFlag" name=bootableVolumeFlag>bootableVolumeFlag</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#coalescedDiskImages" name=coalescedDiskImages>coalescedDiskImages</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Virtual_Disk_Image'>SoftLayer_Virtual_Disk_Image[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#copyOnWriteFlag" name=copyOnWriteFlag>copyOnWriteFlag</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#localDiskFlag" name=localDiskFlag>localDiskFlag</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#metadataFlag" name=metadataFlag>metadataFlag</a></span>
            <div class='views-field-body'>Whether this disk image is meant for storage of custom user data supplied with a Cloud Computing Instance order. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#softwareReferences" name=softwareReferences>softwareReferences</a></span>
            <div class='views-field-body'>References to the software that resides on a disk image. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Virtual_Disk_Image_Software'>SoftLayer_Virtual_Disk_Image_Software[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#sourceDiskImage" name=sourceDiskImage>sourceDiskImage</a></span>
            <div class='views-field-body'>The original disk image that the current disk image was cloned from. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Virtual_Disk_Image'>SoftLayer_Virtual_Disk_Image </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#storageRepository" name=storageRepository>storageRepository</a></span>
            <div class='views-field-body'>The storage repository that a disk image resides in. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Virtual_Storage_Repository'>SoftLayer_Virtual_Storage_Repository </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#storageRepositoryType" name=storageRepositoryType>storageRepositoryType</a></span>
            <div class='views-field-body'>The type of storage repository that a disk image resides in. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Virtual_Storage_Repository_Type'>SoftLayer_Virtual_Storage_Repository_Type </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#templateBlockDevice" name=templateBlockDevice>templateBlockDevice</a></span>
            <div class='views-field-body'>The template that attaches a disk image to a [[SoftLayer_Virtual_Guest_Block_Device_Template_Group|archive]]. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template'>SoftLayer_Virtual_Guest_Block_Device_Template </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#type" name=type>type</a></span>
            <div class='views-field-body'>A virtual disk image's type. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Virtual_Disk_Image_Type'>SoftLayer_Virtual_Disk_Image_Type </a></p></div>
        </div>
            </div>
</div>


