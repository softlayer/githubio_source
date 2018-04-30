---
title: "SoftLayer_Product_Package_Order_Step"
description: "Each package has at least 1 step to the ordering process. For server orders, there are many. Each step has certain item... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Package_Order_Step"
---

# SoftLayer_Product_Package_Order_Step
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Product_Package_Order_Step' >Datatype</a></li>
    </ul>
</div>

## Description 
Each package has at least 1 step to the ordering process. For server orders, there are many. Each step has certain item categories which are displayed. This type describes the steps for each package. 





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
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>The unique identifier for this object. It is not used anywhere but in this object. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#step" name=step>step</a>
            </span>
            <div class='views-field-body'>The number of the step in the order process for this package. These are sequential and only needed for step-based ordering. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#inclusivePreviousSteps" name=inclusivePreviousSteps>inclusivePreviousSteps</a>
            </span>
            <div class='views-field-body'>The next steps in the ordering process for the package tied to this object, including this step. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Package_Order_Step_Next'>SoftLayer_Product_Package_Order_Step_Next[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#nextSteps" name=nextSteps>nextSteps</a>
            </span>
            <div class='views-field-body'>The next steps in the ordering process for the package tied to this object. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Package_Order_Step_Next'>SoftLayer_Product_Package_Order_Step_Next[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#previousSteps" name=previousSteps>previousSteps</a>
            </span>
            <div class='views-field-body'>The item to which this object belongs. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Package_Order_Step_Next'>SoftLayer_Product_Package_Order_Step_Next[] </a></p>
            </div>
        </div>
                <h2>Count</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#inclusivePreviousStepCount" name=inclusivePreviousStepCount>inclusivePreviousStepCount</a>
            </span>
            <div class='views-field-body'>A count of the next steps in the ordering process for the package tied to this object, including this step. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#nextStepCount" name=nextStepCount>nextStepCount</a>
            </span>
            <div class='views-field-body'>A count of the next steps in the ordering process for the package tied to this object. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#previousStepCount" name=previousStepCount>previousStepCount</a>
            </span>
            <div class='views-field-body'>A count of the item to which this object belongs. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
            </div>
</div>


