---
title: "SoftLayer_Hardware_Component_Type"
description: "The SoftLayer_Hardware_Component_Type data type provides details on the type of component requested"
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Component_Type"
---

# SoftLayer_Hardware_Component_Type
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Hardware_Component_Type' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_Hardware_Component_Type data type provides details on the type of component requested 





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
The ID associated with this component type.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[keyName]: #keyname
#### [keyName]
The hardware component type key name or code.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[type]: #type
#### [type]
The type associated with this component type.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[typeParentId]: #typeparentid
#### [typeParentId]
The parent id associated with this component type.  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[hardwareGenericComponentModels]: #hardwaregenericcomponentmodels
#### [hardwareGenericComponentModels]
The generic component model description for this component type object.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_Model_Generic'>SoftLayer_Hardware_Component_Model_Generic[] </a>**  



</div>
<div class="prop-row">

-----
[typeParent]: #typeparent
#### [typeParent]
The parent generic component model object for this generic component model object.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_Type'>SoftLayer_Hardware_Component_Type </a>**  



</div>

## Count
<div class="prop-row">

-----
[hardwareGenericComponentModelCount]: #hardwaregenericcomponentmodelcount
#### [hardwareGenericComponentModelCount]
A count of the generic component model description for this component type object.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>


