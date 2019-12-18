---
title: "SoftLayer_Brand_Contact"
description: "SoftLayer_Brand_Contact contains the contact information for the brand such as Corporate or Support contact information"
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Brand"
classes:
    - "SoftLayer_Brand_Contact"
---

# SoftLayer_Brand_Contact
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Brand_Contact' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer_Brand_Contact contains the contact information for the brand such as Corporate or Support contact information 





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
[address1]: #address1
#### [address1]
The contact's address 1.  
<span class="type-label">Type: </span>**string**

-----
[address2]: #address2
#### [address2]
The contact's address 2.  
<span class="type-label">Type: </span>**string**

-----
[alternatePhone]: #alternatephone
#### [alternatePhone]
The contact's alternate phone number.  
<span class="type-label">Type: </span>**string**

-----
[brandContactTypeId]: #brandcontacttypeid
#### [brandContactTypeId]
The contact's type identifier.  
<span class="type-label">Type: </span>**integer**

-----
[city]: #city
#### [city]
The contact's city.  
<span class="type-label">Type: </span>**string**

-----
[country]: #country
#### [country]
The contact's country.  
<span class="type-label">Type: </span>**string**

-----
[email]: #email
#### [email]
The contact's email address.  
<span class="type-label">Type: </span>**string**

-----
[faxPhone]: #faxphone
#### [faxPhone]
The contact's fax number.  
<span class="type-label">Type: </span>**string**

-----
[firstName]: #firstname
#### [firstName]
The contact's first name.  
<span class="type-label">Type: </span>**string**

-----
[lastName]: #lastname
#### [lastName]
The contact's last name.  
<span class="type-label">Type: </span>**string**

-----
[officePhone]: #officephone
#### [officePhone]
The contact's phone number.  
<span class="type-label">Type: </span>**string**

-----
[postalCode]: #postalcode
#### [postalCode]
The contact's postal code.  
<span class="type-label">Type: </span>**string**

-----
[state]: #state
#### [state]
The contact's state.  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[brand]: #brand
#### [brand]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Brand'>SoftLayer_Brand </a>**

-----
[brandContactType]: #brandcontacttype
#### [brandContactType]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Brand_Contact_Type'>SoftLayer_Brand_Contact_Type </a>**


## Count
</div>


