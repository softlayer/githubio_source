---
title: "SoftLayer_Account_Authentication_Attribute"
description: "Account authentication has many different settings that can be set. This class allows the customer or employee to set th... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Authentication_Attribute"
---

# SoftLayer_Account_Authentication_Attribute
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Account_Authentication_Attribute' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Account_Authentication_Attribute' >Datatype</a></li>
    </ul>
</div>

## Description 
Account authentication has many different settings that can be set. This class allows the customer or employee to set these settigns. 


### associatedMethods

*  [SoftLayer_Account_Authentication_Saml::getAttributes](/reference/services/SoftLayer_Account_Authentication_Saml/getAttributes )



### seeAlso

* [SoftLayer_Account_Authentication_Saml](/reference/datatypes/SoftLayer_Account_Authentication_Saml )


* [SoftLayer_Account_Authentication_Attribute_Type](/reference/datatypes/SoftLayer_Account_Authentication_Attribute_Type )




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
The internal identifier of the SoftLayer customer account that is assigned an account authenction attribute.   
<span class="type-label">Type: </span>**integer**

-----
[id]: #id
#### [id]
A SoftLayer account authenction attribute's internal identifier.   
<span class="type-label">Type: </span>**integer**

-----
[typeId]: #typeid
#### [typeId]
The internal identifier of the type of attribute that a SoftLayer account authenction attribute belongs to.   
<span class="type-label">Type: </span>**integer**

-----
[value]: #value
#### [value]
A SoftLayer account authenction attribute's value.   
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
The SoftLayer customer account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[authenticationRecord]: #authenticationrecord
#### [authenticationRecord]
The SoftLayer account authentication that has an attribute.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Authentication_Saml'>SoftLayer_Account_Authentication_Saml </a>**

-----
[type]: #type
#### [type]
The type of attribute assigned to a SoftLayer account authentication.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Authentication_Attribute_Type'>SoftLayer_Account_Authentication_Attribute_Type </a>**


## Count
</div>


