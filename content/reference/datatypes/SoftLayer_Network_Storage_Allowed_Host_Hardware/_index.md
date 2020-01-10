---
title: "SoftLayer_Network_Storage_Allowed_Host_Hardware"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Allowed_Host_Hardware"
---

# SoftLayer_Network_Storage_Allowed_Host_Hardware
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Storage_Allowed_Host_Hardware' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Storage_Allowed_Host_Hardware' >Datatype</a></li>
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
The account to which this allowed host belongs to.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[credentialId]: #credentialid
#### [credentialId]
The credential this allowed host will use  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
The internal identifier of the igroup  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
The name of allowed host, usually an IQN or other identifier  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[resourceTableId]: #resourcetableid
#### [resourceTableId]
  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[resourceTableName]: #resourcetablename
#### [resourceTableName]
  
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[account]: #account
#### [account]
The SoftLayer_Account object which this SoftLayer_Network_Storage_Allowed_Host belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**


</div>
<div class="prop-row">

-----
[assignedGroups]: #assignedgroups
#### [assignedGroups]
The SoftLayer_Network_Storage_Group objects this SoftLayer_Network_Storage_Allowed_Host is present in.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Group'>SoftLayer_Network_Storage_Group[] </a>**


</div>
<div class="prop-row">

-----
[assignedIscsiVolumes]: #assignediscsivolumes
#### [assignedIscsiVolumes]
The SoftLayer_Network_Storage volumes to which this SoftLayer_Network_Storage_Allowed_Host is allowed access.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**


</div>
<div class="prop-row">

-----
[assignedNfsVolumes]: #assignednfsvolumes
#### [assignedNfsVolumes]
The SoftLayer_Network_Storage volumes to which this SoftLayer_Network_Storage_Allowed_Host is allowed access.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**


</div>
<div class="prop-row">

-----
[assignedReplicationVolumes]: #assignedreplicationvolumes
#### [assignedReplicationVolumes]
The SoftLayer_Network_Storage primary volumes whose replicas are allowed access.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**


</div>
<div class="prop-row">

-----
[assignedVolumes]: #assignedvolumes
#### [assignedVolumes]
The SoftLayer_Network_Storage volumes to which this SoftLayer_Network_Storage_Allowed_Host is allowed access.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**


</div>
<div class="prop-row">

-----
[credential]: #credential
#### [credential]
The SoftLayer_Network_Storage_Credential this allowed host uses.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Credential'>SoftLayer_Network_Storage_Credential </a>**


</div>
<div class="prop-row">

-----
[resource]: #resource
#### [resource]
The SoftLayer_Hardware object which this SoftLayer_Network_Storage_Allowed_Host is referencing.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>**


</div>
<div class="prop-row">

-----
[sourceSubnet]: #sourcesubnet
#### [sourceSubnet]
Connections to a target with a source IP in this subnet prefix are allowed.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[subnetsInAcl]: #subnetsinacl
#### [subnetsInAcl]
The SoftLayer_Network_Subnet records assigned to the ACL for this allowed host.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a>**


</div>

## Count
<div class="prop-row">

-----
[assignedGroupCount]: #assignedgroupcount
#### [assignedGroupCount]
A count of the SoftLayer_Network_Storage_Group objects this SoftLayer_Network_Storage_Allowed_Host is present in.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[assignedIscsiVolumeCount]: #assignediscsivolumecount
#### [assignedIscsiVolumeCount]
A count of the SoftLayer_Network_Storage volumes to which this SoftLayer_Network_Storage_Allowed_Host is allowed access.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[assignedNfsVolumeCount]: #assignednfsvolumecount
#### [assignedNfsVolumeCount]
A count of the SoftLayer_Network_Storage volumes to which this SoftLayer_Network_Storage_Allowed_Host is allowed access.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[assignedReplicationVolumeCount]: #assignedreplicationvolumecount
#### [assignedReplicationVolumeCount]
A count of the SoftLayer_Network_Storage primary volumes whose replicas are allowed access.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[assignedVolumeCount]: #assignedvolumecount
#### [assignedVolumeCount]
A count of the SoftLayer_Network_Storage volumes to which this SoftLayer_Network_Storage_Allowed_Host is allowed access.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[subnetsInAclCount]: #subnetsinaclcount
#### [subnetsInAclCount]
A count of the SoftLayer_Network_Subnet records assigned to the ACL for this allowed host.   
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


