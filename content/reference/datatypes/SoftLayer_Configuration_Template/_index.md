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
Internal identifier of a SoftLayer account that this configuration template belongs to  
<span class="type-label">Type: </span>**integer**

-----
[createDate]: #createdate
#### [createDate]
Created date  
<span class="type-label">Type: </span>**dateTime**

-----
[description]: #description
#### [description]
Configuration template description  
<span class="type-label">Type: </span>**string**

-----
[id]: #id
#### [id]
Internal identifier of a configuration template.  
<span class="type-label">Type: </span>**integer**

-----
[itemId]: #itemid
#### [itemId]
Internal identifier of a product item that this configuration template is associated with  
<span class="type-label">Type: </span>**integer**

-----
[modifyDate]: #modifydate
#### [modifyDate]
Last modified date  
<span class="type-label">Type: </span>**dateTime**

-----
[name]: #name
#### [name]
Configuration template name  
<span class="type-label">Type: </span>**string**

-----
[parentId]: #parentid
#### [parentId]
Internal identifier of the parent configuration template  
<span class="type-label">Type: </span>**integer**

-----
[userRecordId]: #userrecordid
#### [userRecordId]
Internal identifier of a user that last modified this configuration template  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[configurationSections]: #configurationsections
#### [configurationSections]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Template_Section'>SoftLayer_Configuration_Template_Section[] </a>**

-----
[configurationTemplateReference]: #configurationtemplatereference
#### [configurationTemplateReference]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference'>SoftLayer_Monitoring_Agent_Configuration_Template_Group_Reference[] </a>**

-----
[defaultValues]: #defaultvalues
#### [defaultValues]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Template_Section_Definition_Value'>SoftLayer_Configuration_Template_Section_Definition_Value[] </a>**

-----
[definitions]: #definitions
#### [definitions]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Template_Section_Definition'>SoftLayer_Configuration_Template_Section_Definition[] </a>**

-----
[item]: #item
#### [item]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item </a>**

-----
[linkedSectionReferences]: #linkedsectionreferences
#### [linkedSectionReferences]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Template_Section_Reference'>SoftLayer_Configuration_Template_Section_Reference </a>**

-----
[parent]: #parent
#### [parent]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Template'>SoftLayer_Configuration_Template </a>**

-----
[user]: #user
#### [user]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**


## Count

-----
[configurationSectionCount]: #configurationsectioncount
#### [configurationSectionCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[configurationTemplateReferenceCount]: #configurationtemplatereferencecount
#### [configurationTemplateReferenceCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[defaultValueCount]: #defaultvaluecount
#### [defaultValueCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[definitionCount]: #definitioncount
#### [definitionCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**

</div>


