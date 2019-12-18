---
title: "SoftLayer_Account_Link_OpenStack"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Link_OpenStack"
---

# SoftLayer_Account_Link_OpenStack
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Account_Link_OpenStack' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Account_Link_OpenStack' >Datatype</a></li>
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
  
<span class="type-label">Type: </span>**integer**

-----
[createDate]: #createdate
#### [createDate]
  
<span class="type-label">Type: </span>**dateTime**

-----
[destinationAccountAlphanumericId]: #destinationaccountalphanumericid
#### [destinationAccountAlphanumericId]
  
<span class="type-label">Type: </span>**string**

-----
[destinationAccountId]: #destinationaccountid
#### [destinationAccountId]
  
<span class="type-label">Type: </span>**integer**

-----
[domainId]: #domainid
#### [domainId]
Pseudonym for destinationAccountAlphanumericId  
<span class="type-label">Type: </span>**string**

-----
[id]: #id
#### [id]
  
<span class="type-label">Type: </span>**integer**

-----
[serviceProviderId]: #serviceproviderid
#### [serviceProviderId]
  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[serviceProvider]: #serviceprovider
#### [serviceProvider]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Service_Provider'>SoftLayer_Service_Provider </a>**


## Count
</div>


