---
title: "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
description: "The virtual guest block device template group service provides a common interface to an accounts archived image template... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
---
# SoftLayer_Virtual_Guest_Block_Device_Template_Group
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group' >Datatype</a></li>
    </ul>
</div>

## Description
The virtual guest block device template group service provides a common interface to an accounts archived image templates The interaction with various third party APIs is not needed when implementing this service to administer your guests. 



        
<div id="properties" class="content service-content">

## Methods

<div class="view-filters">
    <div class="clearfix">
        <div class="search-input-box">
            <input placeholder="Method Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

<div id="method-div">

<div class="method-row">

#### [addByolAttribute](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/addByolAttribute)

</div>

<div class="method-row">

#### [addCloudInitAttribute](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/addCloudInitAttribute)

</div>

<div class="method-row">

#### [addLocations](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/addLocations)
[SoftLayer_Virtual_Guest_Block_Device]({{<ref "reference/datatypes/SoftLayer_Virtual_Guest_Block_Device">}}) can be made available in all storage locations. This method will create transaction(s) to add available locations to an archive image template. 
</div>

<div class="method-row">

#### [addSupportedBootMode](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/addSupportedBootMode)

</div>

<div class="method-row">

#### [copyToExternalSource](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/copyToExternalSource)
This method generates a transaction to export/copy a template to an external source. 
</div>

<div class="method-row">

#### [copyToIcos](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/copyToIcos)
This method generates a transaction to export/copy a template to IBM Cloud Object Storage (ICOS) 
</div>

<div class="method-row">

#### [createFromExternalSource](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/createFromExternalSource)
This method generates a transaction to import a disk image from an external source and create a standard image template. 
</div>

<div class="method-row">

#### [createFromIcos](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/createFromIcos)
This method generates a process instance to import a disk image from ICOS and create a standard image template. 
</div>

<div class="method-row">

#### [createPublicArchiveTransaction](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/createPublicArchiveTransaction)
[SoftLayer_Virtual_Guest_Block_Device]({{<ref "reference/datatypes/SoftLayer_Virtual_Guest_Block_Device">}}) can be published together in a public repository for use by everyone. This method generates a transaction to perform a public image of the provided archived block devices. 
</div>

<div class="method-row">

#### [deleteByolAttribute](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/deleteByolAttribute)

</div>

<div class="method-row">

#### [deleteCloudInitAttribute](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/deleteCloudInitAttribute)

</div>

<div class="method-row">

#### [deleteObject](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/deleteObject)
Create a transaction that will remove all block device templates from the group and delete the disk images associated with them. 
</div>

<div class="method-row">

#### [denySharingAccess](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/denySharingAccess)
Deny another SoftLayer customer account's previously given access to provision CloudLayer Computing Instances from an image template group. Template access should only be removed from the parent template group object, not the child. 
</div>

<div class="method-row">

#### [editObject](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/editObject)
Edit an image template group's name and note.
</div>

<div class="method-row">

#### [findGcImagesByCurrentUser](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/findGcImagesByCurrentUser)
Fetch a sorted collection of GC enabled cloudinit images for the account of the current active customer user. 
</div>

<div class="method-row">

#### [getAccount](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getAccount)
Retrieve a block device template group's [SoftLayer_Account]({{<ref "reference/datatypes/SoftLayer_Account">}}).
</div>

<div class="method-row">

#### [getAccountContacts](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getAccountContacts)

</div>

<div class="method-row">

#### [getAccountReferences](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getAccountReferences)
Retrieve the accounts which may have read-only access to an image template group. Will only be populated for parent template group objects.
</div>

<div class="method-row">

#### [getAllAvailableCompatiblePlatformNames](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getAllAvailableCompatiblePlatformNames)

</div>

<div class="method-row">

#### [getBlockDevices](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getBlockDevices)
Retrieve the block devices that are part of an image template group
</div>

<div class="method-row">

#### [getBlockDevicesDiskSpaceTotal](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getBlockDevicesDiskSpaceTotal)
Retrieve the total disk space of all images in a image template group.
</div>

<div class="method-row">

#### [getBootMode](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getBootMode)

</div>

<div class="method-row">

#### [getByolFlag](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getByolFlag)
Retrieve a flag indicating that customer is providing the software licenses.
</div>

<div class="method-row">

#### [getChildren](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getChildren)
Retrieve the image template groups that are clones of an image template group.
</div>

<div class="method-row">

#### [getCurrentCompatiblePlatformNames](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getCurrentCompatiblePlatformNames)

</div>

<div class="method-row">

#### [getDatacenter](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getDatacenter)
Retrieve the location containing this image template group. Will only be populated for child template group objects.
</div>

<div class="method-row">

#### [getDatacenters](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getDatacenters)
Retrieve a collection of locations containing a copy of this image template group. Will only be populated for parent template group objects.
</div>

<div class="method-row">

#### [getDefaultBootMode](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getDefaultBootMode)

</div>

<div class="method-row">

#### [getEncryptionAttributes](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getEncryptionAttributes)

</div>

<div class="method-row">

#### [getFlexImageFlag](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getFlexImageFlag)
Retrieve a flag indicating if this is a flex image.
</div>

<div class="method-row">

#### [getGlobalIdentifier](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getGlobalIdentifier)
Retrieve an image template's universally unique identifier.
</div>

<div class="method-row">

#### [getImageType](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getImageType)
Retrieve the virtual disk image type of this template. Value will be populated on parent and child, but only supports object filtering on the parent.
</div>

<div class="method-row">

#### [getImageTypeKeyName](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getImageTypeKeyName)
Retrieve the virtual disk image type keyname (e.g. SYSTEM, DISK_CAPTURE, ISO, etc) of this template. Value will be populated on parent and child, but only supports object filtering on the parent.
</div>

<div class="method-row">

#### [getNextGenFlag](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getNextGenFlag)
Retrieve a flag indicating if this is a next generation image.
</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getObject)
Retrieve a SoftLayer_Virtual_Guest_Block_Device_Template_Group record.
</div>

<div class="method-row">

#### [getParent](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getParent)
Retrieve the image template group that another image template group was cloned from.
</div>

<div class="method-row">

#### [getPublicCustomerOwnedImages](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getPublicCustomerOwnedImages)
Gets all public customer owned image templates that the user is allowed to see. 
</div>

<div class="method-row">

#### [getPublicImages](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getPublicImages)
Gets all public image templates that the user is allowed to see. 
</div>

<div class="method-row">

#### [getSshKeys](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getSshKeys)
Retrieve the ssh keys to be implemented on the server when provisioned or reloaded from an image template group.
</div>

<div class="method-row">

#### [getStatus](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getStatus)
Retrieve a template group's status.
</div>

<div class="method-row">

#### [getStorageLocations](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getStorageLocations)
The available locations for public image storage. 
</div>

<div class="method-row">

#### [getStorageRepository](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getStorageRepository)
Retrieve the storage repository that an image template group resides on.
</div>

<div class="method-row">

#### [getSupportedBootModes](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getSupportedBootModes)

</div>

<div class="method-row">

#### [getSymantecImageFlag](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getSymantecImageFlag)
Retrieve a flag indicating if this is a symantec image.
</div>

<div class="method-row">

#### [getTagReferences](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getTagReferences)
Retrieve the tags associated with this image template group.
</div>

<div class="method-row">

#### [getTemplateDataCenterName](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getTemplateDataCenterName)

</div>

<div class="method-row">

#### [getTransaction](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getTransaction)
Retrieve a transaction that is being performed on a image template group.
</div>

<div class="method-row">

#### [getVhdImportSoftwareDescriptions](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getVhdImportSoftwareDescriptions)
Returns the software descriptions supported for VHD imports.
</div>

<div class="method-row">

#### [isByol](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/isByol)

</div>

<div class="method-row">

#### [isByolCapableOperatingSystem](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/isByolCapableOperatingSystem)

</div>

<div class="method-row">

#### [isByolOnlyOperatingSystem](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/isByolOnlyOperatingSystem)

</div>

<div class="method-row">

#### [isCloudInit](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/isCloudInit)

</div>

<div class="method-row">

#### [isCloudInitOnlyOperatingSystem](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/isCloudInitOnlyOperatingSystem)

</div>

<div class="method-row">

#### [isEncrypted](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/isEncrypted)

</div>

<div class="method-row">

#### [permitSharingAccess](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/permitSharingAccess)
Permit another SoftLayer customer account access to provision CloudLayer Computing Instances from an image template group. Template access should only be given to the parent template group object, not the child. 
</div>

<div class="method-row">

#### [removeCompatiblePlatforms](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/removeCompatiblePlatforms)

</div>

<div class="method-row">

#### [removeLocations](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/removeLocations)
[SoftLayer_Virtual_Guest_Block_Device]({{<ref "reference/datatypes/SoftLayer_Virtual_Guest_Block_Device">}}) can be made available in all storage locations. This method will create transaction(s) to remove available locations from an archive image template. 
</div>

<div class="method-row">

#### [removeSupportedBootMode](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/removeSupportedBootMode)

</div>

<div class="method-row">

#### [setAvailableLocations](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/setAvailableLocations)
This method generates the necessary transaction(s) to set available locations for archived block devices. 
</div>

<div class="method-row">

#### [setBootMode](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/setBootMode)

</div>

<div class="method-row">

#### [setCompatiblePlatforms](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/setCompatiblePlatforms)

</div>

<div class="method-row">

#### [setTags](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/setTags)
Set the tags for this template group.
</div>
</div>

</div>

