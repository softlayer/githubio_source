---
title: "SoftLayer_Container_Search_ObjectType_Property"
description: "This data type is a container that stores information about a single property of a searchable object type.  Each <b>[Sof... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Search_ObjectType_Property"
---

# SoftLayer_Container_Search_ObjectType_Property
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Search_ObjectType_Property' >Datatype</a></li>
    </ul>
</div>

## Description 
This data type is a container that stores information about a single property of a searchable object type.  Each <b>[SoftLayer_Container_Search_ObjectType]({{<ref "reference/datatypes/SoftLayer_Container_Search_ObjectType">}})</b> method.  Refer to the <b>advancedSearch()</b> method for information on using properties in search strings. 


### associatedMethods

*  [SoftLayer_Search::getObjectTypes](/reference/services/SoftLayer_Search/getObjectTypes )
*  [SoftLayer_Search::advancedSearch](/reference/services/SoftLayer_Search/advancedSearch )



### seeAlso

* [SoftLayer_Container_Search_ObjectType](/reference/datatypes/SoftLayer_Container_Search_ObjectType )




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
Name of property.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[sortableFlag]: #sortableflag
#### [sortableFlag]
Indicates if this property can be sorted.   
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[type]: #type
#### [type]
Property data type.  Valid values include 'boolean', 'integer', 'date', 'string' or 'text'.   
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


