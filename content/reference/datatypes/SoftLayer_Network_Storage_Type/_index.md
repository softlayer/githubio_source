---
title: "SoftLayer_Network_Storage_Type"
description: "The SoftLayer_Network_Storage_Type contains a description of the associated SoftLayer_Network_Storage object."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Type"
---

# SoftLayer_Network_Storage_Type
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Storage_Type' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_Storage_Type contains a description of the associated SoftLayer_Network_Storage object. 





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
[description]: #description
#### [description]
Human readable description for the associated SoftLayer_Network_Storage object.   
<span class="type-label">Type: </span>**string**

-----
[id]: #id
#### [id]
ID which corresponds with storageTypeId on storage objects.   
<span class="type-label">Type: </span>**integer**

-----
[keyName]: #keyname
#### [keyName]
Machine readable description code for the associated SoftLayer_Network_Storage object.   
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[volumes]: #volumes
#### [volumes]
The SoftLayer_Network_Storage object that uses this type.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**


## Count

-----
[volumeCount]: #volumecount
#### [volumeCount]
A count of the SoftLayer_Network_Storage object that uses this type.   
<span class="type-label">Type: </span>**unsigned long**

</div>


