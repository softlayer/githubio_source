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
The unique identifier for this object. It is not used anywhere but in this object.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[step]: #step
#### [step]
The number of the step in the order process for this package. These are sequential and only needed for step-based ordering.  
<span class="type-label">Type: </span>**string**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[inclusivePreviousSteps]: #inclusiveprevioussteps
#### [inclusivePreviousSteps]
The next steps in the ordering process for the package tied to this object, including this step.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package_Order_Step_Next'>SoftLayer_Product_Package_Order_Step_Next[] </a>**  



</div>
<div class="prop-row">

-----
[nextSteps]: #nextsteps
#### [nextSteps]
The next steps in the ordering process for the package tied to this object.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package_Order_Step_Next'>SoftLayer_Product_Package_Order_Step_Next[] </a>**  



</div>
<div class="prop-row">

-----
[previousSteps]: #previoussteps
#### [previousSteps]
The item to which this object belongs.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Package_Order_Step_Next'>SoftLayer_Product_Package_Order_Step_Next[] </a>**  



</div>

## Count
<div class="prop-row">

-----
[inclusivePreviousStepCount]: #inclusivepreviousstepcount
#### [inclusivePreviousStepCount]
A count of the next steps in the ordering process for the package tied to this object, including this step.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[nextStepCount]: #nextstepcount
#### [nextStepCount]
A count of the next steps in the ordering process for the package tied to this object.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[previousStepCount]: #previousstepcount
#### [previousStepCount]
A count of the item to which this object belongs.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>


