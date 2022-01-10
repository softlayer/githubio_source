---
title: "SoftLayer_Hardware_Component_Model"
description: "The SoftLayer_Hardware_Component_Model data type contains general information relating to a single SoftLayer component m... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Component_Model"
---

# SoftLayer_Hardware_Component_Model
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Hardware_Component_Model' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Hardware_Component_Model' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_Hardware_Component_Model data type contains general information relating to a single SoftLayer component model.  A component model represents a vendor specific representation of a hardware component.  Every piece of hardware on a server will have a specific hardware component model. 





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
[architectureTypeId]: #architecturetypeid
#### [architectureTypeId]
  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[capacity]: #capacity
#### [capacity]
A component model's capacity. The capacity of a component model depends on the model itself.  For Example: Hard drives have a capacity that reflects the amount of data that hard drive can store.   
<span class="type-label">Type: </span>**decimal**  



</div>
<div class="prop-row">

-----
[description]: #description
#### [description]
A colon delimited list of hardware component model attributes.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[hardwareGenericComponentModelId]: #hardwaregenericcomponentmodelid
#### [hardwareGenericComponentModelId]
The internal identifier of the generic component model for a component model.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A hardware component model's internal identifier number.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[longDescription]: #longdescription
#### [longDescription]
  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[manufacturer]: #manufacturer
#### [manufacturer]
A hardware component model's manufacturer.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
The model name of a hardware component model.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[version]: #version
#### [version]
The model number or model description of a hardware component model.  
<span class="type-label">Type: </span>**string**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[architectureType]: #architecturetype
#### [architectureType]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_Model_Architecture_Type'>SoftLayer_Hardware_Component_Model_Architecture_Type </a>**  



</div>
<div class="prop-row">

-----
[attributes]: #attributes
#### [attributes]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_Model_Attribute'>SoftLayer_Hardware_Component_Model_Attribute[] </a>**  



</div>
<div class="prop-row">

-----
[compatibleArrayTypes]: #compatiblearraytypes
#### [compatibleArrayTypes]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Storage_Group_Array_Type'>SoftLayer_Configuration_Storage_Group_Array_Type[] </a>**  



</div>
<div class="prop-row">

-----
[compatibleChildComponentModels]: #compatiblechildcomponentmodels
#### [compatibleChildComponentModels]
All the component models that are compatible with a hardware component model.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_Model'>SoftLayer_Hardware_Component_Model[] </a>**  



</div>
<div class="prop-row">

-----
[compatibleParentComponentModels]: #compatibleparentcomponentmodels
#### [compatibleParentComponentModels]
All the component models that a hardware component model is compatible with.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_Model'>SoftLayer_Hardware_Component_Model[] </a>**  



</div>
<div class="prop-row">

-----
[firmwareQuantity]: #firmwarequantity
#### [firmwareQuantity]
  
<span class="type-label">Type: </span>**unsigned integer**  



</div>
<div class="prop-row">

-----
[firmwares]: #firmwares
#### [firmwares]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_Firmware'>SoftLayer_Hardware_Component_Firmware[] </a>**  



</div>
<div class="prop-row">

-----
[hardwareComponents]: #hardwarecomponents
#### [hardwareComponents]
A hardware component model's physical components in inventory.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component[] </a>**  



</div>
<div class="prop-row">

-----
[hardwareGenericComponentModel]: #hardwaregenericcomponentmodel
#### [hardwareGenericComponentModel]
The non-vendor specific generic component model for a hardware component model.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_Model_Generic'>SoftLayer_Hardware_Component_Model_Generic </a>**  



</div>
<div class="prop-row">

-----
[infinibandCompatibleAttribute]: #infinibandcompatibleattribute
#### [infinibandCompatibleAttribute]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_Model_Attribute'>SoftLayer_Hardware_Component_Model_Attribute </a>**  



</div>
<div class="prop-row">

-----
[isFlexSkuCompatible]: #isflexskucompatible
#### [isFlexSkuCompatible]
  
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[isInfinibandCompatible]: #isinfinibandcompatible
#### [isInfinibandCompatible]
  
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[rebootTime]: #reboottime
#### [rebootTime]
A motherboard's average reboot time.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_Motherboard_Reboot_Time'>SoftLayer_Hardware_Component_Motherboard_Reboot_Time </a>**  



</div>
<div class="prop-row">

-----
[type]: #type
#### [type]
A hardware component model's type.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[validAttributeTypes]: #validattributetypes
#### [validAttributeTypes]
The types of attributes that are allowed for a given hardware component model.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_Model_Attribute_Type'>SoftLayer_Hardware_Component_Model_Attribute_Type[] </a>**  



</div>

## Count
<div class="prop-row">

-----
[attributeCount]: #attributecount
#### [attributeCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[compatibleArrayTypeCount]: #compatiblearraytypecount
#### [compatibleArrayTypeCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[compatibleChildComponentModelCount]: #compatiblechildcomponentmodelcount
#### [compatibleChildComponentModelCount]
A count of all the component models that are compatible with a hardware component model.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[compatibleParentComponentModelCount]: #compatibleparentcomponentmodelcount
#### [compatibleParentComponentModelCount]
A count of all the component models that a hardware component model is compatible with.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[firmwareCount]: #firmwarecount
#### [firmwareCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[validAttributeTypeCount]: #validattributetypecount
#### [validAttributeTypeCount]
A count of the types of attributes that are allowed for a given hardware component model.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>


