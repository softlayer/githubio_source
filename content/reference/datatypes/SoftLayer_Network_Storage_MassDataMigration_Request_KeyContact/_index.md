---
title: "SoftLayer_Network_Storage_MassDataMigration_Request_KeyContact"
description: "The SoftLayer_Network_Storage_MassDataMigration_Request_KeyContact data type contains name, email, and phone for key con... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_MassDataMigration_Request_KeyContact"
---

# SoftLayer_Network_Storage_MassDataMigration_Request_KeyContact
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Storage_MassDataMigration_Request_KeyContact' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Storage_MassDataMigration_Request_KeyContact' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_Network_Storage_MassDataMigration_Request_KeyContact data type contains name, email, and phone for key contact at customer location who will handle Mass Data Migration. 





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
An account number that is linked to a KeyContact.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
The date a KeyContact was created.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[email]: #email
#### [email]
KeyContact's Email Id.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
The unique id of the key contact.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date a KeyContact was last modified.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
KeyContact's Name.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[phone]: #phone
#### [phone]
A phone number assigned to a KeyContact.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[requestId]: #requestid
#### [requestId]
A request id that is linked to a KeyContact.  
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
The request this key contact belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**  



</div>
<div class="prop-row">

-----
[request]: #request
#### [request]
The request this key contact belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage_MassDataMigration_Request'>SoftLayer_Network_Storage_MassDataMigration_Request </a>**  



</div>

## Count
</div>


