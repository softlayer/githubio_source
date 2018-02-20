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
This data type is a container that stores information about a single indexed object type.  Object type information can be used for discovery of searchable data and for creation or validation of object index search strings.  Each of these containers holds a collection of <b>[[SoftLayer_Container_Search_ObjectType_Property (type)|SoftLayer_Container_Search_ObjectType_Property]]</b> objects, specifying which object properties are exposed for the current user.  Refer to the the documentation for the <b>[[SoftLayer_Search/search|search()]]</b> method for information on using object types in search strings. 
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
            <div class='views-field-body'>Name of object type.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#properties" name=properties>properties</a></span>
            <div class='views-field-body'>A collection of [[SoftLayer_Container_Search_ObjectType_Property|object properties]].  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Container_Search_ObjectType_Property'>SoftLayer_Container_Search_ObjectType_Property[] </a></p></div>
        </div>
            </div>
    </div>


