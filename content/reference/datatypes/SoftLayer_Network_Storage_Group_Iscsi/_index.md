---
title: "SoftLayer_Network_Storage_Group_Iscsi"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Group_Iscsi"
---

# SoftLayer_Network_Storage_Group_Iscsi
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Storage_Group_Iscsi' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Storage_Group_Iscsi' >Datatype</a></li>
    </ul>
</div>

## Description 








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
[accountId]: #accountid
#### [accountId]
The account ID which owns this group  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[alias]: #alias
#### [alias]
The friendly name of this group  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
The date this group was created.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[groupTypeId]: #grouptypeid
#### [groupTypeId]
The SoftLayer_Network_Storage_Group_Type which describes this group.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
The internal identifier of the group  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[osTypeId]: #ostypeid
#### [osTypeId]
A SoftLayer_Network_Storage_OS_Type Operating System designation that this group was created for.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[serviceResourceId]: #serviceresourceid
#### [serviceResourceId]
A SoftLayer_Network_Service_Resource that this group was created on.  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[account]: #account
#### [account]
The SoftLayer_Account which owns this group.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**  



</div>
<div class="prop-row">

-----
[allowedHosts]: #allowedhosts
#### [allowedHosts]
The allowed hosts list for this group.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Allowed_Host'>SoftLayer_Network_Storage_Allowed_Host[] </a>**  



</div>
<div class="prop-row">

-----
[attachedVolumes]: #attachedvolumes
#### [attachedVolumes]
The network storage volumes this group is attached to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**  



</div>
<div class="prop-row">

-----
[groupType]: #grouptype
#### [groupType]
The type which defines this group.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Group_Type'>SoftLayer_Network_Storage_Group_Type </a>**  



</div>
<div class="prop-row">

-----
[osType]: #ostype
#### [osType]
The OS Type this group is configured for.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Iscsi_OS_Type'>SoftLayer_Network_Storage_Iscsi_OS_Type </a>**  



</div>
<div class="prop-row">

-----
[serviceResource]: #serviceresource
#### [serviceResource]
The network resource this group is created on.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Service_Resource'>SoftLayer_Network_Service_Resource </a>**  



</div>

## Count
<div class="prop-row">

-----
[allowedHostCount]: #allowedhostcount
#### [allowedHostCount]
A count of the allowed hosts list for this group.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[attachedVolumeCount]: #attachedvolumecount
#### [attachedVolumeCount]
A count of the network storage volumes this group is attached to.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>


