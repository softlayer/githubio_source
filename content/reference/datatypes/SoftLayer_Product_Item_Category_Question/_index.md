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
[answerValueExpression]: #answervalueexpression
#### [answerValueExpression]
The type of answer expected.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[description]: #description
#### [description]
The description for the question.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[fieldTypeId]: #fieldtypeid
#### [fieldTypeId]
The type of field to use.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
identifier for category.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[keyName]: #keyname
#### [keyName]
The keyname for the question.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[question]: #question
#### [question]
The question for the category.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[valueExample]: #valueexample
#### [valueExample]
An example and/or explanation of what the answer for the question is expected to look like.  
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[fieldType]: #fieldtype
#### [fieldType]
The type of field that should be used in an HTML form to accept an answer from an end user.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Category_Question_Field_Type'>SoftLayer_Product_Item_Category_Question_Field_Type </a>**


</div>
<div class="prop-row">

-----
[itemCategoryReferences]: #itemcategoryreferences
#### [itemCategoryReferences]
The link between an item category and an item category question.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Category_Question_Xref'>SoftLayer_Product_Item_Category_Question_Xref[] </a>**


</div>

## Count
<div class="prop-row">

-----
[itemCategoryReferenceCount]: #itemcategoryreferencecount
#### [itemCategoryReferenceCount]
A count of the link between an item category and an item category question.   
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


