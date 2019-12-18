---
title: "SoftLayer_Virtual_Guest_Block_Device_Template_Group"
description: "The virtual block device template group data type presents the structure in which a group of archived image templates wi... "
layout: "datatype"
tags:
    - "datatype"
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
The virtual block device template group data type presents the structure in which a group of archived image templates will be presented. The structure consists of a parent template group which contain multiple child template group objects.  Each child template group object represents the image template in a particular location. Unless editing/deleting a specific child template group object, it is best to use the parent object. 

A virtual block device template group, also known as an image template group, represents an image of a virtual guest instance. 





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
[accountId]: #accountid
#### [accountId]
A block device template group's [SoftLayer_Account]({{<ref "reference/datatypes/SoftLayer_Account">}}) ID   
<span class="type-label">Type: </span>**integer**

-----
[createDate]: #createdate
#### [createDate]
The date a block device template group was created.   
<span class="type-label">Type: </span>**dateTime**

-----
[id]: #id
#### [id]
A block device template group's unique ID.   
<span class="type-label">Type: </span>**integer**

-----
[name]: #name
#### [name]
A user definable and optional name of a block device template group.   
<span class="type-label">Type: </span>**string**

-----
[note]: #note
#### [note]
A block device template group's user defined note.   
<span class="type-label">Type: </span>**string**

-----
[parentId]: #parentid
#### [parentId]
A block device template group's [SoftLayer_Virtual_Guest_Block_Device_Template_Group]({{<ref "reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group">}}) ID.  This will only be set when a template group is created from a previously existing template group   
<span class="type-label">Type: </span>**integer**

-----
[publicFlag]: #publicflag
#### [publicFlag]
  
<span class="type-label">Type: </span>**integer**

-----
[statusId]: #statusid
#### [statusId]
A block device template group's [SoftLayer_Virtual_Guest_Block_Device_Template_Group_Status]({{<ref "reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group_Status">}}) ID   
<span class="type-label">Type: </span>**integer**

-----
[summary]: #summary
#### [summary]
A block device template group's user defined summary.   
<span class="type-label">Type: </span>**string**

-----
[transactionId]: #transactionid
#### [transactionId]
A block device template group's [SoftLayer_Provisioning_Version1_Transaction]({{<ref "reference/datatypes/SoftLayer_Provisioning_Version1_Transaction">}}) ID.  This will only be set when there is a transaction being performed on the block device template group.   
<span class="type-label">Type: </span>**integer**

-----
[userRecordId]: #userrecordid
#### [userRecordId]
A block device template group's [SoftLayer_User_Customer]({{<ref "reference/datatypes/SoftLayer_User_Customer">}}) ID   
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
A block device template group's [SoftLayer_Account]({{<ref "reference/datatypes/SoftLayer_Account">}}).  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[accountContacts]: #accountcontacts
#### [accountContacts]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Contact'>SoftLayer_Account_Contact[] </a>**

-----
[accountReferences]: #accountreferences
#### [accountReferences]
The accounts which may have read-only access to an image template group. Will only be populated for parent template group objects.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group_Accounts'>SoftLayer_Virtual_Guest_Block_Device_Template_Group_Accounts[] </a>**

-----
[blockDevices]: #blockdevices
#### [blockDevices]
The block devices that are part of an image template group  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template'>SoftLayer_Virtual_Guest_Block_Device_Template[] </a>**

-----
[blockDevicesDiskSpaceTotal]: #blockdevicesdiskspacetotal
#### [blockDevicesDiskSpaceTotal]
The total disk space of all images in a image template group.  
<span class="type-label">Type: </span>**float**

-----
[byolFlag]: #byolflag
#### [byolFlag]
A flag indicating that customer is providing the software licenses.  
<span class="type-label">Type: </span>**boolean**

-----
[children]: #children
#### [children]
The image template groups that are clones of an image template group.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group'>SoftLayer_Virtual_Guest_Block_Device_Template_Group[] </a>**

-----
[datacenter]: #datacenter
#### [datacenter]
The location containing this image template group. Will only be populated for child template group objects.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**

-----
[datacenters]: #datacenters
#### [datacenters]
A collection of locations containing a copy of this image template group. Will only be populated for parent template group objects.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location[] </a>**

-----
[flexImageFlag]: #fleximageflag
#### [flexImageFlag]
A flag indicating if this is a flex image.  
<span class="type-label">Type: </span>**boolean**

-----
[globalIdentifier]: #globalidentifier
#### [globalIdentifier]
An image template's universally unique identifier.  
<span class="type-label">Type: </span>**string**

-----
[imageType]: #imagetype
#### [imageType]
The virtual disk image type of this template. Value will be populated on parent and child, but only supports object filtering on the parent.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Disk_Image_Type'>SoftLayer_Virtual_Disk_Image_Type </a>**

-----
[imageTypeKeyName]: #imagetypekeyname
#### [imageTypeKeyName]
The virtual disk image type keyname (e.g. SYSTEM, DISK_CAPTURE, ISO, etc) of this template. Value will be populated on parent and child, but only supports object filtering on the parent.  
<span class="type-label">Type: </span>**string**

-----
[nextGenFlag]: #nextgenflag
#### [nextGenFlag]
A flag indicating if this is a next generation image.  
<span class="type-label">Type: </span>**boolean**

-----
[parent]: #parent
#### [parent]
The image template group that another image template group was cloned from.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group'>SoftLayer_Virtual_Guest_Block_Device_Template_Group </a>**

-----
[sshKeys]: #sshkeys
#### [sshKeys]
The ssh keys to be implemented on the server when provisioned or reloaded from an image template group.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Security_Ssh_Key'>SoftLayer_Security_Ssh_Key[] </a>**

-----
[status]: #status
#### [status]
A template group's status.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest_Block_Device_Template_Group_Status'>SoftLayer_Virtual_Guest_Block_Device_Template_Group_Status </a>**

-----
[storageRepository]: #storagerepository
#### [storageRepository]
The storage repository that an image template group resides on.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Storage_Repository'>SoftLayer_Virtual_Storage_Repository </a>**

-----
[tagReferences]: #tagreferences
#### [tagReferences]
The tags associated with this image template group.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Tag_Reference'>SoftLayer_Tag_Reference[] </a>**

-----
[transaction]: #transaction
#### [transaction]
A transaction that is being performed on a image template group.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction </a>**


## Count

-----
[accountContactCount]: #accountcontactcount
#### [accountContactCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[accountReferenceCount]: #accountreferencecount
#### [accountReferenceCount]
A count of the accounts which may have read-only access to an image template group. Will only be populated for parent template group objects.   
<span class="type-label">Type: </span>**unsigned long**


-----
[blockDeviceCount]: #blockdevicecount
#### [blockDeviceCount]
A count of the block devices that are part of an image template group   
<span class="type-label">Type: </span>**unsigned long**


-----
[childrenCount]: #childrencount
#### [childrenCount]
A count of the image template groups that are clones of an image template group.   
<span class="type-label">Type: </span>**unsigned long**


-----
[datacenterCount]: #datacentercount
#### [datacenterCount]
A count of a collection of locations containing a copy of this image template group. Will only be populated for parent template group objects.   
<span class="type-label">Type: </span>**unsigned long**


-----
[sshKeyCount]: #sshkeycount
#### [sshKeyCount]
A count of the ssh keys to be implemented on the server when provisioned or reloaded from an image template group.   
<span class="type-label">Type: </span>**unsigned long**


-----
[tagReferenceCount]: #tagreferencecount
#### [tagReferenceCount]
A count of the tags associated with this image template group.   
<span class="type-label">Type: </span>**unsigned long**

</div>


