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
A customer account's internal identifier.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[affiliateId]: #affiliateid
#### [affiliateId]
An affiliate identifier associated with the customer account.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
The date an account affiliation was created.   
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A customer affiliation internal identifier.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date an account affiliation was last modified.   
<span class="type-label">Type: </span>**dateTime**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[account]: #account
#### [account]
The account that an affiliation belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**


</div>

## Count
</div>


