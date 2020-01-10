---
title: "SoftLayer_Layout_Preference"
description: "The SoftLayer_Layout_Preference contains definitions for default layout item preferences"
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Layout"
classes:
    - "SoftLayer_Layout_Preference"
---

# SoftLayer_Layout_Preference
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Layout_Preference' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Layout_Preference contains definitions for default layout item preferences 





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
[id]: #id
#### [id]
The internal identifier of a layout preference  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[layoutPreferenceTypeId]: #layoutpreferencetypeid
#### [layoutPreferenceTypeId]
The internal identifier of the related [SoftLayer_Layout_Preference_Type]({{<ref "reference/datatypes/SoftLayer_Layout_Preference_Type">}})  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[value]: #value
#### [value]
The default value of the preference  
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[layoutPreferenceType]: #layoutpreferencetype
#### [layoutPreferenceType]
The type of the preference object  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Layout_Preference_Type'>SoftLayer_Layout_Preference_Type </a>**


</div>

## Count
</div>


