---
title: "SoftLayer_Account_Password"
description: "The SoftLayer_Account_Password contains username, passwords and notes for services that may require for external applica... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Password"
---

# SoftLayer_Account_Password
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Account_Password' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Account_Password' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Account_Password contains username, passwords and notes for services that may require for external applications such the Webcc interface for the EVault Storage service. 


### associatedMethods

*  [SoftLayer_Account::getEvaultMasterUser](/reference/services/SoftLayer_Account/getEvaultMasterUser )



### seeAlso

* [SoftLayer_Software_Password](/reference/datatypes/SoftLayer_Software_Password )




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
The SoftLayer customer account id that a username/password combination is associated with.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A username/password combination's internal identifier.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[notes]: #notes
#### [notes]
A simple description of a username/password combination. These notes don't affect portal functionality.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[password]: #password
#### [password]
The password portion of a username/password combination.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[typeId]: #typeid
#### [typeId]
An identifier relating to a username/password combinations's associated service.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[username]: #username
#### [username]
The username portion of a username/password combination.  
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
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**


</div>
<div class="prop-row">

-----
[type]: #type
#### [type]
The service that an account/password combination is tied to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Password_Type'>SoftLayer_Account_Password_Type </a>**


</div>

## Count
</div>


