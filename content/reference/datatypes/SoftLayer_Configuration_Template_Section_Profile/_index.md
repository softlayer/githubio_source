---
title: "SoftLayer_Configuration_Template_Section_Profile"
description: "Some configuration templates let you create a unique configuration profiles. 

For example, you can create multiple conf... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Configuration"
classes:
    - "SoftLayer_Configuration_Template_Section_Profile"
---

# SoftLayer_Configuration_Template_Section_Profile
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Configuration_Template_Section_Profile' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Configuration_Template_Section_Profile' >Datatype</a></li>
    </ul>
</div>

## Description 
Some configuration templates let you create a unique configuration profiles. 

For example, you can create multiple configuration profiles to monitor multiple hard drives with "CPU/Memory/Disk Monitoring Agent". SoftLayer_Configuration_Template_Section_Profile help you keep track of custom configuration profiles. 





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
[agentId]: #agentid
#### [agentId]
Internal identifier of a monitoring agent this profile belongs to.  
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
[id]: #id
#### [id]
Internal identifier of a configuration profile.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
Name of a configuration profile  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[sectionId]: #sectionid
#### [sectionId]
Internal identifier of a configuration section that this profile belongs to.  
<span class="type-label">Type: </span>**integer**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[configurationSection]: #configurationsection
#### [configurationSection]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Template_Section'>SoftLayer_Configuration_Template_Section </a>**


</div>

## Count
</div>


