---
title: "SoftLayer_Hardware_Component_Revision"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Component_Revision"
---

# SoftLayer_Hardware_Component_Revision
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Hardware_Component_Revision' >Datatype</a></li>
    </ul>
</div>

## Description 








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
[firmwareVersionId]: #firmwareversionid
#### [firmwareVersionId]
  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[hardwareComponentId]: #hardwarecomponentid
#### [hardwareComponentId]
  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[biosDate]: #biosdate
#### [biosDate]
The firmware build date  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[firmware]: #firmware
#### [firmware]
The Firmware installed on this record's Hardware Component.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_Firmware'>SoftLayer_Hardware_Component_Firmware </a>**  



</div>
<div class="prop-row">

-----
[hardwareComponent]: #hardwarecomponent
#### [hardwareComponent]
The Hardware Component this revision record applies to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component </a>**  



</div>
<div class="prop-row">

-----
[revision]: #revision
#### [revision]
The firmware revision  
<span class="type-label">Type: </span>**string**  



</div>

## Count
</div>


