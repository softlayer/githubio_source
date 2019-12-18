---
title: "SoftLayer_Configuration_Template_Section"
description: "The SoftLayer_Configuration_Template_Section data type contains information of a configuration section. 

Configuration... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Configuration"
classes:
    - "SoftLayer_Configuration_Template_Section"
---

# SoftLayer_Configuration_Template_Section
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Configuration_Template_Section' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Configuration_Template_Section' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Configuration_Template_Section data type contains information of a configuration section. 

Configuration can contain sub-sections. 





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
[createDate]: #createdate
#### [createDate]
Created date  
<span class="type-label">Type: </span>**dateTime**

-----
[description]: #description
#### [description]
Configuration section description  
<span class="type-label">Type: </span>**string**

-----
[id]: #id
#### [id]
Internal identifier of a configuration section.  
<span class="type-label">Type: </span>**integer**

-----
[linkedTemplateId]: #linkedtemplateid
#### [linkedTemplateId]
Internal identifier of a sub configuration template that this section points to. Use this property if you wish to create a reference to a sub configuration template when creating a linked section.   
<span class="type-label">Type: </span>**string**

-----
[modifyDate]: #modifydate
#### [modifyDate]
Last modified date  
<span class="type-label">Type: </span>**dateTime**

-----
[name]: #name
#### [name]
Configuration section name  
<span class="type-label">Type: </span>**string**

-----
[parentId]: #parentid
#### [parentId]
Internal identifier of the parent configuration section  
<span class="type-label">Type: </span>**integer**

-----
[sort]: #sort
#### [sort]
Sort order  
<span class="type-label">Type: </span>**integer**

-----
[templateId]: #templateid
#### [templateId]
Internal identifier of a configuration template that this section belongs to  
<span class="type-label">Type: </span>**string**

-----
[typeId]: #typeid
#### [typeId]
Internal identifier of the configuration section type  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[definitions]: #definitions
#### [definitions]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Template_Section_Definition'>SoftLayer_Configuration_Template_Section_Definition[] </a>**

-----
[disallowedDeletionFlag]: #disalloweddeletionflag
#### [disallowedDeletionFlag]
  
<span class="type-label">Type: </span>**boolean**

-----
[linkedTemplate]: #linkedtemplate
#### [linkedTemplate]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Template'>SoftLayer_Configuration_Template </a>**

-----
[linkedTemplateReference]: #linkedtemplatereference
#### [linkedTemplateReference]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Template_Section_Reference'>SoftLayer_Configuration_Template_Section_Reference </a>**

-----
[profiles]: #profiles
#### [profiles]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Template_Section_Profile'>SoftLayer_Configuration_Template_Section_Profile[] </a>**

-----
[sectionType]: #sectiontype
#### [sectionType]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Template_Section_Type'>SoftLayer_Configuration_Template_Section_Type </a>**

-----
[sectionTypeName]: #sectiontypename
#### [sectionTypeName]
  
<span class="type-label">Type: </span>**string**

-----
[subSections]: #subsections
#### [subSections]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Template_Section'>SoftLayer_Configuration_Template_Section[] </a>**

-----
[template]: #template
#### [template]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Template'>SoftLayer_Configuration_Template </a>**


## Count

-----
[definitionCount]: #definitioncount
#### [definitionCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[profileCount]: #profilecount
#### [profileCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[subSectionCount]: #subsectioncount
#### [subSectionCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**

</div>


