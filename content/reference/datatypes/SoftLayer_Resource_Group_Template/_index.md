---
title: "SoftLayer_Resource_Group_Template"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Resource"
classes:
    - "SoftLayer_Resource_Group_Template"
---

# SoftLayer_Resource_Group_Template
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Resource_Group_Template' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Resource_Group_Template' >Datatype</a></li>
    </ul>
</div>

## Description 






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

## Local
-----
[description]: #description
#### [description]
A resource group template's description.  
<span class="type-label">Type: </span>**string**

-----
[id]: #id
#### [id]
  
<span class="type-label">Type: </span>**integer**

-----
[keyName]: #keyname
#### [keyName]
A resource group template's keyname.  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[children]: #children
#### [children]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Resource_Group_Template'>SoftLayer_Resource_Group_Template[] </a>**

-----
[members]: #members
#### [members]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Resource_Group_Template_Member'>SoftLayer_Resource_Group_Template_Member[] </a>**

-----
[package]: #package
#### [package]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package'>SoftLayer_Product_Package </a>**


## Count

-----
[childrenCount]: #childrencount
#### [childrenCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[memberCount]: #membercount
#### [memberCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**

</div>


