---
title: "SoftLayer_Account_Regional_Registry_Detail_Property"
description: "Subnet registration properties are used to define various attributes of the [SoftLayer_Account_Regional_Registry_Detail]... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Regional_Registry_Detail_Property"
---

# SoftLayer_Account_Regional_Registry_Detail_Property
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Account_Regional_Registry_Detail_Property' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Account_Regional_Registry_Detail_Property' >Datatype</a></li>
    </ul>
</div>

## Description 


Subnet registration properties are used to define various attributes of the [SoftLayer_Account_Regional_Registry_Detail]({{<ref "reference/datatypes/SoftLayer_Account_Regional_Registry_Detail">}}) objects, which describe the available value formats. 





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
[createDate]: #createdate
#### [createDate]
  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
Unique ID of the property object   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[propertyTypeId]: #propertytypeid
#### [propertyTypeId]
The numeric ID of the related [SoftLayer_Account_Regional_Registry_Detail_Property_Type]({{<ref "reference/datatypes/SoftLayer_Account_Regional_Registry_Detail_Property_Type">}})   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[registrationDetailId]: #registrationdetailid
#### [registrationDetailId]
The numeric ID of the related [SoftLayer_Account_Regional_Registry_Detail]({{<ref "reference/datatypes/SoftLayer_Account_Regional_Registry_Detail">}})   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[sequencePosition]: #sequenceposition
#### [sequencePosition]
When multiple properties exist for a property type, defines the position in the sequence of those properties   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[value]: #value
#### [value]
The value of the property   
<span class="type-label">Type: </span>**string**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[detail]: #detail
#### [detail]
The [SoftLayer_Account_Regional_Registry_Detail]({{<ref "reference/datatypes/SoftLayer_Account_Regional_Registry_Detail">}}) object this property belongs to  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Regional_Registry_Detail'>SoftLayer_Account_Regional_Registry_Detail </a>**  



</div>
<div class="prop-row">

-----
[propertyType]: #propertytype
#### [propertyType]
The [SoftLayer_Account_Regional_Registry_Detail_Property_Type]({{<ref "reference/datatypes/SoftLayer_Account_Regional_Registry_Detail_Property_Type">}}) object this property belongs to  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Regional_Registry_Detail_Property_Type'>SoftLayer_Account_Regional_Registry_Detail_Property_Type </a>**  



</div>

## Count
</div>


