---
title: "SoftLayer_Network_Storage_Credential"
description: "The SoftLayer_Network_Storage_Credential data type will give you an overview of the usernames that are currently attache... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Credential"
---

# SoftLayer_Network_Storage_Credential
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Storage_Credential' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_Storage_Credential data type will give you an overview of the usernames that are currently attached to your storage device. 





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
This is the account id associated with the volume.   
<span class="type-label">Type: </span>**string**

-----
[createDate]: #createdate
#### [createDate]
This is the data that the record was created in the table.   
<span class="type-label">Type: </span>**dateTime**

-----
[id]: #id
#### [id]
  
<span class="type-label">Type: </span>**integer**

-----
[modifyDate]: #modifydate
#### [modifyDate]
This is the date that the record was last updated in the table.   
<span class="type-label">Type: </span>**dateTime**

-----
[nasCredentialTypeId]: #nascredentialtypeid
#### [nasCredentialTypeId]
This is the id of the type of credential that this object represents.   
<span class="type-label">Type: </span>**integer**

-----
[password]: #password
#### [password]
This is the password associated with the volume.   
<span class="type-label">Type: </span>**string**

-----
[username]: #username
#### [username]
This is the username associated with the volume.   
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
This is the account that the storage credential is tied to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[networkStorageAllowedHosts]: #networkstorageallowedhosts
#### [networkStorageAllowedHosts]
These are the SoftLayer_Network_Storage_Allowed_Host entries that this credential is assigned to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Allowed_Host'>SoftLayer_Network_Storage_Allowed_Host </a>**

-----
[type]: #type
#### [type]
These are the types of storage that the credential can be assigned to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_Credential_Type'>SoftLayer_Network_Storage_Credential_Type </a>**

-----
[volumes]: #volumes
#### [volumes]
These are the SoftLayer_Network_Storage volumes that this credential is assigned to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a>**


## Count

-----
[volumeCount]: #volumecount
#### [volumeCount]
A count of these are the SoftLayer_Network_Storage volumes that this credential is assigned to.   
<span class="type-label">Type: </span>**unsigned long**

</div>


