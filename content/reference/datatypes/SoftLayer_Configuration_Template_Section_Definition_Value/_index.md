---
title: "SoftLayer_Configuration_Template_Section_Definition_Value"
description: "SoftLayer_Configuration_Section_Value is used to set the value for a configuration definition"
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Configuration"
classes:
    - "SoftLayer_Configuration_Template_Section_Definition_Value"
---

# SoftLayer_Configuration_Template_Section_Definition_Value
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Configuration_Template_Section_Definition_Value' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Configuration_Template_Section_Definition_Value' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer_Configuration_Section_Value is used to set the value for a configuration definition 





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
[definitionId]: #definitionid
#### [definitionId]
Internal identifier of a configuration definition that this configuration value if defined by  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
Internal Last modified date  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[templateId]: #templateid
#### [templateId]
Internal identifier of a configuration template that this configuration value belongs to  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[value]: #value
#### [value]
Internal Configuration value  
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[definition]: #definition
#### [definition]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Template_Section_Definition'>SoftLayer_Configuration_Template_Section_Definition </a>**


</div>
<div class="prop-row">

-----
[template]: #template
#### [template]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Template'>SoftLayer_Configuration_Template </a>**


</div>

## Count
</div>


