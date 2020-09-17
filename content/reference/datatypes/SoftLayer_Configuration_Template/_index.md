---
title: "SoftLayer_Configuration_Template"
description: "The SoftLayer_Configuration_Template data type contains general information of an arbitrary resource."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Configuration"
classes:
    - "SoftLayer_Configuration_Template"
---

# SoftLayer_Configuration_Template
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Configuration_Template' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Configuration_Template' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Configuration_Template data type contains general information of an arbitrary resource. 





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
Internal identifier of a SoftLayer account that this configuration template belongs to  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
Created date  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[description]: #description
#### [description]
Configuration template description  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
Internal identifier of a configuration template.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[itemId]: #itemid
#### [itemId]
Internal identifier of a product item that this configuration template is associated with  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
Last modified date  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
Configuration template name  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[parentId]: #parentid
#### [parentId]
Internal identifier of the parent configuration template  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[userRecordId]: #userrecordid
#### [userRecordId]
Internal identifier of a user that last modified this configuration template  
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
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**


</div>
<div class="prop-row">

-----
[configurationSections]: #configurationsections
#### [configurationSections]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Template_Section'>SoftLayer_Configuration_Template_Section[] </a>**


</div>
<div class="prop-row">

-----
[defaultValues]: #defaultvalues
#### [defaultValues]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Template_Section_Definition_Value'>SoftLayer_Configuration_Template_Section_Definition_Value[] </a>**


</div>
<div class="prop-row">

-----
[definitions]: #definitions
#### [definitions]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Template_Section_Definition'>SoftLayer_Configuration_Template_Section_Definition[] </a>**


</div>
<div class="prop-row">

-----
[item]: #item
#### [item]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item </a>**


</div>
<div class="prop-row">

-----
[linkedSectionReferences]: #linkedsectionreferences
#### [linkedSectionReferences]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Template_Section_Reference'>SoftLayer_Configuration_Template_Section_Reference </a>**


</div>
<div class="prop-row">

-----
[parent]: #parent
#### [parent]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Template'>SoftLayer_Configuration_Template </a>**


</div>
<div class="prop-row">

-----
[user]: #user
#### [user]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**


</div>

## Count
<div class="prop-row">

-----
[configurationSectionCount]: #configurationsectioncount
#### [configurationSectionCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[defaultValueCount]: #defaultvaluecount
#### [defaultValueCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[definitionCount]: #definitioncount
#### [definitionCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


