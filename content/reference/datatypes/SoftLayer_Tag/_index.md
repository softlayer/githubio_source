---
title: "SoftLayer_Tag"
description: "The SoftLayer_Tag data type is an optional type associated with hardware. The account ID that the tag is tied to, and th... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Tag"
classes:
    - "SoftLayer_Tag"
---

# SoftLayer_Tag
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Tag' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Tag' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Tag data type is an optional type associated with hardware. The account ID that the tag is tied to, and the tag itself are stored in this data type. There is also a flag to denote whether the tag is internal or not. 





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
Account the tag belongs to.  
<span class="type-label">Type: </span>**integer**

-----
[id]: #id
#### [id]
Unique identifier for a tag.  
<span class="type-label">Type: </span>**integer**

-----
[internal]: #internal
#### [internal]
Indicates whether a tag is internal.  
<span class="type-label">Type: </span>**integer**

-----
[name]: #name
#### [name]
Name of the tag. The characters permitted are A-Z, 0-9, whitespace,  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
The account to which the tag is tied.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[references]: #references
#### [references]
References that tie object to the tag.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Tag_Reference'>SoftLayer_Tag_Reference[] </a>**


## Count

-----
[referenceCount]: #referencecount
#### [referenceCount]
A count of references that tie object to the tag.   
<span class="type-label">Type: </span>**unsigned long**

</div>


