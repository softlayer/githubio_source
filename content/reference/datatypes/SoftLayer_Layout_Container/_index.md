---
title: "SoftLayer_Layout_Container"
description: "The SoftLayer_Layout_Container contains definitions for default page layouts"
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Layout"
classes:
    - "SoftLayer_Layout_Container"
---

# SoftLayer_Layout_Container
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Layout_Container' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Layout_Container' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_Layout_Container contains definitions for default page layouts 





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
The internal identifier of a layout container  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[keyname]: #keyname
#### [keyname]
The unique key name of the layout container, used primarily for programmatic purposes  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[layoutContainerTypeId]: #layoutcontainertypeid
#### [layoutContainerTypeId]
The internal identifier of the related [SoftLayer_Layout_Container_Type]({{<ref "reference/datatypes/SoftLayer_Layout_Container_Type">}})  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
The friendly name of the layout container  
<span class="type-label">Type: </span>**string**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[layoutContainerType]: #layoutcontainertype
#### [layoutContainerType]
The type of the layout container object  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Layout_Container_Type'>SoftLayer_Layout_Container_Type </a>**  



</div>
<div class="prop-row">

-----
[layoutItems]: #layoutitems
#### [layoutItems]
The layout items assigned to this layout container  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Layout_Item'>SoftLayer_Layout_Item[] </a>**  



</div>

## Count
<div class="prop-row">

-----
[layoutItemCount]: #layoutitemcount
#### [layoutItemCount]
A count of the layout items assigned to this layout container   
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>


