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
[id]: #id
#### [id]
The ID associated with this component type.  
<span class="type-label">Type: </span>**integer**

-----
[keyName]: #keyname
#### [keyName]
The hardware component type key name or code.  
<span class="type-label">Type: </span>**string**

-----
[type]: #type
#### [type]
The type associated with this component type.  
<span class="type-label">Type: </span>**string**

-----
[typeParentId]: #typeparentid
#### [typeParentId]
The parent id associated with this component type.  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[hardwareGenericComponentModels]: #hardwaregenericcomponentmodels
#### [hardwareGenericComponentModels]
The generic component model description for this component type object.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_Model_Generic'>SoftLayer_Hardware_Component_Model_Generic[] </a>**

-----
[typeParent]: #typeparent
#### [typeParent]
The parent generic component model object for this generic component model object.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_Type'>SoftLayer_Hardware_Component_Type </a>**


## Count

-----
[hardwareGenericComponentModelCount]: #hardwaregenericcomponentmodelcount
#### [hardwareGenericComponentModelCount]
A count of the generic component model description for this component type object.   
<span class="type-label">Type: </span>**unsigned long**

</div>


