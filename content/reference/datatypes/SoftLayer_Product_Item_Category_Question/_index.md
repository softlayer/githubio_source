---
title: "SoftLayer_Product_Item_Category_Question"
description: "The SoftLayer_Product_Item_Category_Question data type represents a single question to be answered by an end user.  The... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Item_Category_Question"
---

# SoftLayer_Product_Item_Category_Question
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Product_Item_Category_Question' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Product_Item_Category_Question data type represents a single question to be answered by an end user.  The question may or may not be required which can be located by looking at the 'required' property on the item category references.  The answerValueExpression property is a regular expression that is used to validate the answer to the question.  The description and valueExample properties can be used to get an idea of the type of answer that should be provided. 





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
            <span class='views-field-title'><a href="#answerValueExpression" name=answerValueExpression>answerValueExpression</a></span>
            <div class='views-field-body'>The type of answer expected. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#description" name=description>description</a></span>
            <div class='views-field-body'>The description for the question. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#fieldTypeId" name=fieldTypeId>fieldTypeId</a></span>
            <div class='views-field-body'>The type of field to use. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>identifier for category. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#keyName" name=keyName>keyName</a></span>
            <div class='views-field-body'>The keyname for the question. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#question" name=question>question</a></span>
            <div class='views-field-body'>The question for the category. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#valueExample" name=valueExample>valueExample</a></span>
            <div class='views-field-body'>An example and/or explanation of what the answer for the question is expected to look like. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#fieldType" name=fieldType>fieldType</a></span>
            <div class='views-field-body'>The type of field that should be used in an HTML form to accept an answer from an end user. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item_Category_Question_Field_Type'>SoftLayer_Product_Item_Category_Question_Field_Type </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#itemCategoryReferences" name=itemCategoryReferences>itemCategoryReferences</a></span>
            <div class='views-field-body'>The link between an item category and an item category question. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item_Category_Question_Xref'>SoftLayer_Product_Item_Category_Question_Xref[] </a></p></div>
        </div>
                <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#itemCategoryReferenceCount" name=itemCategoryReferenceCount>itemCategoryReferenceCount</a></span>
            <div class='views-field-body'>A count of the link between an item category and an item category question. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
            </div>
</div>


