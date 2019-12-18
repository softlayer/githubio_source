---
title: "SoftLayer_Account_Rwhois_Handle"
description: "Provides a means of tracking handle identifiers at the various regional internet registries (RIRs). These objects are us... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Rwhois_Handle"
---

# SoftLayer_Account_Rwhois_Handle
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Account_Rwhois_Handle' >Datatype</a></li>
    </ul>
</div>

## Description 
Provides a means of tracking handle identifiers at the various regional internet registries (RIRs). These objects are used by the [SoftLayer_Network_Subnet_Registration]({{<ref "reference/datatypes/SoftLayer_Network_Subnet_Registration">}}) objects to identify a customer or organization when a subnet is registered. 





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
The handle object's associated [SoftLayer_Account]({{<ref "reference/datatypes/SoftLayer_Account">}}) id   
<span class="type-label">Type: </span>**integer**

-----
[createDate]: #createdate
#### [createDate]
  
<span class="type-label">Type: </span>**dateTime**

-----
[handle]: #handle
#### [handle]
The handle object's unique identifier as assigned by the RIR.   
<span class="type-label">Type: </span>**string**

-----
[id]: #id
#### [id]
Unique ID of the handle object   
<span class="type-label">Type: </span>**integer**

-----
[modifyDate]: #modifydate
#### [modifyDate]
  
<span class="type-label">Type: </span>**dateTime**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
The account that this handle belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**


## Count
</div>


