---
title: "SoftLayer_Provisioning_Hook"
description: "The SoftLayer_Provisioning_Hook contains all the information needed to add a hook into a server/Virtual provision and os... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Provisioning"
classes:
    - "SoftLayer_Provisioning_Hook"
---

# SoftLayer_Provisioning_Hook
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Provisioning_Hook' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Provisioning_Hook' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Provisioning_Hook contains all the information needed to add a hook into a server/Virtual provision and os reload. 





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
The ID of the account the script belongs to.  
<span class="type-label">Type: </span>**integer**

-----
[createDate]: #createdate
#### [createDate]
  
<span class="type-label">Type: </span>**dateTime**

-----
[id]: #id
#### [id]
  
<span class="type-label">Type: </span>**integer**

-----
[modifyDate]: #modifydate
#### [modifyDate]
  
<span class="type-label">Type: </span>**dateTime**

-----
[name]: #name
#### [name]
The name of the hook.  
<span class="type-label">Type: </span>**string**

-----
[typeId]: #typeid
#### [typeId]
The ID of the type of hook the script is identified as.  Currently only CUSTOMER_PROVIDED_HOOK has been implemented.  
<span class="type-label">Type: </span>**integer**

-----
[uri]: #uri
#### [uri]
The endpoint that the script will be downloaded from (USERNAME AND PASSWORD SHOULD BE INCLUDED HERE).  If the endpoint is HTTP, the script will only be downloaded.  If the endpoint is HTTPS, the script will be downloaded and executed.  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[hookType]: #hooktype
#### [hookType]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Provisioning_Hook_Type'>SoftLayer_Provisioning_Hook_Type </a>**


## Count
</div>


