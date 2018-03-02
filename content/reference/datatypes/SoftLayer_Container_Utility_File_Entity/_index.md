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
        <h2>Local</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#content" name=content>content</a></span>
            <div class='views-field-body'>A file entity's raw content. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>binary data</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#contentType" name=contentType>contentType</a></span>
            <div class='views-field-body'>A file entity's MIME content type. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#createDate" name=createDate>createDate</a></span>
            <div class='views-field-body'>The date a file entity was created. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#deleteDate" name=deleteDate>deleteDate</a></span>
            <div class='views-field-body'>The date a CloudLayer storage file entity was moved into the recycle bin. This field applies to files that are pending deletion in the recycle bin. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>Unique identifier for the file. This can be either a number or guid. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#isShared" name=isShared>isShared</a></span>
            <div class='views-field-body'>Whether a CloudLayer storage file entity is shared with another CloudLayer user. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#modifyDate" name=modifyDate>modifyDate</a></span>
            <div class='views-field-body'>The date a file entity was last changed. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#name" name=name>name</a></span>
            <div class='views-field-body'>A file entity's name. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#owner" name=owner>owner</a></span>
            <div class='views-field-body'>The owner is usually the account who first upload or created the file on the resource or the account who is responsible for the file at the moment.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#size" name=size>size</a></span>
            <div class='views-field-body'>The size of a file entity in bytes. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsigned long</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#type" name=type>type</a></span>
            <div class='views-field-body'>A CloudLayer storage file entity's type. Types can include "file", "folder", "dir", and "project".  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#version" name=version>version</a></span>
            <div class='views-field-body'>The latest revision of a file on a CloudLayer storage volume. This number increments each time a new revision of the file is uploaded.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
    </div>


