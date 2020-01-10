---
title: "SoftLayer_Layout_Item"
description: "The SoftLayer_Layout_Item contains definitions for default layout items"
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Layout"
classes:
    - "SoftLayer_Layout_Item"
---

# SoftLayer_Layout_Item
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Layout_Item' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Layout_Item' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Layout_Item contains definitions for default layout items 





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
The internal identifier of a layout item  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[keyname]: #keyname
#### [keyname]
The unique key name of the layout item, used primarily for programmatic purposes  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[layoutItemTypeId]: #layoutitemtypeid
#### [layoutItemTypeId]
The internal identifier of the related [SoftLayer_Layout_Item_Type]({{<ref "reference/datatypes/SoftLayer_Layout_Item_Type">}})  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
The friendly name of the layout item  
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[layoutItemPreferences]: #layoutitempreferences
#### [layoutItemPreferences]
The layout preferences assigned to this layout item  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Layout_Preference'>SoftLayer_Layout_Preference[] </a>**


</div>
<div class="prop-row">

-----
[layoutItemType]: #layoutitemtype
#### [layoutItemType]
The type of the layout item object  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Layout_Item_Type'>SoftLayer_Layout_Item_Type </a>**


</div>

## Count
<div class="prop-row">

-----
[layoutItemPreferenceCount]: #layoutitempreferencecount
#### [layoutItemPreferenceCount]
A count of the layout preferences assigned to this layout item   
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


