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
Identifier for category question xref record.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[itemCategoryId]: #itemcategoryid
#### [itemCategoryId]
Identifier for item category.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[locationId]: #locationid
#### [locationId]
Identifier for the question.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[questionId]: #questionid
#### [questionId]
Identifier for the question.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[required]: #required
#### [required]
Flag to indicate whether an answer is required for the question..  
<span class="type-label">Type: </span>**boolean**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[itemCategory]: #itemcategory
#### [itemCategory]
The product item category that this reference points to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Category'>SoftLayer_Product_Item_Category </a>**  



</div>
<div class="prop-row">

-----
[question]: #question
#### [question]
The item category question that this reference points to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item_Category_Question'>SoftLayer_Product_Item_Category_Question </a>**  



</div>

## Count
</div>


