---
title: "SoftLayer_Container_Network_Directory_Listing"
description: "SoftLayer_Container_Network_Directory_Listing represents a single entry in a listing of files within a remote directory.... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Network_Directory_Listing"
---

# SoftLayer_Container_Network_Directory_Listing
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Network_Directory_Listing' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer_Container_Network_Directory_Listing represents a single entry in a listing of files within a remote directory. API methods that return remote directory listings typically return arrays of SoftLayer_Container_Network_Directory_Listing objects. 


### associatedMethods

*  [SoftLayer_Network_ContentDelivery_Account::getDirectoryListing](/reference/services/SoftLayer_Network_ContentDelivery_Account/getDirectoryListing )





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
[fileCount]: #filecount
#### [fileCount]
If the file in a directory listing is a directory itself then fileCount is the number of files within the directory.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
The name of a directory or a file within a directory listing.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[type]: #type
#### [type]
The type of file in a directory listing. If a directory listing entry is a directory itself then type is set to "directory". Otherwise, type is a blank string.   
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


