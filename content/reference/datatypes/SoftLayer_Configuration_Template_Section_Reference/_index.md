---
title: "SoftLayer_Configuration_Template_Section_Reference"
description: "The SoftLayer_Configuration_Template_Section_Reference data type contains information of a configuration section and its... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Configuration"
classes:
    - "SoftLayer_Configuration_Template_Section_Reference"
---

# SoftLayer_Configuration_Template_Section_Reference
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Configuration_Template_Section_Reference' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Configuration_Template_Section_Reference' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_Configuration_Template_Section_Reference data type contains information of a configuration section and its associated configuration template. 





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
[id]: #id
#### [id]
Internal identifier of a configuration section reference.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
Modified date  
<span class="type-label">Type: </span>**dateTime**  



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
[templateId]: #templateid
#### [templateId]
Internal identifier of a configuration template.  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[section]: #section
#### [section]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Template_Section'>SoftLayer_Configuration_Template_Section </a>**  



</div>
<div class="prop-row">

-----
[template]: #template
#### [template]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Template'>SoftLayer_Configuration_Template </a>**  



</div>

## Count
</div>


