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
[address1]: #address1
#### [address1]
Line 1 of the address (normally the street address).  
<span class="type-label">Type: </span>**string**

-----
[address2]: #address2
#### [address2]
Line 2 of the address.  
<span class="type-label">Type: </span>**string**

-----
[city]: #city
#### [city]
The city of the address.  
<span class="type-label">Type: </span>**string**

-----
[contactName]: #contactname
#### [contactName]
The contact name (person, office) of the address.  
<span class="type-label">Type: </span>**string**

-----
[country]: #country
#### [country]
The country of the address.  
<span class="type-label">Type: </span>**string**

-----
[description]: #description
#### [description]
The description of the address.  
<span class="type-label">Type: </span>**string**

-----
[id]: #id
#### [id]
The unique id of the address.  
<span class="type-label">Type: </span>**integer**

-----
[isActive]: #isactive
#### [isActive]
Flag to show whether the address is active.  
<span class="type-label">Type: </span>**integer**

-----
[locationId]: #locationid
#### [locationId]
The location id of the address.  
<span class="type-label">Type: </span>**integer**

-----
[postalCode]: #postalcode
#### [postalCode]
The postal (zip) code of the address.  
<span class="type-label">Type: </span>**string**

-----
[state]: #state
#### [state]
The state of the address.  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
The account to which this address belongs.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[createUser]: #createuser
#### [createUser]
The customer user who created this address.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**

-----
[location]: #location
#### [location]
The location of this address.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**

-----
[modifyEmployee]: #modifyemployee
#### [modifyEmployee]
The employee who last modified this address.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Employee'>SoftLayer_User_Employee </a>**

-----
[modifyUser]: #modifyuser
#### [modifyUser]
The customer user who last modified this address.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**

-----
[type]: #type
#### [type]
An account address' type.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Address_Type'>SoftLayer_Account_Address_Type </a>**


## Count
</div>


