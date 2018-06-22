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



        
<div id="properties" class="content">
    <h2>Methods</h2>
    <div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                    type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
    </div>
    <div id="method-div">
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/addByolAttribute'> addByolAttribute</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/addCloudInitAttribute'> addCloudInitAttribute</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/addLocations'> addLocations</a> </span>
            <div class='views-field-body'>[[SoftLayer_Virtual_Guest_Block_Devices|Block Devices]] can be made available in all storage locations. This method will create transaction(s) to add available locations to an archive image template. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/addSupportedBootMode'> addSupportedBootMode</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/copyToExternalSource'> copyToExternalSource</a> </span>
            <div class='views-field-body'>This method generates a transaction to export/copy a template to an external source. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/createFromExternalSource'> createFromExternalSource</a> </span>
            <div class='views-field-body'>This method generates a transaction to import a disk image from an external source and create a standard image template. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/createPublicArchiveTransaction'> createPublicArchiveTransaction</a> </span>
            <div class='views-field-body'>[[SoftLayer_Virtual_Guest_Block_Devices|Block Devices]] can be published together in a public repository for use by everyone. This method generates a transaction to perform a public image of the provided archived block devices. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/deleteByolAttribute'> deleteByolAttribute</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/deleteCloudInitAttribute'> deleteCloudInitAttribute</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/deleteObject'> deleteObject</a> </span>
            <div class='views-field-body'>Create a transaction that will remove all block device templates from the group and delete the disk images associated with them. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/denySharingAccess'> denySharingAccess</a> </span>
            <div class='views-field-body'>Deny another SoftLayer customer account's previously given access to provision CloudLayer Computing Instances from an image template group. Template access should only be removed from the parent template group object, not the child. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/editObject'> editObject</a> </span>
            <div class='views-field-body'>Edit an image template group's name and note.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/findGcImagesByCurrentUser'> findGcImagesByCurrentUser</a> </span>
            <div class='views-field-body'>Fetch collection of GC enabled images for the account of the current active customer user. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getAccount'> getAccount</a> </span>
            <div class='views-field-body'>Retrieve a block device template group's [[SoftLayer_Account|account]].</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getAccountContacts'> getAccountContacts</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getAccountReferences'> getAccountReferences</a> </span>
            <div class='views-field-body'>Retrieve the accounts which may have read-only access to an image template group. Will only be populated for parent template group objects.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getBlockDevices'> getBlockDevices</a> </span>
            <div class='views-field-body'>Retrieve the block devices that are part of an image template group</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getBlockDevicesDiskSpaceTotal'> getBlockDevicesDiskSpaceTotal</a> </span>
            <div class='views-field-body'>Retrieve the total disk space of all images in a image template group.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getBootMode'> getBootMode</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getByolFlag'> getByolFlag</a> </span>
            <div class='views-field-body'>Retrieve a flag indicating that customer is providing the software licenses.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getChildren'> getChildren</a> </span>
            <div class='views-field-body'>Retrieve the image template groups that are clones of an image template group.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getDatacenter'> getDatacenter</a> </span>
            <div class='views-field-body'>Retrieve the location containing this image template group. Will only be populated for child template group objects.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getDatacenters'> getDatacenters</a> </span>
            <div class='views-field-body'>Retrieve a collection of locations containing a copy of this image template group. Will only be populated for parent template group objects.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getDefaultBootMode'> getDefaultBootMode</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getEncryptionAttributes'> getEncryptionAttributes</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getFlexImageFlag'> getFlexImageFlag</a> </span>
            <div class='views-field-body'>Retrieve a flag indicating if this is a flex image.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getGlobalIdentifier'> getGlobalIdentifier</a> </span>
            <div class='views-field-body'>Retrieve an image template's universally unique identifier.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getImageType'> getImageType</a> </span>
            <div class='views-field-body'>Retrieve the virtual disk image type of this template. Value will be populated on parent and child, but only supports object filtering on the parent.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getImageTypeKeyName'> getImageTypeKeyName</a> </span>
            <div class='views-field-body'>Retrieve the virtual disk image type keyname (e.g. SYSTEM, DISK_CAPTURE, ISO, etc) of this template. Value will be populated on parent and child, but only supports object filtering on the parent.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Virtual_Guest_Block_Device_Template_Group record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getParent'> getParent</a> </span>
            <div class='views-field-body'>Retrieve the image template group that another image template group was cloned from.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getPublicCustomerOwnedImages'> getPublicCustomerOwnedImages</a> </span>
            <div class='views-field-body'>Gets all public customer owned image templates that the user is allowed to see. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getPublicImages'> getPublicImages</a> </span>
            <div class='views-field-body'>Gets all public image templates that the user is allowed to see. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getSshKeys'> getSshKeys</a> </span>
            <div class='views-field-body'>Retrieve the ssh keys to be implemented on the server when provisioned or reloaded from an image template group.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getStatus'> getStatus</a> </span>
            <div class='views-field-body'>Retrieve a template group's status.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getStorageLocations'> getStorageLocations</a> </span>
            <div class='views-field-body'>The available locations for public image storage. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getStorageRepository'> getStorageRepository</a> </span>
            <div class='views-field-body'>Retrieve the storage repository that an image template group resides on.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getSupportedBootModes'> getSupportedBootModes</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getTagReferences'> getTagReferences</a> </span>
            <div class='views-field-body'>Retrieve the tags associated with this image template group.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getTransaction'> getTransaction</a> </span>
            <div class='views-field-body'>Retrieve a transaction that is being performed on a image template group.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/getVhdImportSoftwareDescriptions'> getVhdImportSoftwareDescriptions</a> </span>
            <div class='views-field-body'>Returns the software descriptions supported for VHD imports.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/isByol'> isByol</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/isByolCapableOperatingSystem'> isByolCapableOperatingSystem</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/isByolOnlyOperatingSystem'> isByolOnlyOperatingSystem</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/isCloudInit'> isCloudInit</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/isCloudInitOnlyOperatingSystem'> isCloudInitOnlyOperatingSystem</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/isEncrypted'> isEncrypted</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/permitSharingAccess'> permitSharingAccess</a> </span>
            <div class='views-field-body'>Permit another SoftLayer customer account access to provision CloudLayer Computing Instances from an image template group. Template access should only be given to the parent template group object, not the child. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/removeLocations'> removeLocations</a> </span>
            <div class='views-field-body'>[[SoftLayer_Virtual_Guest_Block_Devices|Block Devices]] can be made available in all storage locations. This method will create transaction(s) to remove available locations from an archive image template. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/removeSupportedBootMode'> removeSupportedBootMode</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/setAvailableLocations'> setAvailableLocations</a> </span>
            <div class='views-field-body'>This method generates the necessary transaction(s) to set available locations for archived block devices. </div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/setBootMode'> setBootMode</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Virtual_Guest_Block_Device_Template_Group/setTags'> setTags</a> </span>
            <div class='views-field-body'>Set the tags for this template group.</div>
        </div>
        </div>
</div>

