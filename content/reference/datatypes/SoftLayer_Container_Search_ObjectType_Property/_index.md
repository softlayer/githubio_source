---
title: "SoftLayer_Container_Search_ObjectType_Property"
description: "This data type is a container that stores information about a single property of a searchable object type.  Each <b>[[So... "
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
This data type is a container that stores information about a single property of a searchable object type.  Each <b>[[SoftLayer_Container_Search_ObjectType (type)|SoftLayer_Container_Search_ObjectType]]</b> object holds a collection of these properties.  Property information can be used for discovery of searchable data and for the creation or validation of object index search strings.  Note that properties are only understood by the <b>[[SoftLayer_Search/advancedSearch|advancedSearch()]]</b> method.  Refer to the <b>advancedSearch()</b> method for information on using properties in search strings. 
<!-- Service Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Method Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Service Filer END -->

<div id="properties" class="content">
    <div id="localProperties" class="prop-content" >
        <h2>Local</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#name" name=name>name</a></span>
            <div class='views-field-body'>Name of property.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#sortableFlag" name=sortableFlag>sortableFlag</a></span>
            <div class='views-field-body'>Indicates if this property can be sorted.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#type" name=type>type</a></span>
            <div class='views-field-body'>Property data type.  Valid values include 'boolean', 'integer', 'date', 'string' or 'text'.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
    </div>


