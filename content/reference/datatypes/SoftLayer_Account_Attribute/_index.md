---
title: "SoftLayer_Account_Attribute"
description: "Many SoftLayer customer accounts have individual attributes assigned to them that describe features or special features... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Attribute"
---

# SoftLayer_Account_Attribute
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Account_Attribute' >Datatype</a></li>
    </ul>
</div>

## Description 
Many SoftLayer customer accounts have individual attributes assigned to them that describe features or special features for that account, such as special pricing, account statuses, and ordering instructions. The SoftLayer_Account_Attribute data type contains information relating to a single SoftLayer_Account attribute. 


### associatedMethods

*  [SoftLayer_Account::getAttributes](/reference/services/SoftLayer_Account/getAttributes )



### seeAlso

* [SoftLayer_Account](/reference/services/SoftLayer_Account )


* [SoftLayer_Account_Attribute_Type](/reference/datatypes/SoftLayer_Account_Attribute_Type )




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
[accountAttributeTypeId]: #accountattributetypeid
#### [accountAttributeTypeId]
The internal identifier of the type of attribute that a SoftLayer customer account attribute belongs to.   
<span class="type-label">Type: </span>**integer**

-----
[accountId]: #accountid
#### [accountId]
The internal identifier of the SoftLayer customer account that is assigned an account attribute.   
<span class="type-label">Type: </span>**integer**

-----
[id]: #id
#### [id]
A SoftLayer customer account attribute's internal identifier.   
<span class="type-label">Type: </span>**integer**

-----
[value]: #value
#### [value]
A SoftLayer account attribute's value.   
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
The SoftLayer customer account that has an attribute.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[accountAttributeType]: #accountattributetype
#### [accountAttributeType]
The type of attribute assigned to a SoftLayer customer account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Attribute_Type'>SoftLayer_Account_Attribute_Type </a>**


## Count
</div>


