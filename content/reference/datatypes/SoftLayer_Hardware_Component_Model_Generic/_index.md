---
title: "SoftLayer_Hardware_Component_Model_Generic"
description: "The SoftLayer_Hardware_Component_Model_Generic data type contains general information relating to a single SoftLayer gen... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Component_Model_Generic"
---

# SoftLayer_Hardware_Component_Model_Generic
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Hardware_Component_Model_Generic' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Hardware_Component_Model_Generic data type contains general information relating to a single SoftLayer generic component model.  A generic component model represents a non-vendor specific representation of a hardware component.  Frequently SoftLayer utilizes components from various vendors in the servers they provision. For Example: Several different vendors produce 6GB DDR2 memory.  The generic component model for the 6GB stick of RAM encompasses every instance of this component regardless of make and model. 





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
[capacity]: #capacity
#### [capacity]
A generic component model's capacity. The capacity of a generic component model depends on the model itself.  For Example: Hard drives have a capacity that reflects the amount of data that hard drive can store.   
<span class="type-label">Type: </span>**decimal**


</div>
<div class="prop-row">

-----
[description]: #description
#### [description]
A brief description for a generic component model that typically defines it's function.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[hardwareComponentTypeId]: #hardwarecomponenttypeid
#### [hardwareComponentTypeId]
The internal identifier of the component type for a generic component model.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A generic component model's internal identification number.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[units]: #units
#### [units]
The unit of measurement for the capacity of a generic component model.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[upgradePriority]: #upgradepriority
#### [upgradePriority]
A generic component model's upgrade priority. The upgrade priority indicates the order a generic component model should be considered over other generic component models. A higher number indicates that a generic component model receives a higher upgrade preference in comparison to a generic component model with a lower priority number.   
<span class="type-label">Type: </span>**integer**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[hardwareComponentModels]: #hardwarecomponentmodels
#### [hardwareComponentModels]
A generic component model's hardware component model.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_Model'>SoftLayer_Hardware_Component_Model[] </a>**


</div>
<div class="prop-row">

-----
[hardwareComponentType]: #hardwarecomponenttype
#### [hardwareComponentType]
A generic component model's type.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_Type'>SoftLayer_Hardware_Component_Type </a>**


</div>
<div class="prop-row">

-----
[marketingFeatures]: #marketingfeatures
#### [marketingFeatures]
A list of features that a generic component model can provide.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_Model_Generic_MarketingFeature'>SoftLayer_Hardware_Component_Model_Generic_MarketingFeature </a>**


</div>

## Count
<div class="prop-row">

-----
[hardwareComponentModelCount]: #hardwarecomponentmodelcount
#### [hardwareComponentModelCount]
A count of a generic component model's hardware component model.   
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


