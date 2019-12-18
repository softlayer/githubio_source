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
            <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

#### [addByolAttribute](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/addByolAttribute)


#### [addCloudInitAttribute](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/addCloudInitAttribute)


#### [addLocations](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/addLocations)
[SoftLayer_Virtual_Guest_Block_Device]({{<ref "reference/datatypes/SoftLayer_Virtual_Guest_Block_Device">}}) can be made available in all storage locations. This method will create transaction(s) to add available locations to an archive image template. 

#### [addSupportedBootMode](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/addSupportedBootMode)


#### [copyToExternalSource](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/copyToExternalSource)
This method generates a transaction to export/copy a template to an external source. 

#### [copyToIcos](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/copyToIcos)
This method generates a transaction to export/copy a template to IBM Cloud Object Storage (ICOS) 

#### [createFromExternalSource](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/createFromExternalSource)
This method generates a transaction to import a disk image from an external source and create a standard image template. 

#### [createFromIcos](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/createFromIcos)
This method generates a process instance to import a disk image from ICOS and create a standard image template. 

#### [createPublicArchiveTransaction](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/createPublicArchiveTransaction)
[SoftLayer_Virtual_Guest_Block_Device]({{<ref "reference/datatypes/SoftLayer_Virtual_Guest_Block_Device">}}) can be published together in a public repository for use by everyone. This method generates a transaction to perform a public image of the provided archived block devices. 

#### [deleteByolAttribute](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/deleteByolAttribute)


#### [deleteCloudInitAttribute](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/deleteCloudInitAttribute)


#### [deleteObject](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/deleteObject)
Create a transaction that will remove all block device templates from the group and delete the disk images associated with them. 

#### [denySharingAccess](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/denySharingAccess)
Deny another SoftLayer customer account's previously given access to provision CloudLayer Computing Instances from an image template group. Template access should only be removed from the parent template group object, not the child. 

#### [editObject](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/editObject)
Edit an image template group's name and note.

#### [findGcImagesByCurrentUser](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/findGcImagesByCurrentUser)
Fetch a sorted collection of GC enabled cloudinit images for the account of the current active customer user. 

#### [getAccount](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getAccount)
Retrieve a block device template group's [SoftLayer_Account]({{<ref "reference/datatypes/SoftLayer_Account">}}).

#### [getAccountContacts](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getAccountContacts)


#### [getAccountReferences](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getAccountReferences)
Retrieve the accounts which may have read-only access to an image template group. Will only be populated for parent template group objects.

#### [getAllAvailableCompatiblePlatformNames](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getAllAvailableCompatiblePlatformNames)


#### [getBlockDevices](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getBlockDevices)
Retrieve the block devices that are part of an image template group

#### [getBlockDevicesDiskSpaceTotal](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getBlockDevicesDiskSpaceTotal)
Retrieve the total disk space of all images in a image template group.

#### [getBootMode](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getBootMode)


#### [getByolFlag](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getByolFlag)
Retrieve a flag indicating that customer is providing the software licenses.

#### [getChildren](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getChildren)
Retrieve the image template groups that are clones of an image template group.

#### [getCurrentCompatiblePlatformNames](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getCurrentCompatiblePlatformNames)


#### [getDatacenter](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getDatacenter)
Retrieve the location containing this image template group. Will only be populated for child template group objects.

#### [getDatacenters](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getDatacenters)
Retrieve a collection of locations containing a copy of this image template group. Will only be populated for parent template group objects.

#### [getDefaultBootMode](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getDefaultBootMode)


#### [getEncryptionAttributes](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getEncryptionAttributes)


#### [getFlexImageFlag](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getFlexImageFlag)
Retrieve a flag indicating if this is a flex image.

#### [getGlobalIdentifier](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getGlobalIdentifier)
Retrieve an image template's universally unique identifier.

#### [getImageType](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getImageType)
Retrieve the virtual disk image type of this template. Value will be populated on parent and child, but only supports object filtering on the parent.

#### [getImageTypeKeyName](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getImageTypeKeyName)
Retrieve the virtual disk image type keyname (e.g. SYSTEM, DISK_CAPTURE, ISO, etc) of this template. Value will be populated on parent and child, but only supports object filtering on the parent.

#### [getNextGenFlag](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getNextGenFlag)
Retrieve a flag indicating if this is a next generation image.

#### [getObject](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getObject)
Retrieve a SoftLayer_Virtual_Guest_Block_Device_Template_Group record.

#### [getParent](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getParent)
Retrieve the image template group that another image template group was cloned from.

#### [getPublicCustomerOwnedImages](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getPublicCustomerOwnedImages)
Gets all public customer owned image templates that the user is allowed to see. 

#### [getPublicImages](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getPublicImages)
Gets all public image templates that the user is allowed to see. 

#### [getSshKeys](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getSshKeys)
Retrieve the ssh keys to be implemented on the server when provisioned or reloaded from an image template group.

#### [getStatus](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getStatus)
Retrieve a template group's status.

#### [getStorageLocations](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getStorageLocations)
The available locations for public image storage. 

#### [getStorageRepository](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getStorageRepository)
Retrieve the storage repository that an image template group resides on.

#### [getSupportedBootModes](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getSupportedBootModes)


#### [getTagReferences](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getTagReferences)
Retrieve the tags associated with this image template group.

#### [getTemplateDataCenterName](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getTemplateDataCenterName)


#### [getTransaction](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getTransaction)
Retrieve a transaction that is being performed on a image template group.

#### [getVhdImportSoftwareDescriptions](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getVhdImportSoftwareDescriptions)
Returns the software descriptions supported for VHD imports.

#### [isByol](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/isByol)


#### [isByolCapableOperatingSystem](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/isByolCapableOperatingSystem)


#### [isByolOnlyOperatingSystem](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/isByolOnlyOperatingSystem)


#### [isCloudInit](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/isCloudInit)


#### [isCloudInitOnlyOperatingSystem](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/isCloudInitOnlyOperatingSystem)


#### [isEncrypted](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/isEncrypted)


#### [permitSharingAccess](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/permitSharingAccess)
Permit another SoftLayer customer account access to provision CloudLayer Computing Instances from an image template group. Template access should only be given to the parent template group object, not the child. 

#### [removeCompatiblePlatforms](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/removeCompatiblePlatforms)


#### [removeLocations](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/removeLocations)
[SoftLayer_Virtual_Guest_Block_Device]({{<ref "reference/datatypes/SoftLayer_Virtual_Guest_Block_Device">}}) can be made available in all storage locations. This method will create transaction(s) to remove available locations from an archive image template. 

#### [removeSupportedBootMode](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/removeSupportedBootMode)


#### [setAvailableLocations](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/setAvailableLocations)
This method generates the necessary transaction(s) to set available locations for archived block devices. 

#### [setBootMode](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/setBootMode)


#### [setCompatiblePlatforms](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/setCompatiblePlatforms)


#### [setTags](/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/setTags)
Set the tags for this template group.

</div>

