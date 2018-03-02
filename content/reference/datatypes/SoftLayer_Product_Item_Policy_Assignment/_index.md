---
title: "SoftLayer_Product_Item_Policy_Assignment"
description: "Represents the assignment of a policy to a product. The existence of a record means that the associated product is subje... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Item_Policy_Assignment"
---

# SoftLayer_Product_Item_Policy_Assignment
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Product_Item_Policy_Assignment' >Datatype</a></li>
    </ul>
</div>

## Description 
Represents the assignment of a policy to a product. The existence of a record means that the associated product is subject to the terms defined in the document content of the policy. 





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
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#productId" name=productId>productId</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#policyName" name=policyName>policyName</a></span>
            <div class='views-field-body'>The name of the assigned policy. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#product" name=product>product</a></span>
            <div class='views-field-body'>The [[SoftLayer_Product_Item]] for this policy assignment. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item </a></p></div>
        </div>
                <h2>Relational</h2>
            </div>
</div>


