---
title: "SoftLayer_Network_Storage_Allowed_Host_VirtualGuest"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Allowed_Host_VirtualGuest"
---

# SoftLayer_Network_Storage_Allowed_Host_VirtualGuest
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Storage_Allowed_Host_VirtualGuest' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Storage_Allowed_Host_VirtualGuest' >Datatype</a></li>
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
The account to which this allowed host belongs to.  
<span class="type-label">Type: </span>**integer**

-----
[credentialId]: #credentialid
#### [credentialId]
The credential this allowed host will use  
<span class="type-label">Type: </span>**integer**

-----
[id]: #id
#### [id]
The internal identifier of the igroup  
<span class="type-label">Type: </span>**integer**

-----
[name]: #name
#### [name]
The name of allowed host, usually an IQN or other identifier  
<span class="type-label">Type: </span>**string**

-----
[resourceTableId]: #resourcetableid
#### [resourceTableId]
  
<span class="type-label">Type: </span>**integer**

-----
[resourceTableName]: #resourcetablename
#### [resourceTableName]
  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
The SoftLayer_Account object which this SoftLayer_Network_Storage_Allowed_Host belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[assignedGroups]: #assignedgroups
#### [assignedGroups]
The SoftLayer_Network_Storage_Group objects this SoftLayer_Network_Storage_Allowed_Host is present in.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Group'>SoftLayer_Network_Storage_Group[] </a>**

-----
[assignedIscsiVolumes]: #assignediscsivolumes
#### [assignedIscsiVolumes]
The SoftLayer_Network_Storage volumes to which this SoftLayer_Network_Storage_Allowed_Host is allowed access.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**

-----
[assignedNfsVolumes]: #assignednfsvolumes
#### [assignedNfsVolumes]
The SoftLayer_Network_Storage volumes to which this SoftLayer_Network_Storage_Allowed_Host is allowed access.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**

-----
[assignedReplicationVolumes]: #assignedreplicationvolumes
#### [assignedReplicationVolumes]
The SoftLayer_Network_Storage primary volumes whose replicas are allowed access.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**

-----
[assignedVolumes]: #assignedvolumes
#### [assignedVolumes]
The SoftLayer_Network_Storage volumes to which this SoftLayer_Network_Storage_Allowed_Host is allowed access.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**

-----
[credential]: #credential
#### [credential]
The SoftLayer_Network_Storage_Credential this allowed host uses.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Credential'>SoftLayer_Network_Storage_Credential </a>**

-----
[resource]: #resource
#### [resource]
The SoftLayer_Virtual_Guest object which this SoftLayer_Network_Storage_Allowed_Host is referencing.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest </a>**

-----
[sourceSubnet]: #sourcesubnet
#### [sourceSubnet]
Connections to a target with a source IP in this subnet prefix are allowed.  
<span class="type-label">Type: </span>**string**

-----
[subnetsInAcl]: #subnetsinacl
#### [subnetsInAcl]
The SoftLayer_Network_Subnet records assigned to the ACL for this allowed host.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a>**


## Count

-----
[assignedGroupCount]: #assignedgroupcount
#### [assignedGroupCount]
A count of the SoftLayer_Network_Storage_Group objects this SoftLayer_Network_Storage_Allowed_Host is present in.   
<span class="type-label">Type: </span>**unsigned long**


-----
[assignedIscsiVolumeCount]: #assignediscsivolumecount
#### [assignedIscsiVolumeCount]
A count of the SoftLayer_Network_Storage volumes to which this SoftLayer_Network_Storage_Allowed_Host is allowed access.   
<span class="type-label">Type: </span>**unsigned long**


-----
[assignedNfsVolumeCount]: #assignednfsvolumecount
#### [assignedNfsVolumeCount]
A count of the SoftLayer_Network_Storage volumes to which this SoftLayer_Network_Storage_Allowed_Host is allowed access.   
<span class="type-label">Type: </span>**unsigned long**


-----
[assignedReplicationVolumeCount]: #assignedreplicationvolumecount
#### [assignedReplicationVolumeCount]
A count of the SoftLayer_Network_Storage primary volumes whose replicas are allowed access.   
<span class="type-label">Type: </span>**unsigned long**


-----
[assignedVolumeCount]: #assignedvolumecount
#### [assignedVolumeCount]
A count of the SoftLayer_Network_Storage volumes to which this SoftLayer_Network_Storage_Allowed_Host is allowed access.   
<span class="type-label">Type: </span>**unsigned long**


-----
[subnetsInAclCount]: #subnetsinaclcount
#### [subnetsInAclCount]
A count of the SoftLayer_Network_Subnet records assigned to the ACL for this allowed host.   
<span class="type-label">Type: </span>**unsigned long**

</div>


