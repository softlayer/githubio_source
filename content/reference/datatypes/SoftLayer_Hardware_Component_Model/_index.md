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
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Hardware_Component_Model' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Hardware_Component_Model data type contains general information relating to a single SoftLayer component model.  A component model represents a vendor specific representation of a hardware component.  Every piece of hardware on a server will have a specific hardware component model. 





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
            <span class='views-field-title'><a href="#architectureTypeId" name=architectureTypeId>architectureTypeId</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#capacity" name=capacity>capacity</a></span>
            <div class='views-field-body'>A component model's capacity. The capacity of a component model depends on the model itself.  For Example: Hard drives have a capacity that reflects the amount of data that hard drive can store.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>decimal</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#description" name=description>description</a></span>
            <div class='views-field-body'>A colon delimited list of hardware component model attributes. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#hardwareGenericComponentModelId" name=hardwareGenericComponentModelId>hardwareGenericComponentModelId</a></span>
            <div class='views-field-body'>The internal identifier of the generic component model for a component model. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>A hardware component model's internal identifier number. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#longDescription" name=longDescription>longDescription</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#manufacturer" name=manufacturer>manufacturer</a></span>
            <div class='views-field-body'>A hardware component model's manufacturer. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#name" name=name>name</a></span>
            <div class='views-field-body'>The model name of a hardware component model. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#version" name=version>version</a></span>
            <div class='views-field-body'>The model number or model description of a hardware component model. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#architectureType" name=architectureType>architectureType</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware_Component_Model_Architecture_Type'>SoftLayer_Hardware_Component_Model_Architecture_Type </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#attributes" name=attributes>attributes</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware_Component_Model_Attribute'>SoftLayer_Hardware_Component_Model_Attribute[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#compatibleArrayTypes" name=compatibleArrayTypes>compatibleArrayTypes</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Configuration_Storage_Group_Array_Type'>SoftLayer_Configuration_Storage_Group_Array_Type[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#compatibleChildComponentModels" name=compatibleChildComponentModels>compatibleChildComponentModels</a></span>
            <div class='views-field-body'>All the component models that are compatible with a hardware component model. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware_Component_Model'>SoftLayer_Hardware_Component_Model[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#compatibleParentComponentModels" name=compatibleParentComponentModels>compatibleParentComponentModels</a></span>
            <div class='views-field-body'>All the component models that a hardware component model is compatible with. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware_Component_Model'>SoftLayer_Hardware_Component_Model[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#firmwareQuantity" name=firmwareQuantity>firmwareQuantity</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsigned integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#firmwares" name=firmwares>firmwares</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware_Component_Firmware'>SoftLayer_Hardware_Component_Firmware[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#hardwareComponents" name=hardwareComponents>hardwareComponents</a></span>
            <div class='views-field-body'>A hardware component model's physical components in inventory. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#hardwareGenericComponentModel" name=hardwareGenericComponentModel>hardwareGenericComponentModel</a></span>
            <div class='views-field-body'>The non-vendor specific generic component model for a hardware component model. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware_Component_Model_Generic'>SoftLayer_Hardware_Component_Model_Generic </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#infinibandCompatibleAttribute" name=infinibandCompatibleAttribute>infinibandCompatibleAttribute</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware_Component_Model_Attribute'>SoftLayer_Hardware_Component_Model_Attribute </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#isFlexSkuCompatible" name=isFlexSkuCompatible>isFlexSkuCompatible</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#isInfinibandCompatible" name=isInfinibandCompatible>isInfinibandCompatible</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#rebootTime" name=rebootTime>rebootTime</a></span>
            <div class='views-field-body'>A motherboard's average reboot time. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware_Component_Motherboard_Reboot_Time'>SoftLayer_Hardware_Component_Motherboard_Reboot_Time </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#type" name=type>type</a></span>
            <div class='views-field-body'>A hardware component model's type. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#validAttributeTypes" name=validAttributeTypes>validAttributeTypes</a></span>
            <div class='views-field-body'>The types of attributes that are allowed for a given hardware component model. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware_Component_Model_Attribute_Type'>SoftLayer_Hardware_Component_Model_Attribute_Type[] </a></p></div>
        </div>
                <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#attributeCount" name=attributeCount>attributeCount</a></span>
            <div class='views-field-body'>A count of  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#compatibleArrayTypeCount" name=compatibleArrayTypeCount>compatibleArrayTypeCount</a></span>
            <div class='views-field-body'>A count of  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#compatibleChildComponentModelCount" name=compatibleChildComponentModelCount>compatibleChildComponentModelCount</a></span>
            <div class='views-field-body'>A count of all the component models that are compatible with a hardware component model. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#compatibleParentComponentModelCount" name=compatibleParentComponentModelCount>compatibleParentComponentModelCount</a></span>
            <div class='views-field-body'>A count of all the component models that a hardware component model is compatible with. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#firmwareCount" name=firmwareCount>firmwareCount</a></span>
            <div class='views-field-body'>A count of  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#validAttributeTypeCount" name=validAttributeTypeCount>validAttributeTypeCount</a></span>
            <div class='views-field-body'>A count of the types of attributes that are allowed for a given hardware component model. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
            </div>
</div>


