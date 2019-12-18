---
title: "SoftLayer_Container_Utility_File_Entity"
description: "SoftLayer_Container_Utility_File_Entity data type models a single entity on a storage resource. Entities can include any... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Utility_File_Entity"
---

# SoftLayer_Container_Utility_File_Entity
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Utility_File_Entity' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer_Container_Utility_File_Entity data type models a single entity on a storage resource. Entities can include anything within a storage volume including files, folders, directories, and CloudLayer storage projects. 

### External Links


* [Internet media type at Wikipedia](http://en.wikipedia.org/wiki/Internet_media_type)



### associatedMethods

*  [SoftLayer_Network_Storage::uploadFile](/reference/services/SoftLayer_Network_Storage/uploadFile )
*  [SoftLayer_Network_Storage::downloadFile](/reference/services/SoftLayer_Network_Storage/downloadFile )
*  [SoftLayer_Network_Storage::getAllFiles](/reference/services/SoftLayer_Network_Storage/getAllFiles )
*  [SoftLayer_Network_Storage::getFileByIdentifier](/reference/services/SoftLayer_Network_Storage/getFileByIdentifier )
*  [SoftLayer_Network_Storage::restoreFile](/reference/services/SoftLayer_Network_Storage/restoreFile )
*  [SoftLayer_Network_Storage::getFilesPendingDelete](/reference/services/SoftLayer_Network_Storage/getFilesPendingDelete )
*  [SoftLayer_Network_Storage::getRecycleBinFileByIdentifier](/reference/services/SoftLayer_Network_Storage/getRecycleBinFileByIdentifier )





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
[content]: #content
#### [content]
A file entity's raw content.  
<span class="type-label">Type: </span>**binary data**

-----
[contentType]: #contenttype
#### [contentType]
A file entity's MIME content type.  
<span class="type-label">Type: </span>**string**

-----
[createDate]: #createdate
#### [createDate]
The date a file entity was created.  
<span class="type-label">Type: </span>**dateTime**

-----
[deleteDate]: #deletedate
#### [deleteDate]
The date a CloudLayer storage file entity was moved into the recycle bin. This field applies to files that are pending deletion in the recycle bin.  
<span class="type-label">Type: </span>**dateTime**

-----
[id]: #id
#### [id]
Unique identifier for the file. This can be either a number or guid.  
<span class="type-label">Type: </span>**string**

-----
[isShared]: #isshared
#### [isShared]
Whether a CloudLayer storage file entity is shared with another CloudLayer user.  
<span class="type-label">Type: </span>**integer**

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date a file entity was last changed.  
<span class="type-label">Type: </span>**dateTime**

-----
[name]: #name
#### [name]
A file entity's name.  
<span class="type-label">Type: </span>**string**

-----
[owner]: #owner
#### [owner]
The owner is usually the account who first upload or created the file on the resource or the account who is responsible for the file at the moment.   
<span class="type-label">Type: </span>**string**

-----
[size]: #size
#### [size]
The size of a file entity in bytes.  
<span class="type-label">Type: </span>**unsigned long**

-----
[type]: #type
#### [type]
A CloudLayer storage file entity's type. Types can include "file", "folder", "dir", and "project".   
<span class="type-label">Type: </span>**string**

-----
[version]: #version
#### [version]
The latest revision of a file on a CloudLayer storage volume. This number increments each time a new revision of the file is uploaded.   
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

</div>


