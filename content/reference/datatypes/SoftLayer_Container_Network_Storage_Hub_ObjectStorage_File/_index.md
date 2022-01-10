---
title: "SoftLayer_Container_Network_Storage_Hub_ObjectStorage_File"
description: "SoftLayer_Container_Network_Storage_Hub_ObjectStorage_File provides specific details that only apply to files that are s... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Network_Storage_Hub_ObjectStorage_File"
---

# SoftLayer_Container_Network_Storage_Hub_ObjectStorage_File
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Network_Storage_Hub_ObjectStorage_File' >Datatype</a></li>
    </ul>
</div>

## Description 


SoftLayer_Container_Network_Storage_Hub_ObjectStorage_File provides specific details that only apply to files that are sent or received from CloudLayer storage resources. 


### associatedMethods

*  [SoftLayer_Network_Storage::uploadFile](/reference/services/SoftLayer_Network_Storage/uploadFile )
*  [SoftLayer_Network_Storage::downloadFile](/reference/services/SoftLayer_Network_Storage/downloadFile )



### seeAlso

* [SoftLayer_Container_Utility_File_Entity](/reference/datatypes/SoftLayer_Container_Utility_File_Entity )




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
[content]: #content
#### [content]
A file entity's raw content.  
<span class="type-label">Type: </span>**binary data**  



</div>
<div class="prop-row">

-----
[contentType]: #contenttype
#### [contentType]
A file entity's MIME content type.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
The date a file entity was created.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[deleteDate]: #deletedate
#### [deleteDate]
The date a CloudLayer storage file entity was moved into the recycle bin. This field applies to files that are pending deletion in the recycle bin.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[folder]: #folder
#### [folder]
  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[hash]: #hash
#### [hash]
  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
Unique identifier for the file. This can be either a number or guid.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[isShared]: #isshared
#### [isShared]
Whether a CloudLayer storage file entity is shared with another CloudLayer user.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date a file entity was last changed.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
A file entity's name.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[owner]: #owner
#### [owner]
The owner is usually the account who first upload or created the file on the resource or the account who is responsible for the file at the moment.   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[size]: #size
#### [size]
The size of a file entity in bytes.  
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[type]: #type
#### [type]
A CloudLayer storage file entity's type. Types can include "file", "folder", "dir", and "project".   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[version]: #version
#### [version]
The latest revision of a file on a CloudLayer storage volume. This number increments each time a new revision of the file is uploaded.   
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


