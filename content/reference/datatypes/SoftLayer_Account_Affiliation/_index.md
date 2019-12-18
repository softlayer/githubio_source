---
title: "SoftLayer_Account_Affiliation"
description: "This service allows for a unique identifier to be associated to an existing customer account."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Affiliation"
---

# SoftLayer_Account_Affiliation
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Account_Affiliation' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Account_Affiliation' >Datatype</a></li>
    </ul>
</div>

## Description 
This service allows for a unique identifier to be associated to an existing customer account. 





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
A customer account's internal identifier.   
<span class="type-label">Type: </span>**integer**

-----
[affiliateId]: #affiliateid
#### [affiliateId]
An affiliate identifier associated with the customer account.   
<span class="type-label">Type: </span>**string**

-----
[createDate]: #createdate
#### [createDate]
The date an account affiliation was created.   
<span class="type-label">Type: </span>**dateTime**

-----
[id]: #id
#### [id]
A customer affiliation internal identifier.   
<span class="type-label">Type: </span>**integer**

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date an account affiliation was last modified.   
<span class="type-label">Type: </span>**dateTime**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
The account that an affiliation belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**


## Count
</div>


