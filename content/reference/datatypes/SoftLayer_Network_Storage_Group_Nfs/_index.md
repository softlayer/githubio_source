---
title: "SoftLayer_Network_Storage_Group_Nfs"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Group_Nfs"
---

# SoftLayer_Network_Storage_Group_Nfs
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Storage_Group_Nfs' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Storage_Group_Nfs' >Datatype</a></li>
    </ul>
</div>

## Description 






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
The account ID which owns this group  
<span class="type-label">Type: </span>**integer**

-----
[alias]: #alias
#### [alias]
The friendly name of this group  
<span class="type-label">Type: </span>**string**

-----
[createDate]: #createdate
#### [createDate]
The date this group was created.  
<span class="type-label">Type: </span>**dateTime**

-----
[groupTypeId]: #grouptypeid
#### [groupTypeId]
The SoftLayer_Network_Storage_Group_Type which describes this group.  
<span class="type-label">Type: </span>**integer**

-----
[id]: #id
#### [id]
The internal identifier of the group  
<span class="type-label">Type: </span>**integer**

-----
[modifyDate]: #modifydate
#### [modifyDate]
  
<span class="type-label">Type: </span>**dateTime**

-----
[osTypeId]: #ostypeid
#### [osTypeId]
A SoftLayer_Network_Storage_OS_Type Operating System designation that this group was created for.  
<span class="type-label">Type: </span>**integer**

-----
[serviceResourceId]: #serviceresourceid
#### [serviceResourceId]
A SoftLayer_Network_Service_Resource that this group was created on.  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
The SoftLayer_Account which owns this group.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[allowedHosts]: #allowedhosts
#### [allowedHosts]
The allowed hosts list for this group.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Allowed_Host'>SoftLayer_Network_Storage_Allowed_Host[] </a>**

-----
[attachedVolumes]: #attachedvolumes
#### [attachedVolumes]
The network storage volumes this group is attached to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**

-----
[groupType]: #grouptype
#### [groupType]
The type which defines this group.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Group_Type'>SoftLayer_Network_Storage_Group_Type </a>**

-----
[osType]: #ostype
#### [osType]
The OS Type this group is configured for.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Iscsi_OS_Type'>SoftLayer_Network_Storage_Iscsi_OS_Type </a>**

-----
[serviceResource]: #serviceresource
#### [serviceResource]
The network resource this group is created on.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Service_Resource'>SoftLayer_Network_Service_Resource </a>**


## Count

-----
[allowedHostCount]: #allowedhostcount
#### [allowedHostCount]
A count of the allowed hosts list for this group.   
<span class="type-label">Type: </span>**unsigned long**


-----
[attachedVolumeCount]: #attachedvolumecount
#### [attachedVolumeCount]
A count of the network storage volumes this group is attached to.   
<span class="type-label">Type: </span>**unsigned long**

</div>


