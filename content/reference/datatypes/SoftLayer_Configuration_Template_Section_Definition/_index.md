---
title: "SoftLayer_Configuration_Template_Section_Definition"
description: "Configuration definition gives you details of the value that you're setting. 

If value type is defined as 'Resource Spe... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Configuration"
classes:
    - "SoftLayer_Configuration_Template_Section_Definition"
---

# SoftLayer_Configuration_Template_Section_Definition
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Configuration_Template_Section_Definition' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Configuration_Template_Section_Definition' >Datatype</a></li>
    </ul>
</div>

## Description 


Configuration definition gives you details of the value that you're setting. 

If value type is defined as "Resource Specific Values", you will have to make an additional API call to retrieve your system specific values. 







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
Created date  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[description]: #description
#### [description]
Description of a configuration definition.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[enumerationValues]: #enumerationvalues
#### [enumerationValues]
Enumeration values separated by comma.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[groupId]: #groupid
#### [groupId]
Definition group id.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
Internal identifier of a configuration definition.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[maximumValue]: #maximumvalue
#### [maximumValue]
Maximum value of a configuration definition.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[minimumValue]: #minimumvalue
#### [minimumValue]
Minimum value of a configuration definition.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
Last modify date  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
Configuration definition name.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[path]: #path
#### [path]
Definition path.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[requireValueFlag]: #requirevalueflag
#### [requireValueFlag]
Indicates if a configuration value is required for this definition.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[sectionId]: #sectionid
#### [sectionId]
Internal identifier of a configuration section.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[shortName]: #shortname
#### [shortName]
Shortened configuration definition name.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[sort]: #sort
#### [sort]
Sort order  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[typeId]: #typeid
#### [typeId]
Internal identifier of a configuration definition type.  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[attributes]: #attributes
#### [attributes]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Template_Section_Definition_Attribute'>SoftLayer_Configuration_Template_Section_Definition_Attribute[] </a>**  



</div>
<div class="prop-row">

-----
[defaultValue]: #defaultvalue
#### [defaultValue]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Template_Section_Definition_Value'>SoftLayer_Configuration_Template_Section_Definition_Value </a>**  



</div>
<div class="prop-row">

-----
[group]: #group
#### [group]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Template_Section_Definition_Group'>SoftLayer_Configuration_Template_Section_Definition_Group </a>**  



</div>
<div class="prop-row">

-----
[monitoringDataFlag]: #monitoringdataflag
#### [monitoringDataFlag]
  
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[section]: #section
#### [section]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Template_Section'>SoftLayer_Configuration_Template_Section </a>**  



</div>
<div class="prop-row">

-----
[valueType]: #valuetype
#### [valueType]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Template_Section_Definition_Type'>SoftLayer_Configuration_Template_Section_Definition_Type </a>**  



</div>

## Count
<div class="prop-row">

-----
[attributeCount]: #attributecount
#### [attributeCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>


