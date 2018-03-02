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
            <span class='views-field-title'><a href="#capacity" name=capacity>capacity</a></span>
            <div class='views-field-body'>A generic component model's capacity. The capacity of a generic component model depends on the model itself.  For Example: Hard drives have a capacity that reflects the amount of data that hard drive can store.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>decimal</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#description" name=description>description</a></span>
            <div class='views-field-body'>A brief description for a generic component model that typically defines it's function.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#hardwareComponentTypeId" name=hardwareComponentTypeId>hardwareComponentTypeId</a></span>
            <div class='views-field-body'>The internal identifier of the component type for a generic component model.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>A generic component model's internal identification number. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#units" name=units>units</a></span>
            <div class='views-field-body'>The unit of measurement for the capacity of a generic component model.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#upgradePriority" name=upgradePriority>upgradePriority</a></span>
            <div class='views-field-body'>A generic component model's upgrade priority. The upgrade priority indicates the order a generic component model should be considered over other generic component models. A higher number indicates that a generic component model receives a higher upgrade preference in comparison to a generic component model with a lower priority number.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#hardwareComponentModels" name=hardwareComponentModels>hardwareComponentModels</a></span>
            <div class='views-field-body'>A generic component model's hardware component model. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware_Component_Model'>SoftLayer_Hardware_Component_Model[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#hardwareComponentType" name=hardwareComponentType>hardwareComponentType</a></span>
            <div class='views-field-body'>A generic component model's type. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware_Component_Type'>SoftLayer_Hardware_Component_Type </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#marketingFeatures" name=marketingFeatures>marketingFeatures</a></span>
            <div class='views-field-body'>A list of features that a generic component model can provide. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware_Component_Model_Generic_MarketingFeature'>SoftLayer_Hardware_Component_Model_Generic_MarketingFeature </a></p></div>
        </div>
                <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#hardwareComponentModelCount" name=hardwareComponentModelCount>hardwareComponentModelCount</a></span>
            <div class='views-field-body'>A count of a generic component model's hardware component model. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
            </div>
</div>


