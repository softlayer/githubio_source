---
title: "SoftLayer_Configuration_Storage_Group"
description: "This class describes the base Storage Group for a Complex Drive Configuration"
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Configuration"
classes:
    - "SoftLayer_Configuration_Storage_Group"
---

# SoftLayer_Configuration_Storage_Group
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Configuration_Storage_Group' >Datatype</a></li>
    </ul>
</div>

## Description 
This class describes the base Storage Group for a Complex Drive Configuration 





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
[description]: #description
#### [description]
Storage group description   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[diskSpace]: #diskspace
#### [diskSpace]
Storage group disk space   
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
Storage group type id   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[lvmFlag]: #lvmflag
#### [lvmFlag]
Flag to indicate if the storage group is setup for lvm   
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
Storage group name   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[units]: #units
#### [units]
Storage group disk size units   
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[ancestorGroups]: #ancestorgroups
#### [ancestorGroups]
This class represents a storage groups ancestors  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Storage_Group'>SoftLayer_Configuration_Storage_Group[] </a>**


</div>
<div class="prop-row">

-----
[arrayType]: #arraytype
#### [arrayType]
This class represents a storage group disk array type  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Storage_Group_Array_Type'>SoftLayer_Configuration_Storage_Group_Array_Type </a>**


</div>
<div class="prop-row">

-----
[captureEnabledFlag]: #captureenabledflag
#### [captureEnabledFlag]
Determine if the storage group is able to be image captured. If unable to image capture the reasons will be provided.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[createEmployee]: #createemployee
#### [createEmployee]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Employee'>SoftLayer_User_Employee </a>**


</div>
<div class="prop-row">

-----
[descendantGroups]: #descendantgroups
#### [descendantGroups]
This class represents a storage groups descendants  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Storage_Group'>SoftLayer_Configuration_Storage_Group[] </a>**


</div>
<div class="prop-row">

-----
[hardDrives]: #harddrives
#### [hardDrives]
The hard drives contained within this storage group.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component[] </a>**


</div>

## Count
<div class="prop-row">

-----
[ancestorGroupCount]: #ancestorgroupcount
#### [ancestorGroupCount]
A count of this class represents a storage groups ancestors   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[descendantGroupCount]: #descendantgroupcount
#### [descendantGroupCount]
A count of this class represents a storage groups descendants   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[hardDriveCount]: #harddrivecount
#### [hardDriveCount]
A count of the hard drives contained within this storage group.   
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


