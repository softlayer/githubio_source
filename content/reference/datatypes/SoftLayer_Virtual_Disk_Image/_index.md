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
[capacity]: #capacity
#### [capacity]
A disk image's size measured in gigabytes.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[checksum]: #checksum
#### [checksum]
A disk image's unique md5 checksum.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
The date a disk image was created.   
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[description]: #description
#### [description]
A brief description of a virtual disk image.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A disk image's unique ID.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date a disk image was last modified.   
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
A descriptive name used to identify a disk image to a user.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[parentId]: #parentid
#### [parentId]
The ID of the the disk image that this disk image is based on, if applicable.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[storageRepositoryId]: #storagerepositoryid
#### [storageRepositoryId]
The [SoftLayer_Virtual_Storage_Repository]({{<ref "reference/datatypes/SoftLayer_Virtual_Storage_Repository">}}) that a disk image is in.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[typeId]: #typeid
#### [typeId]
A disk image's [SoftLayer_Virtual_Disk_Image_Type]({{<ref "reference/datatypes/SoftLayer_Virtual_Disk_Image_Type">}}) ID   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[units]: #units
#### [units]
The unit of storage in which the size of the image is measured. Defaults to "GB" for gigabytes.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[uuid]: #uuid
#### [uuid]
A disk image's unique ID on a virtualization platform.   
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[billingItem]: #billingitem
#### [billingItem]
The billing item for a virtual disk image.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item_Virtual_Disk_Image'>SoftLayer_Billing_Item_Virtual_Disk_Image </a>**


</div>
<div class="prop-row">

-----
[blockDevices]: #blockdevices
#### [blockDevices]
The block devices that a disk image is attached to. Block devices connect computing instances to disk images.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device'>SoftLayer_Virtual_Guest_Block_Device[] </a>**


</div>
<div class="prop-row">

-----
[bootableVolumeFlag]: #bootablevolumeflag
#### [bootableVolumeFlag]
  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[cloudInitFlag]: #cloudinitflag
#### [cloudInitFlag]
Check if cloud-init is enabled.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[coalescedDiskImages]: #coalesceddiskimages
#### [coalescedDiskImages]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Disk_Image'>SoftLayer_Virtual_Disk_Image[] </a>**


</div>
<div class="prop-row">

-----
[copyOnWriteFlag]: #copyonwriteflag
#### [copyOnWriteFlag]
  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[diskImageStorageGroup]: #diskimagestoragegroup
#### [diskImageStorageGroup]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Storage_Group'>SoftLayer_Configuration_Storage_Group </a>**


</div>
<div class="prop-row">

-----
[importedDiskType]: #importeddisktype
#### [importedDiskType]
Return imported disk type  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[isEncrypted]: #isencrypted
#### [isEncrypted]
Return if image is encrypted  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[localDiskFlag]: #localdiskflag
#### [localDiskFlag]
  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[metadataFlag]: #metadataflag
#### [metadataFlag]
Whether this disk image is meant for storage of custom user data supplied with a Cloud Computing Instance order.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[softwareReferences]: #softwarereferences
#### [softwareReferences]
References to the software that resides on a disk image.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Disk_Image_Software'>SoftLayer_Virtual_Disk_Image_Software[] </a>**


</div>
<div class="prop-row">

-----
[sourceDiskImage]: #sourcediskimage
#### [sourceDiskImage]
The original disk image that the current disk image was cloned from.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Disk_Image'>SoftLayer_Virtual_Disk_Image </a>**


</div>
<div class="prop-row">

-----
[storageGroupDetails]: #storagegroupdetails
#### [storageGroupDetails]
Return storage group details for symantec disk  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[storageGroups]: #storagegroups
#### [storageGroups]
The storage group for a virtual disk image.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Storage_Group'>SoftLayer_Configuration_Storage_Group[] </a>**


</div>
<div class="prop-row">

-----
[storageRepository]: #storagerepository
#### [storageRepository]
The storage repository that a disk image resides in.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Storage_Repository'>SoftLayer_Virtual_Storage_Repository </a>**


</div>
<div class="prop-row">

-----
[storageRepositoryType]: #storagerepositorytype
#### [storageRepositoryType]
The type of storage repository that a disk image resides in.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Storage_Repository_Type'>SoftLayer_Virtual_Storage_Repository_Type </a>**


</div>
<div class="prop-row">

-----
[templateBlockDevice]: #templateblockdevice
#### [templateBlockDevice]
The template that attaches a disk image to a [SoftLayer_Virtual_Guest_Block_Device_Template_Group]({{<ref "reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group">}}).  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template'>SoftLayer_Virtual_Guest_Block_Device_Template </a>**


</div>
<div class="prop-row">

-----
[type]: #type
#### [type]
A virtual disk image's type.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Disk_Image_Type'>SoftLayer_Virtual_Disk_Image_Type </a>**


</div>

## Count
<div class="prop-row">

-----
[blockDeviceCount]: #blockdevicecount
#### [blockDeviceCount]
A count of the block devices that a disk image is attached to. Block devices connect computing instances to disk images.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[coalescedDiskImageCount]: #coalesceddiskimagecount
#### [coalescedDiskImageCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[softwareReferenceCount]: #softwarereferencecount
#### [softwareReferenceCount]
A count of references to the software that resides on a disk image.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[storageGroupCount]: #storagegroupcount
#### [storageGroupCount]
A count of the storage group for a virtual disk image.   
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


