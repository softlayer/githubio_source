---
title: "SoftLayer_Network_Storage_Partnership"
description: "A network storage partnership is used to link multiple volumes to each other. These partnerships describe replication hi... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Partnership"
---

# SoftLayer_Network_Storage_Partnership
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Storage_Partnership' >Datatype</a></li>
    </ul>
</div>

## Description 
A network storage partnership is used to link multiple volumes to each other. These partnerships describe replication hierarchies or link volume snapshots to their associated storage volume. 





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
[createDate]: #createdate
#### [createDate]
The date a partnership was created.  
<span class="type-label">Type: </span>**dateTime**

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date a partnership was last modified.  
<span class="type-label">Type: </span>**dateTime**

-----
[partnerVolumeId]: #partnervolumeid
#### [partnerVolumeId]
The child volume id which a partnership is associated with.  
<span class="type-label">Type: </span>**integer**

-----
[volumeId]: #volumeid
#### [volumeId]
The volume id which a partnership is associated with.  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[partnerVolume]: #partnervolume
#### [partnerVolume]
The associated child volume for a partnership.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage </a>**

-----
[type]: #type
#### [type]
The type provides a standardized definition for a partnership.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Partnership_Type'>SoftLayer_Network_Storage_Partnership_Type </a>**

-----
[volume]: #volume
#### [volume]
The associated parent volume for a partnership.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage </a>**


## Count
</div>


