---
title: "SoftLayer_Container_Search_ObjectType"
description: "This data type is a container that stores information about a single indexed object type.  Object type information can b... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Search_ObjectType"
---

# SoftLayer_Container_Search_ObjectType
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Search_ObjectType' >Datatype</a></li>
    </ul>
</div>

## Description 


This data type is a container that stores information about a single indexed object type.  Object type information can be used for discovery of searchable data and for creation or validation of object index search strings.  Each of these containers holds a collection of <b>[SoftLayer_Container_Search_ObjectType_Property]({{<ref "reference/datatypes/SoftLayer_Container_Search_ObjectType_Property">}})</b> method for information on using object types in search strings. 


### associatedMethods

*  [SoftLayer_Search::getObjectTypes](/reference/services/SoftLayer_Search/getObjectTypes )
*  [SoftLayer_Search::search](/reference/services/SoftLayer_Search/search )
*  [SoftLayer_Search::advancedSearch](/reference/services/SoftLayer_Search/advancedSearch )



### seeAlso

* [SoftLayer_Container_Search_ObjectType_Property](/reference/datatypes/SoftLayer_Container_Search_ObjectType_Property )




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
[name]: #name
#### [name]
Name of object type.   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[properties]: #properties
#### [properties]
A collection of [SoftLayer_Container_Search_ObjectType_Property]({{<ref "reference/datatypes/SoftLayer_Container_Search_ObjectType_Property">}}).   
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Search_ObjectType_Property'>SoftLayer_Container_Search_ObjectType_Property[] </a>**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


