---
title: "SoftLayer_Account_Address"
description: "The SoftLayer_Account_Address data type contains information on an address associated with a SoftLayer account."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Address"
---

# SoftLayer_Account_Address
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Account_Address' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Account_Address' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_Account_Address data type contains information on an address associated with a SoftLayer account. 





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
  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[address1]: #address1
#### [address1]
Line 1 of the address (normally the street address).  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[address2]: #address2
#### [address2]
Line 2 of the address.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[city]: #city
#### [city]
The city of the address.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[contactName]: #contactname
#### [contactName]
The contact name (person, office) of the address.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[country]: #country
#### [country]
The country of the address.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[description]: #description
#### [description]
The description of the address.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
The unique id of the address.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[isActive]: #isactive
#### [isActive]
Flag to show whether the address is active.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[locationId]: #locationid
#### [locationId]
The location id of the address.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[postalCode]: #postalcode
#### [postalCode]
The postal (zip) code of the address.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[state]: #state
#### [state]
The state of the address.  
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
The account to which this address belongs.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**  



</div>
<div class="prop-row">

-----
[createUser]: #createuser
#### [createUser]
The customer user who created this address.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**  



</div>
<div class="prop-row">

-----
[location]: #location
#### [location]
The location of this address.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**  



</div>
<div class="prop-row">

-----
[modifyEmployee]: #modifyemployee
#### [modifyEmployee]
The employee who last modified this address.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Employee'>SoftLayer_User_Employee </a>**  



</div>
<div class="prop-row">

-----
[modifyUser]: #modifyuser
#### [modifyUser]
The customer user who last modified this address.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**  



</div>
<div class="prop-row">

-----
[type]: #type
#### [type]
An account address' type.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Address_Type'>SoftLayer_Account_Address_Type </a>**  



</div>

## Count
</div>


