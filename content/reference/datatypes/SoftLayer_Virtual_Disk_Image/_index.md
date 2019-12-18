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

## Local
-----
[capacity]: #capacity
#### [capacity]
A disk image's size measured in gigabytes.   
<span class="type-label">Type: </span>**integer**

-----
[checksum]: #checksum
#### [checksum]
A disk image's unique md5 checksum.   
<span class="type-label">Type: </span>**string**

-----
[createDate]: #createdate
#### [createDate]
The date a disk image was created.   
<span class="type-label">Type: </span>**dateTime**

-----
[description]: #description
#### [description]
A brief description of a virtual disk image.   
<span class="type-label">Type: </span>**string**

-----
[id]: #id
#### [id]
A disk image's unique ID.   
<span class="type-label">Type: </span>**integer**

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date a disk image was last modified.   
<span class="type-label">Type: </span>**dateTime**

-----
[name]: #name
#### [name]
A descriptive name used to identify a disk image to a user.   
<span class="type-label">Type: </span>**string**

-----
[parentId]: #parentid
#### [parentId]
The ID of the the disk image that this disk image is based on, if applicable.   
<span class="type-label">Type: </span>**integer**

-----
[storageRepositoryId]: #storagerepositoryid
#### [storageRepositoryId]
The [SoftLayer_Virtual_Storage_Repository]({{<ref "reference/datatypes/SoftLayer_Virtual_Storage_Repository">}}) that a disk image is in.   
<span class="type-label">Type: </span>**integer**

-----
[typeId]: #typeid
#### [typeId]
A disk image's [SoftLayer_Virtual_Disk_Image_Type]({{<ref "reference/datatypes/SoftLayer_Virtual_Disk_Image_Type">}}) ID   
<span class="type-label">Type: </span>**integer**

-----
[units]: #units
#### [units]
The unit of storage in which the size of the image is measured. Defaults to "GB" for gigabytes.   
<span class="type-label">Type: </span>**string**

-----
[uuid]: #uuid
#### [uuid]
A disk image's unique ID on a virtualization platform.   
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[billingItem]: #billingitem
#### [billingItem]
The billing item for a virtual disk image.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item_Virtual_Disk_Image'>SoftLayer_Billing_Item_Virtual_Disk_Image </a>**

-----
[blockDevices]: #blockdevices
#### [blockDevices]
The block devices that a disk image is attached to. Block devices connect computing instances to disk images.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device'>SoftLayer_Virtual_Guest_Block_Device[] </a>**

-----
[bootableVolumeFlag]: #bootablevolumeflag
#### [bootableVolumeFlag]
  
<span class="type-label">Type: </span>**boolean**

-----
[coalescedDiskImages]: #coalesceddiskimages
#### [coalescedDiskImages]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Disk_Image'>SoftLayer_Virtual_Disk_Image[] </a>**

-----
[copyOnWriteFlag]: #copyonwriteflag
#### [copyOnWriteFlag]
  
<span class="type-label">Type: </span>**boolean**

-----
[importedDiskType]: #importeddisktype
#### [importedDiskType]
Return imported disk type  
<span class="type-label">Type: </span>**string**

-----
[isEncrypted]: #isencrypted
#### [isEncrypted]
Return if image is encrypted  
<span class="type-label">Type: </span>**boolean**

-----
[localDiskFlag]: #localdiskflag
#### [localDiskFlag]
  
<span class="type-label">Type: </span>**boolean**

-----
[metadataFlag]: #metadataflag
#### [metadataFlag]
Whether this disk image is meant for storage of custom user data supplied with a Cloud Computing Instance order.  
<span class="type-label">Type: </span>**boolean**

-----
[softwareReferences]: #softwarereferences
#### [softwareReferences]
References to the software that resides on a disk image.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Disk_Image_Software'>SoftLayer_Virtual_Disk_Image_Software[] </a>**

-----
[sourceDiskImage]: #sourcediskimage
#### [sourceDiskImage]
The original disk image that the current disk image was cloned from.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Disk_Image'>SoftLayer_Virtual_Disk_Image </a>**

-----
[storageRepository]: #storagerepository
#### [storageRepository]
The storage repository that a disk image resides in.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Storage_Repository'>SoftLayer_Virtual_Storage_Repository </a>**

-----
[storageRepositoryType]: #storagerepositorytype
#### [storageRepositoryType]
The type of storage repository that a disk image resides in.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Storage_Repository_Type'>SoftLayer_Virtual_Storage_Repository_Type </a>**

-----
[templateBlockDevice]: #templateblockdevice
#### [templateBlockDevice]
The template that attaches a disk image to a [SoftLayer_Virtual_Guest_Block_Device_Template_Group]({{<ref "reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group">}}).  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template'>SoftLayer_Virtual_Guest_Block_Device_Template </a>**

-----
[type]: #type
#### [type]
A virtual disk image's type.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Disk_Image_Type'>SoftLayer_Virtual_Disk_Image_Type </a>**


## Count

-----
[blockDeviceCount]: #blockdevicecount
#### [blockDeviceCount]
A count of the block devices that a disk image is attached to. Block devices connect computing instances to disk images.   
<span class="type-label">Type: </span>**unsigned long**


-----
[coalescedDiskImageCount]: #coalesceddiskimagecount
#### [coalescedDiskImageCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[softwareReferenceCount]: #softwarereferencecount
#### [softwareReferenceCount]
A count of references to the software that resides on a disk image.   
<span class="type-label">Type: </span>**unsigned long**

</div>


