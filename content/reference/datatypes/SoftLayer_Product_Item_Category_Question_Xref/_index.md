---
title: "SoftLayer_Product_Item_Category_Question_Xref"
description: "The SoftLayer_Product_Item_Category_Question_Xref data type represents a link between an item category and an item categ... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Item_Category_Question_Xref"
---

# SoftLayer_Product_Item_Category_Question_Xref
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Product_Item_Category_Question_Xref' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Product_Item_Category_Question_Xref data type represents a link between an item category and an item category question.  It also contains a 'required' field that designates if the question is required to be answered for the given item category. 





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
            <div class='views-field-body'>Identifier for category question xref record. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#itemCategoryId" name=itemCategoryId>itemCategoryId</a>
            </span>
            <div class='views-field-body'>Identifier for item category. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#locationId" name=locationId>locationId</a>
            </span>
            <div class='views-field-body'>Identifier for the question. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#questionId" name=questionId>questionId</a>
            </span>
            <div class='views-field-body'>Identifier for the question. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#required" name=required>required</a>
            </span>
            <div class='views-field-body'>Flag to indicate whether an answer is required for the question.. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#itemCategory" name=itemCategory>itemCategory</a>
            </span>
            <div class='views-field-body'>The product item category that this reference points to. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Item_Category'>SoftLayer_Product_Item_Category </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#question" name=question>question</a>
            </span>
            <div class='views-field-body'>The item category question that this reference points to. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Product_Item_Category_Question'>SoftLayer_Product_Item_Category_Question </a></p>
            </div>
        </div>
                <h2>Count</h2>
            </div>
</div>


